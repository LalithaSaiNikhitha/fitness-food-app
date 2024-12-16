import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))

import streamlit as st
from backend.recommender import generate_recommendations


st.title("Personalized Fitness and Diet Advisor")

goal = st.text_input("Enter your fitness goal:")
preferences = st.text_input("Enter dietary preferences:")
if st.button("Get Recommendations"):
    result = generate_recommendations(goal, preferences)
    st.subheader("Meal Plan")
    st.write(result["meal_plan"])
    st.subheader("Food Suggestions")
    st.json(result["food_suggestions"])
    st.subheader("Exercise Plan")
    for exercise in result["exercise_plan"]:
        st.write(f"- {exercise['name']}: {exercise['instructions']}")
