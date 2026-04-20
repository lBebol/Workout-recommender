# Deliverable 02: Phase 2 - Data Preprocessing & Feature Engineering

**Status: 🚧 TO BE COMPLETED**

---

## Student Information
- **Name:** Abdelrahman Yasser Hassan Zaky
- **ID:** 231000102
- **University:** Faculty of ITCS, Nile University

---

## Objective
Prepare the workout dataset for machine learning by loading, analyzing, and transforming the data into a format suitable for model training.

---

## Work Location

Create files in:
```
/home/bebo/Projects/Machine intelligence/notebooks/
```

---

## Task 1: Data Loading & Exploratory Data Analysis

### File Name
`02_data_loading_eda.ipynb`

### Steps to Complete

#### 1. Import Required Libraries
- pandas
- numpy
- matplotlib
- seaborn
- Enable inline plotting

#### 2. Load the Dataset
- Read from: `../data/workout_dataset.csv`
- Display total number of rows and columns

#### 3. Initial Data Inspection
- Display first 5 rows of the dataset
- Show data types for each column
- Check for missing values
- Show basic statistical summary

#### 4. Create Visualizations

Save all plots to: `/home/bebo/Projects/Machine intelligence/reports/`

**Plot 1 - Exercises by Target Muscle (Bar Chart)**
- Title: "Distribution of Exercises by Target Muscle"
- X-axis: Target Muscle
- Y-axis: Count
- Color: Steel blue
- Save as: `muscle_distribution.png`

**Plot 2 - Difficulty Distribution (Pie Chart)**
- Title: "Exercise Difficulty Distribution"
- Show percentage for each difficulty level
- Colors: Green (beginner), Orange (intermediate), Red (advanced)
- Save as: `difficulty_distribution.png`

**Plot 3 - Exercise Type Distribution (Bar Chart)**
- Title: "Distribution by Exercise Type"
- X-axis: Type
- Y-axis: Count
- Color: Coral
- Save as: `type_distribution.png`

**Plot 4 - Equipment Distribution (Bar Chart)**
- Title: "Distribution by Equipment"
- X-axis: Equipment type
- Y-axis: Count
- Color: Medium sea green
- Save as: `equipment_distribution.png`

**Plot 5 - Heatmap (Muscle vs Difficulty)**
- Title: "Muscle Groups by Difficulty"
- Cross-tabulation between target_muscles and difficulty
- Annotation enabled
- Colormap: YlOrRd
- Save as: `heatmap.png`

---

## Task 2: Feature Engineering

### File Name
`03_feature_engineering.ipynb`

### Steps to Complete

#### 1. Load the Original Dataset
- Read `workout_dataset.csv` again

#### 2. Label Encoding
Convert these categorical columns to numerical:
- target_muscles → target_muscles_enc
- equipment → equipment_enc
- difficulty → difficulty_enc
- type → type_enc

Print the encoding mappings for each column.

#### 3. Feature Selection
Select these columns as features:
- target_muscles_enc
- equipment_enc
- difficulty_enc
- type_enc

Set `type_enc` as the target variable (what we want to predict).

#### 4. Train-Test Split
- Training set: 80%
- Test set: 20%
- Use stratified sampling
- Random state: 42

Display the number of samples in each set.

#### 5. Feature Scaling
- Use StandardScaler
- Fit on training data
- Transform both training and test data

Display the mean and standard deviation of scaled training data.

#### 6. Save Processed Data
Save to: `/home/bebo/Projects/Machine intelligence/data/processed_data.pkl`

Include:
- X_train, X_test, y_train, y_test
- Scaled versions of X_train and X_test
- Label encoders (muscle, equipment, difficulty, type)
- Scaler object

---

## Output Files Summary

| File | Save Location |
|------|---------------|
| muscle_distribution.png | reports/ |
| difficulty_distribution.png | reports/ |
| type_distribution.png | reports/ |
| equipment_distribution.png | reports/ |
| heatmap.png | reports/ |
| processed_data.pkl | data/ |

---

## Deliverable Checklist

- [ ] Created `02_data_loading_eda.ipynb`
- [ ] Loaded and inspected dataset
- [ ] Created all 5 visualizations
- [ ] Saved all plots to reports folder
- [ ] Created `03_feature_engineering.ipynb`
- [ ] Applied label encoding to all 4 categorical features
- [ ] Performed train-test split (80/20)
- [ ] Applied feature scaling
- [ ] Saved processed data as pickle file

---

## Notes
- Keep the dataset in: `data/workout_dataset.csv` (do not move it)
- All visualizations go to: `reports/`
- Processed data for next deliverable goes to: `data/processed_data.pkl`

---

*Deliverable 02 - Machine Intelligence Course - Nile University*