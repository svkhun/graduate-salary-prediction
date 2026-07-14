from pathlib import Path

import joblib
import pandas as pd
import streamlit as st


MODEL_PATH = Path(__file__).with_name("model.pkl")
RAW_FEATURES = [
    "aptitude_score",
    "coding_skill_score",
    "communication_skill_score",
    "logical_reasoning_score",
]


@st.cache_resource
def load_model():
    """Load the model once per Streamlit server session."""
    return joblib.load(MODEL_PATH)


def build_features(
    aptitude_score: float,
    coding_skill_score: float,
    communication_skill_score: float,
    logical_reasoning_score: float,
) -> pd.DataFrame:
    """Create the six features expected by the saved model."""
    scores = {
        "aptitude_score": aptitude_score,
        "coding_skill_score": coding_skill_score,
        "communication_skill_score": communication_skill_score,
        "logical_reasoning_score": logical_reasoning_score,
    }
    total_skill = sum(scores.values())
    scores["total_skill"] = total_skill
    scores["avg_skill"] = total_skill / len(RAW_FEATURES)
    return pd.DataFrame([scores])


st.set_page_config(page_title="Graduate Salary Prediction", layout="centered")
st.title("Graduate Salary Prediction")
st.caption("Research prototype for estimating an entry-level salary from four skill scores.")

with st.form("prediction_form"):
    left_column, right_column = st.columns(2)

    with left_column:
        aptitude_score = st.number_input(
            "Aptitude score", min_value=0.0, max_value=100.0, value=0.0, step=0.1
        )
        coding_skill_score = st.number_input(
            "Coding skill score", min_value=0.0, max_value=100.0, value=0.0, step=0.1
        )

    with right_column:
        communication_skill_score = st.number_input(
            "Communication skill score", min_value=0.0, max_value=100.0, value=0.0, step=0.1
        )
        logical_reasoning_score = st.number_input(
            "Logical reasoning score", min_value=0.0, max_value=100.0, value=0.0, step=0.1
        )

    submitted = st.form_submit_button("Predict salary")

if submitted:
    try:
        model = load_model()
        prediction = float(
            model.predict(
                build_features(
                    aptitude_score,
                    coding_skill_score,
                    communication_skill_score,
                    logical_reasoning_score,
                )
            )[0]
        )
        st.success(f"Estimated salary: {prediction:.2f} LPA")
        st.caption("LPA is the unit used by the training dataset; it is not a Thai-baht estimate.")
    except FileNotFoundError:
        st.error("model.pkl was not found. Keep it in the same folder as app.py.")
    except Exception as error:
        st.error(f"The prediction could not be generated: {error}")

st.warning(
    "This is a research prototype. Predictions are estimates only and may be inaccurate. "
    "Actual starting salaries depend on factors not represented in this model, including the job role, "
    "location, labour market, experience, skills, and employer. Do not use this result as a salary guarantee "
    "or as the sole basis for a decision. The model requires further development and evaluation."
)
