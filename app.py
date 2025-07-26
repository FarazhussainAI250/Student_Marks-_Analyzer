import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set dark theme for chart
plt.style.use('dark_background')

# Page config
st.set_page_config(page_title="Student Marks Analyzer", layout="centered")

# Title
st.title("📘 Student Marks Analyzer")
st.subheader("📝 Enter Student Details")

# Inputs
name = st.text_input("Student Name")
math = st.number_input("Math Marks", 0, 150, step=1)
science = st.number_input("Science Marks", 0, 150, step=1)
english = st.number_input("English Marks", 0, 150, step=1)
urdu = st.number_input("Urdu Marks", 0, 150, step=1)
islamicstudies = st.number_input("Islamic Studies Marks", 0, 150, step=1)
education = st.number_input("Education Marks", 0, 150, step=1)
islamiyat = st.number_input("Islamiyat Marks", 0, 100, step=1)

# Analyze
if st.button("🔍 Analyze Result"):
    total = math + science + english + urdu + islamicstudies + education + islamiyat
    percentage = round((total / 1000) * 100, 2)

    if percentage >= 80:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 40:
        grade = "C"
    else:
        grade = "F"

    st.markdown("---")
    st.subheader(f"🎓 Result for: {name}")

    st.subheader("✅ Obtained Marks")
    st.write(f"**Total Marks Obtained:** {total} / 1000")

    st.subheader("📈 Percentage")
    st.success(f"Your Percentage is: **{percentage}%**")

    st.subheader("🏅 Grade")
    st.info(f"Grade: **{grade}**")

    st.markdown("---")
    st.subheader("📊 Subject-wise Marks Chart")

    df = pd.DataFrame({
        "Subjects": ["Math", "Science", "English", "Urdu", "Islamic Studies", "Education", "Islamiyat"],
        "Marks": [math, science, english, urdu, islamicstudies, education, islamiyat]
    })

    fig, ax = plt.subplots(figsize=(10, 6), dpi=100)
    bars = ax.bar(df["Subjects"], df["Marks"], color='#1f77b4', edgecolor='white')

    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval + 2, f'{int(yval)}',
                ha='center', va='bottom', fontsize=9, color='white')

    ax.set_ylabel("Marks", fontsize=12, color='white')
    ax.set_xlabel("Subjects", fontsize=12, color='white')
    ax.set_title("Subject-wise Marks", fontsize=14, color='white')
    ax.tick_params(axis='x', labelrotation=30, labelsize=10, colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.set_ylim(0, max(df["Marks"]) + 20)

    ax.set_facecolor("#222222")
    fig.patch.set_facecolor("#111111")
    ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.3)

    plt.tight_layout()
    st.pyplot(fig)
