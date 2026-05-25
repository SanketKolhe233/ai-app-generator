from app.generators.intent_extractor import extract_intent
from app.generators.system_designer import design_system
from app.generators.schema_generator import generate_schema

from app.validators.consistency_validator import validate_consistency

from evaluation.metrics import MetricsTracker
from evaluation.test_dataset import TEST_PROMPTS


metrics = MetricsTracker()


for i, prompt in enumerate(TEST_PROMPTS):

    print("\n========================")
    print(f"TEST CASE {i+1}")
    print("========================")

    print("\nPROMPT:")
    print(prompt)

    start_time = metrics.start_timer()

    try:

        # =========================
        # STAGE 1 — INTENT
        # =========================

        intent = extract_intent(prompt)

        # =========================
        # STAGE 2 — ARCHITECTURE
        # =========================

        architecture = design_system(intent)

        # =========================
        # STAGE 3 — SCHEMA GENERATION
        # =========================

        schemas = generate_schema(architecture)

        # =========================
        # STAGE 4 — VALIDATION
        # =========================

        validation = validate_consistency(
            schemas
        )

        latency = metrics.end_timer(
            start_time
        )

        if validation["valid"]:

            metrics.record_success()

            print("\nSTATUS: SUCCESS")

        else:

            metrics.record_failure(
                validation["errors"]
            )

            print("\nSTATUS: FAILED")

            print(validation["errors"])


    except Exception as e:

        metrics.record_failure(str(e))

        print("\nEXCEPTION:")
        print(e)


print("\n========================")
print("FINAL METRICS")
print("========================")

print(metrics.get_metrics())