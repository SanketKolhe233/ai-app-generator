def validate_schema_structure(schemas):

    errors = []

    # =========================
    # REQUIRED TOP-LEVEL KEYS
    # =========================

    required_keys = [
        "database_schema",
        "api_schema",
        "ui_schema",
        "auth_schema"
    ]

    for key in required_keys:

        if key not in schemas:

            errors.append(
                f"Missing top-level schema: {key}"
            )

    # =========================
    # DATABASE VALIDATION
    # =========================

    database_schema = schemas.get(
        "database_schema",
        {}
    )

    if not isinstance(database_schema, dict):

        errors.append(
            "database_schema must be a dictionary"
        )

    # =========================
    # API VALIDATION
    # =========================

    api_schema = schemas.get(
        "api_schema",
        {}
    )

    if not isinstance(api_schema, dict):

        errors.append(
            "api_schema must be a dictionary"
        )

    # =========================
    # UI VALIDATION
    # =========================

    ui_schema = schemas.get(
        "ui_schema",
        {}
    )

    if not isinstance(ui_schema, dict):

        errors.append(
            "ui_schema must be a dictionary"
        )

    # =========================
    # AUTH VALIDATION
    # =========================

    auth_schema = schemas.get(
        "auth_schema",
        {}
    )

    if not isinstance(auth_schema, dict):

        errors.append(
            "auth_schema must be a dictionary"
        )

    # =========================
    # EMPTY SCHEMA CHECKS
    # =========================

    if not database_schema:

        errors.append(
            "database_schema is empty"
        )

    if not api_schema:

        errors.append(
            "api_schema is empty"
        )

    if not ui_schema:

        errors.append(
            "ui_schema is empty"
        )

    if not auth_schema:

        errors.append(
            "auth_schema is empty"
        )

    # =========================
    # FINAL RESULT
    # =========================

    return {

        "valid": len(errors) == 0,

        "errors": errors
    }
