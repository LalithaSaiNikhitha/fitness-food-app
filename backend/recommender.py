from backend.model import generate_response
from backend.embeddings import get_food_info, load_exercise_data, get_exercise_by_category

def generate_recommendations(goal, preferences):
    # Step 1: Generate a meal plan using GPT-J
    query = f"Create a fitness and diet plan for {goal} with {preferences}."
    plan = generate_response(query)

    # Step 2: Fetch food details from Nutritionix
    food = get_food_info("chicken breast")  # Example food item

    # Step 3: Load exercise data and filter by category
    exercise_data = load_exercise_data("data/exercise_data.json")
    exercises = get_exercise_by_category(exercise_data, "Strength")

    return {
        "meal_plan": plan,
        "food_suggestions": food,
        "exercise_plan": exercises,
    }
