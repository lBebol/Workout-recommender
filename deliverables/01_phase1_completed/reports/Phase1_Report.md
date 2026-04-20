# Workout Recommender System
## Based on User Fitness Level and Goals

---

**Machine Intelligence**  
Faculty of ITCS, Nile University

**Abdelrahman Yasser Hassan Zaky**  
231000102

**Phase 1 Report**  
Dataset Collection and Initial Analysis

---

## Abstract

This report presents Phase 1 of the Workout Recommender System project, developed as part of the Machine Intelligence course requirements. The primary objective of this project is to build an intelligent system that suggests personalized exercises based on a user's fitness level and specific goals (such as cardio-focused or strength-focused training). Phase 1 focuses on dataset collection, where workout exercise data is gathered from MuscleWiki.com, a comprehensive fitness database. This report documents the data collection methodology, dataset structure, and initial analysis of the collected data.

---

## 1. Introduction

Regular physical exercise is essential for maintaining good health and achieving fitness goals. However, many individuals struggle to create effective workout routines that match their current fitness level and personal objectives. Beginners may find advanced exercises overwhelming or even injurious, while experienced athletes may become bored with exercises that no longer challenge them.

Workout recommendation systems aim to solve this problem by providing personalized exercise suggestions based on user profiles. These systems consider factors such as the user's current fitness level, available equipment, time constraints, and specific goals (e.g., building strength, improving cardiovascular health, or weight loss).

The goal of this project is to develop a Workout Recommender System that takes user input regarding their fitness level and goals, and outputs appropriate exercise recommendations. The system will analyze exercise characteristics and match them with user requirements to provide tailored suggestions.

### Key Objectives:
- Collect a comprehensive dataset of exercises with relevant attributes
- Develop a recommendation algorithm based on content-based filtering
- Implement multiple machine learning models for enhanced recommendations
- Create a user-friendly interface for inputting fitness profiles
- Evaluate model performance using appropriate metrics

---

## 2. Data Collection

### 2.1 Data Source

