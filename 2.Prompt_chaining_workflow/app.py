import openai
from dotenv import load_dotenv
load_dotenv()


os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")


openai.api_key=os.getenv("OPENAI_API_KEY")

# Function to call OpenAI API
def call_openai(prompt, model="text-davinci-003", max_tokens=100):
    """
    Function to call OpenAI API with a given prompt.
    """
    try:
        response = openai.Completion.create(
            engine=model,
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=0.7
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error: {e}")
        return None

# Step 1: Generate Marketing Copy
def generate_marketing_copy(product_description):
    """
    Generate marketing copy based on the product description.
    """
    prompt = f"Write a compelling marketing copy for the following product:\n\n{product_description}"
    marketing_copy = call_openai(prompt, max_tokens=150)
    return marketing_copy

# Step 2: Translate Marketing Copy
def translate_marketing_copy(marketing_copy, target_language):
    """
    Translate the marketing copy into the target language.
    """
    prompt = f"Translate the following marketing copy into {target_language}:\n\n{marketing_copy}"
    translated_copy = call_openai(prompt, max_tokens=150)
    return translated_copy

# Main workflow
def prompt_chaining_workflow(product_description, target_language):
    """
    Execute the prompt chaining workflow.
    """
    print(f"Product Description: {product_description}")
    
    # Step 1: Generate Marketing Copy
    print("\nStep 1: Generating marketing copy...")
    marketing_copy = generate_marketing_copy(product_description)
    if not marketing_copy:
        print("Failed to generate marketing copy.")
        return
    print(f"Marketing Copy:\n{marketing_copy}")
    
    # Step 2: Translate Marketing Copy
    print("\nStep 2: Translating marketing copy...")
    translated_copy = translate_marketing_copy(marketing_copy, target_language)
    if not translated_copy:
        print("Failed to translate marketing copy.")
        return
    print(f"Translated Copy ({target_language}):\n{translated_copy}")

# Run the workflow
if _name_ == "_main_":
    product_description = "A revolutionary new smartwatch that tracks your fitness, monitors your health, and keeps you connected."
    target_language = "Spanish"
    prompt_chaining_workflow(product_description, target_language)