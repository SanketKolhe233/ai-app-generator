from groq import Groq
from dotenv import load_dotenv

import os
import json

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def design_system(intent_data):

    system_prompt = """
    You are a software architecture generator.

    Return ONLY raw valid JSON.

    DO NOT:
    - use markdown
    - explain anything
    - add extra text

    Required format:

    {
      "entities": [],
      "pages": [],
      "api_modules": [],
      "permissions": {}
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
                "content": json.dumps(intent_data)
            }
        ]
    )

    content = response.choices[0].message.content

    print(content)

    cleaned = content.strip()

    cleaned = cleaned.replace("```json", "")
    cleaned = cleaned.replace("```", "")

    return json.loads(cleaned)