The dataset is collected from **MuscleWiki.com** (https://musclewiki.com), a comprehensive online fitness database that provides detailed information about various exercises. MuscleWiki is chosen as the primary data source due to several advantages:

- **Clean Structure**: Exercises are organized by muscle groups and exercise categories
- **Customization Options**: Includes difficulty levels and equipment requirements
- **Video Demonstrations**: Offers video guides for each exercise
- **Free Access**: No subscription or login required for data access
- **Comprehensive Coverage**: Includes exercises for all major muscle groups

### 2.2 Data Collection Methodology

The data collection process involved manual extraction and curation of exercise information from MuscleWiki.com. Due to anti-bot measures and access restrictions on many fitness websites, the data was collected through systematic manual identification and cataloging of exercises with their respective attributes. Each exercise was carefully verified for accuracy in target muscles, equipment requirements, difficulty level, and exercise type. The methodology follows these steps:

1. **Page Identification**: Identify target pages for each muscle group (chest, back, shoulders, arms, legs, core)
2. **Manual Extraction**: Extract exercise information including name, target muscles, equipment, and difficulty
3. **Data Verification**: Verify each entry for accuracy and consistency
4. **Data Cleaning**: Remove duplicates and normalize text formats
5. **Data Storage**: Save structured data in CSV format for analysis

### 2.3 Dataset Structure

The collected dataset includes the following attributes for each exercise:

| Field | Type | Description |
|-------|------|-------------|
| **Name** | String | Exercise name/title |
| **Target Muscles** | String | Primary muscle groups targeted |
| **Equipment** | String | Required equipment for performing the exercise |
| **Difficulty** | Enum | Beginner / Intermediate / Advanced |
| **Type** | Enum | Push / Pull / Legs / Cardio / Isolation / Core / Compound |
| **Description** | String | Brief description of the exercise |

### 2.4 Dataset Statistics

The dataset collection has been completed with the following statistics:

| Metric | Value |
|--------|-------|
| **Total Exercises** | 111 |
| **Unique Muscle Groups** | 12 |
| **Difficulty Levels** | 3 |
| **Exercise Types** | 7 |
| **Equipment Types** | 13 |

#### Distribution by Target Muscle

| Target Muscle | Count |
|--------------|-------|
| Cardiovascular | 17 |
| Chest | 15 |
| Abs | 13 |
| Back | 11 |
| Quadriceps | 11 |
| Shoulders | 10 |
| Biceps | 8 |
| Triceps | 8 |
| Glutes | 8 |
| Hamstrings | 5 |
| Calves | 4 |
| Trapezius | 1 |

#### Distribution by Difficulty

| Difficulty | Count | Percentage |
|------------|-------|------------|
| Beginner | 50 | 45% |
| Intermediate | 52 | 47% |
| Advanced | 9 | 8% |

#### Distribution by Exercise Type

| Type | Count |
|------|-------|
| Isolation | 39 |
| Push | 20 |
| Pull | 18 |
| Cardio | 16 |
| Legs | 11 |
| Core | 4 |
| Compound | 3 |

#### Distribution by Equipment

| Equipment | Count |
|-----------|-------|
| Bodyweight | 34 |
| Barbell | 21 |
| Dumbbells | 20 |
| Machine | 10 |
| Cable Machine | 10 |
| Parallel Bars | 3 |
| Cable | 3 |
| Resistance Band | 3 |
| Pull-up Bar | 3 |
| Other | 4 |

#### Table 1: Sample of Collected Exercise Dataset

| Exercise | Target | Equipment | Difficulty | Type |
|----------|--------|-----------|------------|------|
| Push-up | Chest | Bodyweight | Beginner | Push |
| Bench Press | Chest | Barbell | Intermediate | Push |
| Squat | Legs | Barbell | Intermediate | Legs |
| Pull-up | Back | Pull-up Bar | Intermediate | Pull |
| Crunches | Abs | Bodyweight | Beginner | Isolation |
| Dumbbell Curl | Biceps | Dumbbells | Beginner | Isolation |
| Deadlift | Back | Barbell | Advanced | Pull |
| Plank | Abs | Bodyweight | Beginner | Core |

---

## 3. Proposed System

### 3.1 System Overview

The Workout Recommender System will use a content-based filtering approach to recommend exercises. The system architecture consists of three main components:

1. **User Input Module**: Collects user fitness profile (level, goals, available equipment)
2. **Recommendation Engine**: Matches user profile with exercise features
3. **Output Module**: Presents recommended exercises to the user

### 3.2 System Flow

```
User Input Module
        ↓
User Profile (Level, Goals, Equipment)
        ↓
Recommendation Engine (Matching Algorithm)
        ↓
Exercise Database (111 exercises)
        ↓
Recommended Exercises
        ↓
User Output
```

*Figure 1: System Flow Diagram*

### 3.3 User Input Parameters

The system will accept the following user inputs:

- **Fitness Level**: Beginner / Intermediate / Advanced
- **Fitness Goal**: Strength (Cardio/Strength/Hybrid)
- **Available Equipment**: Bodyweight only / Home gym / Full gym
- **Target Muscle Groups**: Optional selection of focus areas

### 3.4 Recommendation Logic

The recommendation algorithm will:

1. Filter exercises by difficulty matching user's fitness level
2. Filter by available equipment
3. Match exercise type with user's fitness goals
4. Consider muscle group balance in recommendations
5. Rank exercises by relevance score

### 3.5 Technical Implementation

The system will be implemented using Python with the following tools:

- **Data Processing**: Pandas, NumPy
- **Machine Learning**: Scikit-learn
- **Interface**: Jupyter Notebook for demonstration
- **Data Visualization**: Matplotlib, Seaborn

Multiple machine learning models will be applied and compared. The selection of these models is based on their suitability for recommendation systems and classification tasks with categorical features:

- **K-Nearest Neighbors (KNN)**: A simple yet effective algorithm that finds exercises similar to user preferences based on feature distance. Ideal for content-based filtering where we match exercise attributes (difficulty, equipment, type) with user profile.

- **Decision Tree Classifier**: Provides interpretable rules for exercise recommendations. The tree structure naturally handles categorical features and can explain why a specific exercise was recommended (e.g., "if user_level=beginner AND goal=cardio THEN recommend push-ups").

- **Random Forest Classifier**: An ensemble method that combines multiple decision trees for more robust predictions. Handles mixed feature types well and reduces overfitting compared to single decision trees.

- **Naive Bayes Classifier**: Works well with categorical and text features. Efficient and performs surprisingly well even when features are not fully independent, which is suitable for exercise classification based on attributes.

- **Support Vector Machine (SVM)**: Effective for classification with clear decision boundaries. Handles both linear and non-linear relationships through kernel functions, useful for distinguishing between exercise categories.

These models will be evaluated using accuracy, precision, recall, and F1-score to determine the best performing recommendation approach.

---

## 4. Conclusion & Future Work

### 4.1 Conclusion

Phase 1 of the Workout Recommender System project has been successfully completed. A comprehensive dataset of 111 exercises has been collected from MuscleWiki.com, covering 12 different muscle groups with diverse equipment requirements and difficulty levels.

The dataset is well-balanced with 45% beginner exercises, 47% intermediate, and 8% advanced, making it suitable for building a recommendation system that serves users at all fitness levels. The variety in exercise types (push, pull, legs, cardio, isolation, core, compound) ensures comprehensive workout recommendations.

### 4.2 Challenges Encountered

During Phase 1, several challenges were encountered:

- Many fitness websites block automated scraping due to anti-bot measures
- Data required manual verification for accuracy
- Ensuring consistent categorization across all exercises

These challenges were addressed through careful data validation and quality control procedures.

### 4.3 Future Work

The following tasks are planned for Phase 2:

1. Implement the recommendation algorithm using content-based filtering
2. Apply and compare multiple machine learning models
3. Develop a user interface for demonstration
4. Evaluate model performance with appropriate metrics
5. Prepare final project documentation and presentation

The project aims to deliver a functional workout recommendation system that can effectively match users with appropriate exercises based on their individual profiles.

---

## References

1. MuscleWiki. https://musclewiki.com/
2. Scikit-learn: Machine Learning in Python. https://scikit-learn.org/
3. Pandas: Python Data Analysis Library. https://pandas.pydata.org/
4. Machine Intelligence Course Guidelines, Faculty of ITCS, Nile University

---

## Appendix: Dataset Schema

The final dataset includes the following fields:

| Field | Type | Description |
|-------|------|-------------|
| name | String | Exercise name |
| target_muscles | String | Primary muscle groups targeted |
| equipment | String | Required equipment |
| difficulty | Enum | Beginner, Intermediate, Advanced |
| type | Enum | Push, Pull, Legs, Cardio, Isolation, Core, Compound |
| description | String | Brief exercise description |

---
