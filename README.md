# Employee-Salary-Prediction

This is a user-friendly Streamlit web application that predicts the annual salary of an employee based on input features like company, job title, education, experience, and location. The prediction is powered by a pre-trained machine learning model.

🚀 Demo

(Replace this with a real screenshot or GIF of your app in action)

📦 Features
🔮 Predicts salary based on real-world features

📋 User-friendly interface with dropdowns and tooltips

✅ Handles missing input columns and errors gracefully

🧠 Integrates with a machine learning model trained on real data

💬 Clear instructions via sidebar

🧰 Technologies Used
Python

Streamlit – for the interactive web UI

Pandas – for data manipulation

Joblib – to load the trained model

Scikit-learn (used during model training)

📂 Project Structure
bash
Copy
Edit
salary_predictor/
├── best_model.pkl           # Trained regression model (Joblib format)
├── input_columns.pkl        # Columns used for training (to match input features)
├── app.py                   # Streamlit application code
├── README.md                # Project documentation
🛠️ Setup Instructions
Clone the repository

bash
Copy
Edit
git clone https://github.com/yourusername/salary-predictor.git
cd salary-predictor
Install dependencies

Make sure you have Python 3.7+ installed.

bash
Copy
Edit
pip install -r requirements.txt
If requirements.txt is missing, install manually:

bash
Copy
Edit
pip install streamlit pandas scikit-learn joblib
Add the model files

Make sure the following files are in the root directory:

best_model.pkl

input_columns.pkl

⚠️ These files must match the format used during training (especially the one-hot encoded column order).

Run the app

bash
Copy
Edit
streamlit run app.py
Visit in browser

It should automatically open in your default browser at
http://localhost:8501

🧠 Model Assumptions
Model is trained using categorical encoding (one-hot) for:

Company

Education Level

Location

Job Title

Feature Years of Experience is numerical

Model output is in INR (₹)

📈 Example Inputs
Feature	Example Value
Company	Google
Job Title	Data Scientist
Education Level	Master
Location	Bangalore
Years of Experience	3

📌 To-Do / Future Enhancements
 Add charts to compare predicted vs average salaries

 Upload resume to auto-fill inputs

 Train model on a larger real-world dataset

 Export prediction as PDF or downloadable file

🤝 Contributing
Feel free to open issues or submit pull requests if you'd like to improve this project!

