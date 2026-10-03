import csv
from pathlib import Path

def test_dataset_has_1000_rows():
    p=Path(__file__).resolve().parents[1]/"data/social_media_privacy_assessments.csv"
    with p.open(encoding="utf-8") as f:
        rows=list(csv.DictReader(f))
    assert len(rows)==1000

def test_dataset_is_synthetic():
    p=Path(__file__).resolve().parents[1]/"data/social_media_privacy_assessments.csv"
    with p.open(encoding="utf-8") as f:
        row=next(csv.DictReader(f))
    assert row["profile_id"].startswith("SYN-")
