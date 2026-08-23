from pathlib import Path

import joblib
import pandas as pd
import streamlit as st


# -----------------------------
# Paths
# -----------------------------
APP_DIR = Path(__file__).resolve().parent
MODEL_PATH = APP_DIR / "flight_delay_model.joblib"
OPTIONS_PATH = APP_DIR / "app_options.joblib"
OVERVIEW_PATH = APP_DIR / "overview.csv"
AIRLINE_PATH = APP_DIR / "airline_summary.csv"
MONTHLY_PATH = APP_DIR / "monthly_summary.csv"


# -----------------------------
# Load saved project files
# -----------------------------
@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


@st.cache_data
def load_options():
    return joblib.load(OPTIONS_PATH)


@st.cache_data
def load_summary_files():
    overview = pd.read_csv(OVERVIEW_PATH)
    airline_summary = pd.read_csv(AIRLINE_PATH)
    monthly_summary = pd.read_csv(MONTHLY_PATH)

    return overview, airline_summary, monthly_summary


model = load_model()
options = load_options()
overview, airline_summary, monthly_summary = load_summary_files()


# -----------------------------
# Page settings
# -----------------------------
st.set_page_config(
    page_title="Flight Delay Analysis",
    page_icon="✈️",
    layout="wide",
)


# -----------------------------
# Header
# -----------------------------
st.title("✈️ Flight Delay Analysis & Prediction")

st.write(
    "Explore flight delay patterns and estimate the probability "
    "of an arrival delay of 15 minutes or more."
)

st.divider()


# -----------------------------
# Overview metrics
# -----------------------------
metrics = {
    row["Metric"]: row["Value"]
    for _, row in overview.iterrows()
}

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Flights Analysed",
    f"{int(metrics['Total Flights']):,}"
)

col2.metric(
    "Delayed Flights",
    f"{int(metrics['Delayed Flights']):,}"
)

col3.metric(
    "Delay Rate",
    f"{metrics['Delay Rate']:.2f}%"
)

col4.metric(
    "Avg Arrival Delay",
    f"{metrics['Average Arrival Delay']:.1f} min"
)


# -----------------------------
# Analysis
# -----------------------------
st.header("Flight Delay Patterns")

tab1, tab2 = st.tabs(
    ["Airline Analysis", "Monthly Analysis"]
)


with tab1:
    chart_data = airline_summary.set_index("Airline")["Delay_Rate"]

    st.subheader("Delay Rate by Airline")
    st.bar_chart(chart_data)

    st.dataframe(
        airline_summary.sort_values(
            "Delay_Rate",
            ascending=False
        ),
        use_container_width=True,
        hide_index=True,
    )


with tab2:
    monthly_chart = monthly_summary.set_index("Month")["Delay_Rate"]

    st.subheader("Monthly Delay Rate")
    st.line_chart(monthly_chart)

    st.dataframe(
        monthly_summary,
        use_container_width=True,
        hide_index=True,
    )


# -----------------------------
# Prediction section
# -----------------------------
st.divider()

st.header("✈️ Flight Delay Risk Prediction")

st.write(
    "Enter scheduled flight information to estimate the "
    "probability of an arrival delay."
)

col1, col2 = st.columns(2)

with col1:

    airline = st.selectbox(
        "Airline",
        options["airlines"]
    )

    origin = st.selectbox(
        "Origin Airport",
        options["origins"]
    )

    destination = st.selectbox(
        "Destination Airport",
        options["destinations"]
    )

    distance = st.number_input(
        "Distance (miles)",
        min_value=1.0,
        value=500.0,
        step=10.0
    )

    month = st.slider(
        "Month",
        min_value=1,
        max_value=12,
        value=6
    )

with col2:

    day_of_week = st.slider(
        "Day of Week",
        min_value=0,
        max_value=6,
        value=2,
        help="0 = Monday, 6 = Sunday"
    )

    dep_hour = st.slider(
        "Scheduled Departure Hour",
        min_value=0,
        max_value=23,
        value=10
    )

    arr_hour = st.slider(
        "Scheduled Arrival Hour",
        min_value=0,
        max_value=23,
        value=12
    )

    scheduled_duration = st.number_input(
        "Scheduled Duration (minutes)",
        min_value=1,
        value=120,
        step=5
    )


# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict Delay Risk", type="primary"):

    input_data = pd.DataFrame({
        "Airline": [airline],
        "Origin": [origin],
        "Dest": [destination],
        "CRSDepTime": [dep_hour * 100],
        "CRSArrTime": [arr_hour * 100],
        "Distance": [distance],
        "Month": [month],
        "DayOfWeek": [day_of_week],
        "DepHour": [dep_hour],
        "ArrHour": [arr_hour],
        "ScheduledDuration": [scheduled_duration]
    })

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0, 1]

    st.divider()

    if prediction == 1:
        st.warning(
            f"Estimated delay probability: {probability:.1%}"
        )
        st.error(
            "The model predicts that the flight is likely "
            "to arrive 15 minutes or more late."
        )
    else:
        st.success(
            f"Estimated delay probability: {probability:.1%}"
        )
        st.success(
            "The model predicts a lower likelihood of a "
            "15-minute-or-more arrival delay."
        )


# -----------------------------
# Footer
# -----------------------------
st.divider()

st.caption(
    "Flight Delay Analysis & Prediction | "
    "Data analytics project"
)
