# Deliverable 03: Phase 2 - Model Training & Implementation

**Status: 🚧 TO BE COMPLETED**

---

## Student Information
- **Name:** Abdelrahman Yasser Hassan Zaky
- **ID:** 231000102
- **University:** Faculty of ITCS, Nile University

---

## Objective
Train and implement 5 different machine learning models for the workout recommendation system.

---

## Work Location

Create files in:
```
/home/bebo/Projects/Machine intelligence/notebooks/
```

Load processed data from:
```
/home/bebo/Projects/Machine intelligence/data/processed_data.pkl
```

---

## Model 1: K-Nearest Neighbors (KNN)

### File Name
`04_knn_model.ipynb`

### Steps to Complete

1. **Load Processed Data**
   - Load the pickle file created in deliverable 02
   - Extract X_train, X_test, y_train, y_test

2. **Implement KNN Classifier**
   - Use scikit-learn's KNeighborsClassifier

3. **Find Optimal K Value**
   - Test K values from 1 to 20
   - Plot accuracy vs K value (elbow curve)
   - Select the best K value

4. **Train the Model**
   - Train with optimal K

5. **Evaluate**
   - Accuracy score
   - Precision, Recall, F1-Score
   - Confusion matrix
   - Classification report

6. **Save Model**
   - Save to: `data/knn_model.pkl`

---

## Model 2: Decision Tree Classifier

### File Name
`05_decision_tree_model.ipynb`

### Steps to Complete

1. **Load Processed Data**

2. **Implement Decision Tree**
   - Use DecisionTreeClassifier from scikit-learn
   - Set max_depth between 5-10

3. **Train the Model**

4. **Evaluate**
   - Accuracy score
   - Precision, Recall, F1-Score
   - Confusion matrix
   - Classification report

5. **Feature Importance**
   - Extract and display feature importance
   - Show which features matter most

6. **Save Model**
   - Save to: `data/decision_tree_model.pkl`

---

## Model 3: Random Forest Classifier

### File Name
`06_random_forest_model.ipynb`

### Steps to Complete

1. **Load Processed Data**

2. **Implement Random Forest**
   - Use RandomForestClassifier
   - Set n_estimators to 100
   - Set max_depth between 5-10

3. **Train the Model**

4. **Evaluate**
   - Accuracy score
   - Precision, Recall, F1-Score
   - Confusion matrix
   - Classification report

5. **Feature Importance**
   - Extract and display feature importance
   - Compare with single Decision Tree

6. **Save Model**
   - Save to: `data/random_forest_model.pkl`

---

## Model 4: Naive Bayes Classifier

### File Name
`07_naive_bayes_model.ipynb`

### Steps to Complete

1. **Load Processed Data**

2. **Implement Naive Bayes**
   - Use GaussianNB or MultinomialNB
   - Try both and compare

3. **Train the Model**

4. **Evaluate**
   - Accuracy score
   - Precision, Recall, F1-Score
   - Confusion matrix
   - Classification report

5. **Save Model**
   - Save to: `data/naive_bayes_model.pkl`

---

## Model 5: Support Vector Machine (SVM)

### File Name
`08_svm_model.ipynb`

### Steps to Complete

1. **Load Processed Data**

2. **Implement SVM**
   - Use SVC from scikit-learn
   - Try different kernels: linear, rbf
   - Use scaled data for better performance

3. **Train the Model**

4. **Evaluate**
   - Accuracy score
   - Precision, Recall, F1-Score
   - Confusion matrix
   - Classification report

5. **Kernel Comparison**
   - Compare results with different kernels

6. **Save Model**
   - Save to: `data/svm_model.pkl`

---

## Output Files Summary

| Model | Notebook | Saved Model |
|-------|----------|-------------|
| KNN | 04_knn_model.ipynb | data/knn_model.pkl |
| Decision Tree | 05_decision_tree_model.ipynb | data/decision_tree_model.pkl |
| Random Forest | 06_random_forest_model.ipynb | data/random_forest_model.pkl |
| Naive Bayes | 07_naive_bayes_model.ipynb | data/naive_bayes_model.pkl |
| SVM | 08_svm_model.ipynb | data/svm_model.pkl |

---

## Deliverable Checklist

### For Each Model (5 total):
- [ ] Created notebook for the model
- [ ] Loaded processed data
- [ ] Implemented the model
- [ ] Trained the model
- [ ] Evaluated with all metrics (accuracy, precision, recall, F1)
- [ ] Created confusion matrix
- [ ] Saved the trained model

### Additional:
- [ ] KNN: Found optimal K value and plotted elbow curve
- [ ] Decision Tree: Extracted feature importance
- [ ] Random Forest: Extracted feature importance, compared with Decision Tree
- [ ] SVM: Compared different kernels

---

## Notes
- Load data from: `data/processed_data.pkl`
- Save all trained models to: `data/` folder
- Use `.pkl` extension for model files

---

*Deliverable 03 - Machine Intelligence Course - Nile University*