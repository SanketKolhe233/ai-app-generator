from groq import Groq
from dotenv import load_dotenv

import os
import json

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def repair_schema(errors, broken_schema):

    system_prompt = """
    You are a schema repair engine.

    Fix ONLY the broken parts.

    Return ONLY raw valid JSON.

    Do not explain anything.
    """

    repair_input = {
        "errors": errors,
        "broken_schema": broken_schema
    }

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
                "content": json.dumps(repair_input)
            }
        ]
    )

    content = response.choices[0].message.content

    cleaned = content.strip()

    cleaned = cleaned.replace("```json", "")
    cleaned = cleaned.replace("```", "")

    return json.loads(cleaned)
