"""
Phase One - Initial Report Generator
Creates a report based on the collected dataset.
"""

import pandas as pd
import os
from datetime import datetime

DATA_PATH = os.path.join(os.path.dirname(__file__), '../data/workout_dataset.csv')
REPORT_PATH = os.path.join(os.path.dirname(__file__), '../reports/phase_one_report.md')

def generate_report():
    df = pd.read_csv(DATA_PATH)
    
    report = f"""# Phase One Report: Workout Recommender Dataset

**Date:** {datetime.now().strftime('%Y-%m-%d')}  
**Project:** Workout Recommender System  
**Course:** Machine Intelligence

---

## 1. Data Source Description

The dataset was collected from publicly available fitness databases:
- **Primary Sources:** Fitness websites with exercise libraries
- **Data Type:** Structured exercise information
- **Collection Method:** Web scraping / manual curation

## 2. Dataset Statistics

| Metric | Value |
|--------|-------|
| Total Exercises | {len(df)} |
| Unique Muscle Groups | {df['target_muscles'].nunique()} |
| Equipment Types | {df['equipment'].nunique()} |

### Distribution by Difficulty
{df['difficulty'].value_counts().to_markdown()}

### Distribution by Workout Type
{df['type'].value_counts().to_markdown()}

### Top Target Muscles
{df['target_muscles'].value_counts().head(10).to_markdown()}

### Equipment Used
{df['equipment'].value_counts().to_markdown()}

## 3. Data Schema

| Field | Type | Description |
|-------|------|-------------|
| name | string | Exercise name |
| target_muscles | list | Primary muscle groups targeted |
| equipment | string | Required equipment |
| difficulty | enum | beginner/intermediate/advanced |
| type | enum | push/pull/legs/cardio/isolation/compound |
| description | string | Brief exercise description |

## 4. Methodology

### Data Collection Process
1. Identified fitness data sources
2. Scraped exercise information programmatically
3. Cleaned and structured data into CSV format
4. Validated data completeness and consistency

### Challenges Encountered
- Some websites block automated access
- Inconsistent data formats across sources
- Equipment categorization required manual review

## 5. Next Steps (Phase Two)

- Build recommendation engine using content-based filtering
- Apply ML models: KNN, Decision Trees, Random Forest, etc.
- Create user interface for fitness level input
- Validate recommendations with fitness professionals

---

*Report generated automatically from dataset analysis.*
"""
    
    os.makedirs(os.path.dirname(REPORT_PATH), exist_ok=True)
    with open(REPORT_PATH, 'w') as f:
        f.write(report)
    
    print(f"✓ Report saved to: {REPORT_PATH}")
    print(f"\nDataset Summary:")
    print(f"  - Total exercises: {len(df)}")
    print(f"  - Difficulty levels: {df['difficulty'].unique().tolist()}")
    print(f"  - Workout types: {df['type'].unique().tolist()}")

if __name__ == "__main__":
    generate_report()
