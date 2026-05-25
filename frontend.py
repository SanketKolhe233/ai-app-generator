import streamlit as st

from app.generators.intent_extractor import extract_intent
from app.generators.system_designer import design_system
from app.generators.schema_generator import generate_schema

from app.validators.consistency_validator import validate_consistency


# ====================================
# PAGE TITLE
# ====================================

st.title("AI Application Generator")

st.markdown("""
### Compiler-Style AI Application Generator

Pipeline:

1. Intent Extraction  
2. System Design  
3. Schema Generation  
4. Validation + Repair  
5. Runtime Execution
""")


# ====================================
# USER INPUT
# ====================================

prompt = st.text_area(
    "Enter your app idea",
    placeholder="""
Build a CRM with:
- login
- contacts
- payments
- dashboard
- admin analytics
"""
)


# ====================================
# GENERATE BUTTON
# ====================================

if st.button("Generate"):

    with st.spinner("Generating application architecture..."):

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

    # ====================================
    # SUCCESS MESSAGE
    # ====================================

    st.success("Pipeline Execution Complete")


    # ====================================
    # DISPLAY OUTPUTS
    # ====================================

    st.subheader("Intent")

    st.json(intent)


    st.subheader("Architecture")

    st.json(architecture)


    st.subheader("Schemas")

    st.json(schemas)


    st.subheader("Validation")

    st.json(validation)


    # ====================================
    # METRICS
    # ====================================

    st.subheader("Metrics")

    st.json({
        "pipeline_stages": 4,
        "validation_passed": validation["valid"],
        "errors": validation["errors"]
    })