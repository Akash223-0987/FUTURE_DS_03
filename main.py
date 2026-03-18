import sys
sys.path.insert(0, ".")

from src.data_preprocessing import run as preprocess
from src.feature_engineering import run as engineer
from src.funnel_analysis import run as analyze

print("=" * 55)
print("   LEAD SCORING — MARKETING FUNNEL ANALYSIS PIPELINE")
print("=" * 55)

df = preprocess()
df, metrics, drop_stages = engineer(df)
analyze(df, metrics, drop_stages)
