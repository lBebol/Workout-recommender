"""
Workout Recommender - Data Collection Script
Run this script to scrape exercise data from available sources.
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import csv
import os

OUTPUT_FILE = os.path.join(os.path.dirname(__file__), '../data/workout_dataset.csv')

def scrape_musclewiki():
    """Scrape from MuscleWiki API"""
    exercises = []
    
    # MuscleWiki has a simple API
    muscles = ['chest', 'back', 'shoulders', 'biceps', 'triceps', 
               'quadriceps', 'hamstrings', 'glutes', 'calves', 'abs']
    
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; WorkoutRecommender/1.0)'}
    
    for muscle in muscles:
        url = f"https://musclewiki.com/api/exercises?category={muscle}"
        try:
            resp = requests.get(url, headers=headers, timeout=10)
            if resp.status_code == 200:
                data = resp.json()
                for item in data:
                    exercises.append({
                        'name': item.get('name', ''),
                        'target_muscles': [muscle],
                        'equipment': item.get('equipment', 'bodyweight'),
                        'difficulty': item.get('difficulty', 'intermediate'),
                        'type': classify_type(item.get('name', ''), muscle),
                        'description': item.get('description', '')
                    })
                print(f"✓ {muscle}: {len(data)} exercises")
            time.sleep(0.5)
        except Exception as e:
            print(f"✗ {muscle}: {e}")
    
    return exercises

def classify_type(name, muscle):
    """Classify workout type"""
    name_lower = name.lower()
    if any(x in name_lower for x in ['crunch', 'curl', 'fly']):
        return 'isolation'
    elif any(x in name_lower for x in ['run', 'jump', 'burpee', 'cardio']):
        return 'cardio'
    return 'compound'

def save_to_csv(exercises):
    """Save exercises to CSV"""
    if exercises:
        df = pd.DataFrame(exercises)
        df.to_csv(OUTPUT_FILE, index=False)
        print(f"\n✓ Saved {len(exercises)} exercises to {OUTPUT_FILE}")
        return df
    return None

if __name__ == "__main__":
    print("Scraping workout data...\n")
    exercises = scrape_musclewiki()
    if exercises:
        df = save_to_csv(exercises)
        print(f"\nDataset ready: {len(df)} exercises")
    else:
        print("No exercises scraped. Try running manually or check connection.")
