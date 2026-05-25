from app.generators.intent_extractor import extract_intent
from app.generators.system_designer import design_system
from app.generators.schema_generator import generate_schema

from app.runtime.api_runtime import create_routes

import uvicorn

prompt = """
Build a CRM with login, contacts, dashboard,
role-based access, and payments.
"""

# Pipeline
intent = extract_intent(prompt)

architecture = design_system(intent)

schemas = generate_schema(architecture)

# Create APIs dynamically
app = create_routes(
    schemas["api_schema"]
)

# Run server
if __name__ == "__main__":

    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000
    )
