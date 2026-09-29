import streamlit as st
import pickle
import pandas as pd

# -----------------------------
# Load trained model
# -----------------------------
with open("student_model.pkl", "rb") as file:
    model = pickle.load(file)

# -----------------------------
# Page settings
# -----------------------------
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="centered"
)

# -----------------------------
# Header
# -----------------------------
st.title("🎓 Student Performance Predictor")
st.write(
    "Enter your academic details to predict your performance "
    "and get personalized study recommendations."
)

st.divider()

# -----------------------------
# Student Inputs
# -----------------------------
st.subheader("📋 Enter Student Details")

col1, col2 = st.columns(2)

with col1:
    study_hours = st.number_input(
        "📚 Study Hours Per Day",
        min_value=0.0,
        max_value=24.0,
        value=3.0,
        step=0.5
    )

    attendance = st.number_input(
        "📅 Attendance Percentage",
        min_value=0,
        max_value=100,
        value=75
    )

    previous_score = st.number_input(
        "📊 Previous Year Score",
        min_value=0,
        max_value=100,
        value=60
    )

with col2:
    math_score = st.number_input(
        "➗ Math Score",
        min_value=0,
        max_value=100,
        value=60
    )

    science_score = st.number_input(
        "🔬 Science Score",
        min_value=0,
        max_value=100,
        value=60
    )

    english_score = st.number_input(
        "📖 English Score",
        min_value=0,
        max_value=100,
        value=60
    )

st.divider()

# -----------------------------
# Prediction
# -----------------------------
if st.button("🔮 Predict Performance", use_container_width=True):

    input_data = pd.DataFrame({
        "Study_Hours_Per_Day": [study_hours],
        "Attendance_Percentage": [attendance],
        "Previous_Year_Score": [previous_score],
        "Math_Score": [math_score],
        "Science_Score": [science_score],
        "English_Score": [english_score]
    })

    prediction = model.predict(input_data)[0]

    # Probability
    probabilities = model.predict_proba(input_data)[0]
    classes = model.classes_

    pass_probability = 0
    fail_probability = 0

    for class_name, probability in zip(classes, probabilities):
        if class_name == "Pass":
            pass_probability = probability * 100
        elif class_name == "Fail":
            fail_probability = probability * 100

    # -----------------------------
    # Result
    # -----------------------------
    st.divider()
    st.subheader("🎯 Prediction Result")

    if prediction == "Pass":
        st.success("🎉 Prediction: PASS")
        st.write(
            f"Based on the entered information, the model predicts that "
            f"the student will **Pass**."
        )
    else:
        st.error("⚠️ Prediction: FAIL")
        st.write(
            "The model predicts that the student may need additional "
            "academic preparation."
        )

    # -----------------------------
    # Probability
    # -----------------------------
    st.subheader("📈 Prediction Probability")

    c1, c2 = st.columns(2)

    with c1:
        st.metric("Pass Probability", f"{pass_probability:.1f}%")

    with c2:
        st.metric("Fail Probability", f"{fail_probability:.1f}%")

    # -----------------------------
    # Find weakest subject
    # -----------------------------
    subjects = {
        "Math": math_score,
        "Science": science_score,
        "English": english_score
    }

    weakest_subject = min(subjects, key=subjects.get)
    weakest_score = subjects[weakest_subject]

    st.divider()

    # -----------------------------
    # Personalized Study Advice
    # -----------------------------
    st.subheader("📚 Personalized Study Recommendation")

    st.info(
        f"Your lowest score is in **{weakest_subject} ({weakest_score}/100)**. "
        f"Give extra attention to this subject."
    )

    if weakest_score < 50:
        st.warning(
            f"⚠️ Your {weakest_subject} score is below 50. "
            f"Focus strongly on basic concepts and regular practice."
        )

    elif weakest_score < 70:
        st.warning(
            f"📖 Your {weakest_subject} score can be improved. "
            f"Practice this subject regularly and revise difficult topics."
        )

    else:
        st.success(
            f"👍 Your {weakest_subject} score is relatively good. "
            f"Continue practicing to maintain your performance."
        )

    # -----------------------------
    # General instructions
    # -----------------------------
    st.subheader("💡 Study Instructions")

    if study_hours < 2:
        st.write("• Try to increase your daily study time gradually.")

    if attendance < 75:
        st.write("• Try to improve your class attendance and attend lessons regularly.")

    if previous_score < 50:
        st.write("• Revise previous concepts before starting advanced topics.")

    st.write("• Practice questions regularly instead of only reading theory.")
    st.write("• Revise difficult topics every week.")
    st.write("• Give extra time to your weakest subject.")
    st.write("• Take short breaks during long study sessions.")

    # -----------------------------
    # Learning Resources
    # -----------------------------
    st.subheader("🎥 Learning Resources")

    if weakest_subject == "Math":
        st.write("### ➗ Mathematics")
        st.link_button(
            "🎓 Learn Mathematics - Khan Academy",
            "https://www.khanacademy.org/math"
        )

    elif weakest_subject == "Science":
        st.write("### 🔬 Science")
        st.link_button(
            "🎓 Learn Science - Khan Academy",
            "https://www.khanacademy.org/science"
        )

    elif weakest_subject == "English":
        st.write("### 📖 English")
        st.link_button(
            "🎓 Learn English - Khan Academy",
            "https://www.khanacademy.org/humanities/grammar"
        )

    st.divider()

    st.caption(
        "Note: This prediction is generated by a machine-learning model "
        "and should be used as an academic guidance tool."
    )