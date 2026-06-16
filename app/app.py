import streamlit as st
import joblib

# Load trained model

model = joblib.load('models/xgb_model.pkl')


# Title

st.title("Intern Performance Prediction System")

# Description

st.write(
    "Predict intern performance using an XGBoost Machine Learning model."
)

st.write(
    "Enter intern details below and click Predict."
)

# Input fields

completion_time = st.number_input(

    "Completion Time (Hours)",

    min_value=0.0,

    max_value=100.0,

    value=5.0
)

feedback_rating = st.number_input(

    "Feedback Rating",

    min_value=1.0,

    max_value=5.0,

    value=4.0,

    step=0.1
)

attendance = st.number_input(

    "Attendance (%)",

    min_value=0.0,

    max_value=100.0,

    value=90.0
)


# Predict Button

if st.button("Predict Performance"):


    # Predict score

    prediction = model.predict([

        [

            completion_time,

            feedback_rating,

            attendance

        ]

    ])

    score = prediction[0]

    # Show Score

    st.metric(

        "Predicted Performance Score",

        round(score, 2)

    )

    # Show Category

    if score <= 50:

        st.error(

            "Struggling Intern"

        )

    elif score <= 75:

        st.warning(

            "Average Intern"

        )

    else:

        st.success(

            "Excellent Intern"

        )