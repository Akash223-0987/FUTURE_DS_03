import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns
import os

PROCESSED_DIR = "data/processed"
OUTPUT_DIR = "outputs"

def channel_analysis(df, min_leads=10):
    """Calculate conversion rates per channel, filtering low-volume sources."""
    channel_df = df.groupby("Lead Source").agg(
        Total_Leads=("Converted", "count"),
        Converted_Leads=("Converted", "sum")
    ).reset_index()

    channel_df["Conversion_Rate_pct"] = round(
        (channel_df["Converted_Leads"] / channel_df["Total_Leads"]) * 100, 2
    )
    
    # Sort for best/worst (Top performer must have at least min_leads)
    reliable = channel_df[channel_df["Total_Leads"] >= min_leads].sort_values("Conversion_Rate_pct", ascending=False)
    
    best = reliable.iloc[0] if not reliable.empty else channel_df.iloc[0]
    worst = reliable.iloc[-1] if not reliable.empty else channel_df.iloc[-1]
    
    print("\n[CHANNELS]")
    print(reliable.head(10).to_string(index=False))
    print(f"\n  [BEST]  {best['Lead Source']} ({best['Conversion_Rate_pct']}%)")
    print(f"  [WORST] {worst['Lead Source']} ({worst['Conversion_Rate_pct']}%)")
    
    return channel_df, best, worst

def save_outputs(df, metrics, drop_stages, channel_df):
    os.makedirs(PROCESSED_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    df.to_csv(f"{PROCESSED_DIR}/lead_data_final.csv", index=False)
    
    funnel_summary = pd.DataFrame([
        {"Stage": "Visitors",  "Count": metrics["Total Visitors"]},
        {"Stage": "Engaged",   "Count": metrics["Total Engaged"]},
        {"Stage": "Qualified", "Count": metrics["Total Qualified"]},
        {"Stage": "Customers", "Count": metrics["Total Customers"]},
    ])
    funnel_summary.to_csv(f"{PROCESSED_DIR}/funnel_summary.csv", index=False)
    channel_df.to_csv(f"{PROCESSED_DIR}/channel_performance.csv", index=False)
    
    print(f"\n[OK] CSVs generated in {PROCESSED_DIR}")

def plot_outputs(metrics, channel_df):
    # Set style
    sns.set_theme(style="whitegrid")
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    # --- Funnel Plot ---
    stages = ["Visitors", "Engaged", "Qualified", "Customers"]
    vals = [metrics["Total Visitors"], metrics["Total Engaged"], metrics["Total Qualified"], metrics["Total Customers"]]
    
    sns.barplot(x=stages, y=vals, hue=stages, palette="magma", ax=ax1, legend=False)
    ax1.set_title("Marketing Funnel Counts", fontweight="bold", fontsize=14)
    ax1.yaxis.set_major_formatter(mtick.FuncFormatter(lambda x, p: f"{int(x):,}"))
    
    # --- Channel Plot ---
    top_v = channel_df.sort_values("Total_Leads", ascending=False).head(10)
    sns.barplot(data=top_v, x="Lead Source", y="Conversion_Rate_pct", 
                hue="Lead Source", palette="viridis", ax=ax2, legend=False)
    ax2.set_title("Conversion Rate by Top Channels", fontweight="bold", fontsize=14)
    plt.xticks(rotation=45, ha="right")
    
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/marketing_dashboard_preview.png", dpi=180)
    print(f"[OK] Plots saved to {OUTPUT_DIR}")
    plt.close()

def run(df, metrics, drop_stages):
    channel_df, best, worst = channel_analysis(df)
    save_outputs(df, metrics, drop_stages, channel_df)
    plot_outputs(metrics, channel_df)
    
    print("\n" + "=" * 55)
    print(f"  Overall Conv Rate    : {metrics['Overall Conversion (%)']}%")
    # Identify the drop off only where there is a real drop-off (Stages)
    print(f"  Biggest Drop-off Stage: {max(drop_stages, key=drop_stages.get)}")
    print("=" * 55)

if __name__ == "__main__":
    import sys
    sys.path.insert(0, ".")
    from src.data_preprocessing import run as preprocess
    from src.feature_engineering import run as engineer
    df = preprocess()
    df, metrics, drop_stages = engineer(df)
    run(df, metrics, drop_stages)
