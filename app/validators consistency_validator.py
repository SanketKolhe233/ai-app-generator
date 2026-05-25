def validate_consistency(schemas):
    
    errors = []

    db_schema = schemas.get("database_schema", {})
    api_schema = schemas.get("api_schema", {})
    ui_schema = schemas.get("ui_schema", {})
    auth_schema = schemas.get("auth_schema", {})

    # Validate API modules exist
    if not api_schema:
        errors.append("Missing API schema")

    # Validate DB tables exist
    if not db_schema:
        errors.append("Missing database schema")

    # Validate UI pages exist
    if not ui_schema:
        errors.append("Missing UI schema")

    # Validate auth exists
    if not auth_schema:
        errors.append("Missing auth schema")

    # Example consistency checks

    # Contacts page requires Contact table
    if "Contacts" in ui_schema:
        if "Contact" not in db_schema:
            errors.append(
                "Contacts UI exists but Contact table missing"
            )

    # Payments API requires Payment table
    if "Payments" in api_schema:
        if "Payment" not in db_schema:
            errors.append(
                "Payments API exists but Payment table missing"
            )

    return {
        "valid": len(errors) == 0,
        "errors": errors
    }
