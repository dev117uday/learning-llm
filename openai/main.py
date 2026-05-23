import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)

response = client.responses.create(
    model="gpt-5-nano", input="Hello, introduce yourself to me ?"
)

print(response.output_text)
print(response.metadata)
