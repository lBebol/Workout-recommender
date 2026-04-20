# Deliverable 02: Phase 2 - Data Preprocessing & Feature Engineering

**Status: 🚧 TO BE COMPLETED**

---

## Overview
This deliverable focuses on preparing the workout dataset for machine learning model training.

## Tasks to Complete

### 1. Data Loading & Inspection
- [ ] Load the workout dataset (`../../data/workout_dataset.csv`)
- [ ] Display first few rows
- [ ] Check data types
- [ ] Verify for missing values
- [ ] Basic statistics

### 2. Exploratory Data Analysis (EDA)
- [ ] **Visualizations to create:**
  - [ ] Bar chart: Exercises by target muscle
  - [ ] Pie chart: Difficulty distribution
  - [ ] Bar chart: Exercise types
  - [ ] Bar chart: Equipment distribution
  - [ ] Heatmap: Muscle groups vs difficulty
  - [ ] Cross-tabulation analysis

### 3. Feature Engineering
- [ ] **Label Encoding:** Convert categorical to numerical
  - [ ] target_muscles
  - [ ] equipment
  - [ ] difficulty
  - [ ] type

- [ ] **One-Hot Encoding:** Alternative encoding method
- [ ] **Feature Selection:** Choose features for ML models
- [ ] **Train-Test Split:** 80/20 split with stratification
- [ ] **Feature Scaling:** StandardScaler for normalization

---

## Files to Create
Create a Python script or Jupyter notebook that includes:

```
Notebook: 02_eda_visualization.ipynb
- All distribution plots
- Correlation analysis
- Data insights

Notebook: 03_feature_engineering.ipynb
- Label encoding
- One-hot encoding  
- Train-test split
- Feature scaling

Script: preprocessing.py
- data_loader.py - Load and clean data
- visualization.py - Create plots
- preprocessing.py - Feature engineering
```

---

## Expected Outputs
1. Clean dataset with encoded features
2. Visualization images/plots
3. Train/test datasets ready for ML
4. Documentation of preprocessing steps

---

## Author
**Abdelrahman Yasser Hassan Zaky**  
**ID:** 231000102  
**Faculty of ITCS, Nile University**

---

*Workout Recommender System - Machine Intelligence Course*