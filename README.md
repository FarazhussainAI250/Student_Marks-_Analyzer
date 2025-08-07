
# 📘 Student Marks Analyzer

A simple and interactive Streamlit web application that allows users to input student marks across multiple subjects and get a visual and statistical analysis of the student's performance.

## 🚀 Features

- Input marks for subjects like Math, Science, English, Urdu, Islamic Studies, Education, and Islamiyat
- Calculates total marks, percentage, and assigns grade based on performance
- Displays subject-wise bar chart using Matplotlib with dark theme
- Fully interactive and responsive web interface built using Streamlit

## 📁 Project Structure

```
📦 Student_Marks-_Analyzer
├── app.py               # Streamlit application
├── Requirement.txt      # Required dependencies
```

## 💻 Getting Started

### 🔧 1. Clone the Repository

```bash
git clone https://github.com/FarazhussainAI250/Student_Marks-_Analyzer.git
cd Student_Marks-_Analyzer
```

### 📦 2. Install Dependencies

```bash
pip install -r Requirement.txt
```

### ▶️ 3. Run the Streamlit App

```bash
streamlit run app.py
```

The app will open in your default browser (usually at `http://localhost:8501/`).

## 🧮 How It Works

1. User inputs student name and marks in each subject.
2. App calculates:
   - **Total Marks (out of 1000)**
   - **Percentage**
   - **Grade (A, B, C, F based on percentage)**
3. Displays a clean bar chart of marks across subjects using Matplotlib.

## 🛠️ Future Improvements

- Add export to PDF/Excel functionality
- Add support for uploading marks via CSV file
- Store historical results

## 🧾 License

This project is open-source and available under the MIT License.

## 🙋 Contact

For queries or collaborations:  
**Faraz Hussain**  
GitHub: [@FarazhussainAI250](https://github.com/FarazhussainAI250)
