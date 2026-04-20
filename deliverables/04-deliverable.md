# Deliverable 04: Phase 2 - Model Evaluation, Recommendation Engine & Final Demo

**Status: 🚧 TO BE COMPLETED**

---

## Student Information
- **Name:** Abdelrahman Yasser Hassan Zaky
- **ID:** 231000102
- **University:** Faculty of ITCS, Nile University

---

## Objective
Evaluate all trained models, build the recommendation engine, and create a final demonstration.

---

## Work Location

Create files in:
```
/home/bebo/Projects/Machine intelligence/notebooks/
```

Load models from:
```
/home/bebo/Projects/Machine intelligence/data/*.pkl
```

---

## Part 1: Model Evaluation & Comparison

### File Name
`09_model_comparison.ipynb`

### Steps to Complete

#### 1. Load All Models
Load these saved models:
- knn_model.pkl
- decision_tree_model.pkl
- random_forest_model.pkl
- naive_bayes_model.pkl
- svm_model.pkl

#### 2. Load Test Data
Load the test data from processed_data.pkl

#### 3. Evaluate Each Model
For each of the 5 models, calculate:
- Accuracy Score
- Precision Score
- Recall Score
- F1 Score

#### 4. Create Comparison Table

| Model | Accuracy | Precision | Recall | F1-Score |
|-------|----------|-----------|--------|----------|
| KNN | | | | |
| Decision Tree | | | | |
| Random Forest | | | | |
| Naive Bayes | | | | |
| SVM | | | | |

#### 5. Create Visualizations

**Plot 1 - Model Accuracy Comparison (Bar Chart)**
- Title: "Model Accuracy Comparison"
- X-axis: Model names
- Y-axis: Accuracy
- Save as: `accuracy_comparison.png`

**Plot 2 - Multi-Metric Comparison (Grouped Bar Chart)**
- Show all 4 metrics for all models
- Save as: `metrics_comparison.png`

**Plot 3 - Confusion Matrices**
- Create subplots with all 5 confusion matrices
- Save as: `confusion_matrices.png`

#### 6. Cross-Validation
- Perform 5-fold cross-validation on each model
- Report mean and standard deviation
- Identify most stable model

#### 7. Best Model Selection
- Identify the best performing model
- Justify selection based on metrics

#### 8. Save Results
- Save comparison results to: `data/model_comparison_results.pkl`

---

## Part 2: Recommendation Engine

### File Name
`10_recommendation_engine.ipynb`

### Steps to Complete

#### 1. Load Best Model
Load the best performing model from Part 1

#### 2. Load Label Encoders
Load the label encoders to convert between encoded and original values

#### 3. Create User Input Function
Build a function that accepts:
- Fitness level: "beginner", "intermediate", or "advanced"
- Goal: "cardio", "strength", or "hybrid"
- Available equipment: list of equipment user has access to

#### 4. Build Recommendation Algorithm
The algorithm should:
- Filter exercises by difficulty matching user's fitness level
- Filter by available equipment
- Match exercise type to user's goal
- Return top 5-10 recommendations

#### 5. Create Recommendation Function
```python
def recommend_exercises(user_level, user_goal, available_equipment):
    # Implementation
    # Return list of recommended exercises
```

#### 6. Test with Example Users

**Test Case 1 - Beginner, Cardio, Bodyweight Only**
- Show input parameters
- Show recommended exercises
- Display exercise details

**Test Case 2 - Intermediate, Strength, Full Gym**
- Show input parameters
- Show recommended exercises
- Display exercise details

**Test Case 3 - Advanced, Hybrid, Home Gym**
- Show input parameters
- Show recommended exercises
- Display exercise details

#### 7. Save Recommendation Engine
- Save to: `data/recommendation_engine.pkl`

---

## Part 3: Final Demo

### File Name
`11_final_demo.ipynb`

### Steps to Complete

#### 1. Create Interactive Demo
Build a simple command-line or notebook-based demo that:
- Asks user for their fitness level
- Asks user for their fitness goal
- Asks user for available equipment
- Displays personalized recommendations

#### 2. Demo Scenarios
Run at least 3 different scenarios showing:
- Beginner user
- Intermediate user
- Advanced user

For each scenario:
- Show the user input
- Show the recommendation output
- Explain why these exercises were recommended

#### 3. Display Results
Show for each recommended exercise:
- Exercise name
- Target muscles
- Equipment needed
- Difficulty level
- Brief description

#### 4. Summary Statistics
- Total recommendations made
- Distribution of recommended exercises by type
- Distribution by difficulty

---

## Output Files Summary

| File | Save Location |
|------|---------------|
| 09_model_comparison.ipynb | notebooks/ |
| 10_recommendation_engine.ipynb | notebooks/ |
| 11_final_demo.ipynb | notebooks/ |
| accuracy_comparison.png | reports/ |
| metrics_comparison.png | reports/ |
| confusion_matrices.png | reports/ |
| model_comparison_results.pkl | data/ |
| recommendation_engine.pkl | data/ |

---

## Deliverable Checklist

### Part 1 - Model Evaluation:
- [ ] Loaded all 5 trained models
- [ ] Evaluated each model with all metrics
- [ ] Created comparison table
- [ ] Created accuracy comparison chart
- [ ] Created metrics comparison chart
- [ ] Created confusion matrix visualization
- [ ] Performed cross-validation
- [ ] Identified best model

### Part 2 - Recommendation Engine:
- [ ] Built user input function
- [ ] Created recommendation algorithm
- [ ] Tested with 3 different user profiles
- [ ] Saved recommendation engine

### Part 3 - Final Demo:
- [ ] Created interactive demo interface
- [ ] Ran 3+ demo scenarios
- [ ] Displayed exercise details for each recommendation
- [ ] Included summary statistics

---

## Additional Notes
- All visualization outputs go to: `reports/`
- All model and data outputs go to: `data/`
- Keep notebooks in: `notebooks/`

---

*Deliverable 04 - Machine Intelligence Course - Nile University*