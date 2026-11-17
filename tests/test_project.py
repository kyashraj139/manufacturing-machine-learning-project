from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.project_utils import make_domain_data

def test_manufacturing_dataset():
    df, target, _ = make_domain_data("manufacturing", n=200, seed=12)
    assert len(df) == 200
    assert df[target].isin([0, 1]).all()
    assert df[target].nunique() == 2
    assert not df.isna().any().any()
