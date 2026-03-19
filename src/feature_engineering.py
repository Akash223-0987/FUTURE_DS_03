import pandas as pd

def add_funnel_flags(df):
    """
    Apply sequential funnel flagging:
    All Visitors -> Engaged (Time spent) -> Qualified (Page views) -> Customers (Converted)
    Ensure each stage is a subset of the previous one for valid funnel reporting.
    """
    # 3. Customer: Successfully Converted (Final step)
    df["Customer"] = df["Converted"] == 1
    
    # 2. Qualified: Met behavioral qualification OR became a Customer
    df["Qualified"] = ((df["Total Time Spent on Website"] > 300) & (df["Page Views Per Visit"] > 3)) | df["Customer"]
    
    # 1. Engaged: Spent more than 300 seconds OR is Qualified (which includes Customers)
    df["Engaged"] = (df["Total Time Spent on Website"] > 300) | df["Qualified"]
    
    return df

def compute_conversion_metrics(df):
    """Calculate and return funnel counts and rates."""
    counts = {
        "Total Visitors": len(df),
        "Total Engaged": int(df["Engaged"].sum()),
        "Total Qualified": int(df["Qualified"].sum()),
        "Total Customers": int(df["Customer"].sum()),
    }
    
    # Calculate conversion percentages
    v = counts["Total Visitors"]
    e = counts["Total Engaged"]
    q = counts["Total Qualified"]
    c = counts["Total Customers"]
    
    metrics = {
        **counts,
        "Visitor to Lead (%)": round((e / v) * 100, 2) if v else 0,
        "Lead to Customer (%)": round((c / e) * 100, 2) if e else 0,
        "Overall Conversion (%)": round((c / v) * 100, 2) if v else 0,
    }
    
    # Attach scalar metrics for easier Power BI usage
    df["Visitor_to_Lead_pct"] = metrics["Visitor to Lead (%)"]
    df["Lead_to_Customer_pct"] = metrics["Lead to Customer (%)"]
    df["Overall_Conversion_pct"] = metrics["Overall Conversion (%)"]
    
    return df, metrics

def dropoff_analysis(m):
    """Return counts of leads lost at each step."""
    stages = {
        "Visitors -> Engaged": m["Total Visitors"] - m["Total Engaged"],
        "Engaged -> Qualified": m["Total Engaged"] - m["Total Qualified"],
        "Qualified -> Customer": m["Total Qualified"] - m["Total Customers"],
    }
    
    print("\n[FUNNEL STAGES]")
    print(f"  Visitors:  {m['Total Visitors']:,}")
    print(f"  Engaged:   {m['Total Engaged']:,}  ({m['Visitor to Lead (%)']}%)")
    print(f"  Qualified: {m['Total Qualified']:,}")
    print(f"  Customers: {m['Total Customers']:,}  ({m['Overall Conversion (%)']}% overall)")
    
    return stages

def run(df):
    df = add_funnel_flags(df)
    df, metrics = compute_conversion_metrics(df)
    drop_stages = dropoff_analysis(metrics)
    return df, metrics, drop_stages

if __name__ == "__main__":
    import sys
    sys.path.insert(0, ".")
    from src.data_preprocessing import run as preprocess
    df = preprocess()
    run(df)
