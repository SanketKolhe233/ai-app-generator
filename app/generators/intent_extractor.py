from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv

import json
import os

# Load environment variables
load_dotenv()

# Create client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Schema
class IntentSchema(BaseModel):
    app_type: str
    features: list[str]
    roles: list[str]

# Main function
def extract_intent(user_prompt: str):

    system_prompt = """
    You are an intent extraction engine.

    Return ONLY valid JSON.

    No markdown.
    No explanation.
    No code blocks.

    Required schema:

    {
      "app_type": "string",
      "features": [],
      "roles": []
    }
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        temperature=0.1,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ]
    )

    content = response.choices[0].message.content

    data = json.loads(content)

    validated = IntentSchema(**data)

    return validated.model_dump()

# Test
print(extract_intent(
    "Build a food delivery app with admin dashboard, customer login, and delivery tracking"
))
