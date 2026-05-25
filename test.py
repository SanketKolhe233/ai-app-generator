from app.generators.intent_extractor import extract_intent
from app.generators.system_designer import design_system
from app.generators.schema_generator import generate_schema

from app.validators.consistency_validator import validate_consistency

from app.generators.repair_engine import repair_schema

from evaluation.metrics import MetricsTracker


# =========================
# METRICS
# =========================

metrics = MetricsTracker()


# =========================
# USER PROMPT
# =========================

prompt = """
Build a CRM with login, contacts, dashboard,
role-based access, and payments.
"""


# =========================
# START TIMER
# =========================

start_time = metrics.start_timer()


# =========================
# STAGE 1 — INTENT
# =========================

intent = extract_intent(prompt)

print("\n===== INTENT =====")
print(intent)


# =========================
# STAGE 2 — ARCHITECTURE
# =========================

architecture = design_system(intent)

print("\n===== ARCHITECTURE =====")
print(architecture)


# =========================
# STAGE 3 — SCHEMA GENERATION
# =========================

schemas = generate_schema(architecture)

print("\n===== SCHEMAS =====")
print(schemas)


# =========================
# STAGE 4 — VALIDATION
# =========================

validation = validate_consistency(schemas)

print("\n===== VALIDATION =====")
print(validation)


# =========================
# STAGE 5 — REPAIR
# =========================

if not validation["valid"]:

    repaired = repair_schema(
        validation["errors"],
        schemas
    )

    metrics.record_repair()

    print("\n===== REPAIRED SCHEMA =====")
    print(repaired)

else:

    print("\nNo repair needed.")


# =========================
# METRICS RECORDING
# =========================

latency = metrics.end_timer(start_time)

if validation["valid"]:

    metrics.record_success()

else:

    metrics.record_failure(
        validation["errors"]
    )


# =========================
# FINAL METRICS
# =========================

print("\n===== METRICS =====")
print(metrics.get_metrics())