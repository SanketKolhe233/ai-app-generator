from groq import Groq
from dotenv import load_dotenv

import os
import json

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_schema(architecture):

    system_prompt = """
    You are a schema generation engine.

    Return ONLY raw valid JSON.

    Generate:

    1. database_schema
    2. api_schema
    3. ui_schema
    4. auth_schema

    Do not explain anything.

    Required format:

    {
      "database_schema": {},
      "api_schema": {},
      "ui_schema": {},
      "auth_schema": {}
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
                "content": json.dumps(architecture)
            }
        ]
    )

    content = response.choices[0].message.content

    print(content)

    cleaned = content.strip()

    cleaned = cleaned.replace("```json", "")
    cleaned = cleaned.replace("```", "")

    return json.loads(cleaned)
