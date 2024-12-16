from transformers import pipeline

# Load GPT-J model
generator = pipeline("text-generation", model="EleutherAI/gpt-neo-2.7B")
#generator = pipeline("text-generation", model="EleutherAI/gpt-j-6B")

def generate_response(prompt):
    response = generator(prompt, max_length=100, do_sample=True)
    return response[0]['generated_text']
