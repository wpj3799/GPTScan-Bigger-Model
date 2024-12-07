import openai
from config import OPENAI_API_KEY, MODEL

# Set the OpenAI API key
openai.api_key = OPENAI_API_KEY

# Just ask the AI a question and return the response in a string
def query(question: str):
    # Prepare the request payload
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": question}
    ]

    # Send the request to the OpenAI API
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=messages,
        temperature=0.7
    )

    # Extract the model's response
    answer = response.choices[0].message['content']
    return answer
