from fastapi import FastAPI

app = FastAPI()

def create_routes(api_schema):

    # Auth APIs
    if "Auth" in api_schema:

        @app.post("/login")
        def login():
            return {
                "message": "Login API working"
            }

        @app.post("/register")
        def register():
            return {
                "message": "Register API working"
            }

    # Contacts APIs
    if "Contacts" in api_schema:

        @app.get("/contacts")
        def get_contacts():
            return {
                "contacts": []
            }

    # Payments APIs
    if "Payments" in api_schema:

        @app.get("/payments")
        def get_payments():
            return {
                "payments": []
            }

    return app
