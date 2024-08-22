import os
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv(find_dotenv())
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialise the OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

def answer_question(question):
    print(f'Using OPENAI_API_KEY, {OPENAI_API_KEY}')

    messages = [
        {
            "role": "user",
            "content": question
        }
    ]
    model = "gpt-4o-mini"
    response = client.chat.completions.create(
        model=model,
        messages=messages,
    )
    return response.choices[0].message.content


if __name__ == '__main__':
    question = "What is the capital of France?"
    answer = answer_question(question)
    print(f'Question: {question}')
    print(f'Answer: {answer}')

