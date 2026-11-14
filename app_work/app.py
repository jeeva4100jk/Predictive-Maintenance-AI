import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# Load the saved Random Forest model
project_folder = Path(__file__).resolve().parent.parent
model_path = project_folder / "models" / "random_forest_model.pkl"

@st.cache_resource
def load_model():
    return joblib.load(model_path)

model = load_model()

st.title("Predictive Maintenance AI")
st.write("Machine Failure Prediction System")

st.success("Random Forest Model Loaded Successfully!")

# Store prediction history
if "prediction_history" not in st.session_state:
    st.session_state.prediction_history = []

st.subheader("Enter Machine Details")

machine_type = st.selectbox(
    "Machine Type",
    ["L", "M", "H"]
)

air_temp = st.number_input(
    "Air Temperature [K]",
    value=300.0
)

process_temp = st.number_input(
    "Process Temperature [K]",
    value=310.0
)

rot_speed = st.number_input(
    "Rotational Speed [rpm]",
    value=1500,
    step=10
)

torque = st.number_input(
    "Torque [Nm]",
     min_value=0,
    max_value=100,
    value=40,
    step=1
)

tool_wear = st.number_input(
    "Tool Wear [min]",
    value=100,
    step=5
)

if st.button("Predict Machine Failure"):

    # Get the exact feature names used during model training
    if not hasattr(model, "feature_names_in_"):
        st.error("Model feature information is unavailable.")
    else:
        features = list(model.feature_names_in_)

        input_values = {
            "Air temperature [K]": air_temp,
            "Process temperature [K]": process_temp,
            "Air temperature [C]": air_temp - 273.15,
            "Process temperature [C]": process_temp - 273.15,
            "Rotational speed [rpm]": rot_speed,
            "Torque [Nm]": torque,
            "Tool wear [min]": tool_wear,
            "Type_L": 1 if machine_type == "L" else 0,
            "Type_M": 1 if machine_type == "M" else 0,
            "Type_H": 1 if machine_type == "H" else 0
        }

        missing_features = [
            feature for feature in features
            if feature not in input_values
        ]

        if missing_features:
            st.error(
                f"Please check model features: {missing_features}"
            )
        else:
            input_data = pd.DataFrame(
                [[input_values[feature] for feature in features]],
                columns=features
            )

            prediction = model.predict(input_data)

        failure_probability = (
            model.predict_proba(input_data)[0][
                list(model.classes_).index(1)
            ] * 100
        )
        
        if prediction[0] == 1:
            result = "Machine Failure Predicted!"
            st.error(result)
        else:
            result = "No Machine Failure Predicted!"
            st.success(result)
        
        st.metric(
            "Machine Failure Risk",
            f"{failure_probability:.2f}%"
        )
        
        # Save prediction in history
        st.session_state.prediction_history.append({
            "Machine Type": machine_type,
            "Torque": torque,
            "Tool Wear": tool_wear,
            "Prediction": result,
            "Failure Risk (%)": round(failure_probability, 2)
        })

        # Display Prediction History
        st.subheader("Prediction History")
        
        if st.session_state.prediction_history:
            history_df = pd.DataFrame(
                st.session_state.prediction_history
            )
        
            st.dataframe(history_df, use_container_width=True)
        
        else:
            st.info("No prediction history available yet.")