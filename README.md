🏥 Hospital Management System (Flask + MySQL)
This is a simple Hospital Management System REST API built using Flask and MySQL.
It allows you to manage patients and doctors using CRUD (Create, Read, Update, Delete) operations.
__________________________________________________________________________________________________

🚀 Features
👤 Patient Management
•	Get all patients
•	Get patient by ID
•	Add a new patient
•	Update patient details
•	Delete a patient

👨‍⚕️ Doctor Management
•	Get all doctors
•	Add a new doctor
•	Update doctor details
•	Delete a doctor
__________________________________________________________________________________________________

🛠️ Tech Stack
•	Python
•	Flask
•	Flask-MySQLdb
•	MySQL
•	REST API (JSON)
__________________________________________________________________________________________________

📂 Project Structure
project/
│
├── app.py          # Main Flask application
├── README.md       # Project documentation
__________________________________________________________________________________________________

⚙️ Requirements
Make sure you have the following installed:
•	Python 3.x
•	MySQL Server
•	pip (Python package manager)
Python Packages
pip install flask flask-mysqldb
__________________________________________________________________________________________________

🗄️ Database Setup

1️⃣ Create Database
CREATE DATABASE hospital_db;
USE hospital_db;

2️⃣ Create patients Table
CREATE TABLE patients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    diagnosis VARCHAR(255),
    doctor VARCHAR(100)
);

3️⃣ Create doctors Table
CREATE TABLE doctors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    specialty VARCHAR(100)
);
__________________________________________________________________________________________________

🔧 Configuration
Update MySQL credentials in app.py:
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'hospital_db'
__________________________________________________________________________________________________

▶️ Run the Application
python app.py
Server will start at:
http://127.0.0.1:5000/
__________________________________________________________________________________________________

📌 API Endpoints
🏠 Home
GET /
__________________________________________________________________________________________________

👤 Patients API
Method	Endpoint	              Description
GET	    /patients/get	          Get all patients
GET	    /patient/get/<id>	      Get patient by ID
POST	  /patient/add	          Add new patient
PUT	    /patient/update/<id>	  Update patient
DELETE	/patient/del/<id>	      Delete patient

📥 Sample JSON (Add / Update Patient)
{
  "name": "Rahul Sharma",
  "age": 30,
  "gender": "Male",
  "diagnosis": "Fever",
  "doctor": "Dr. Mehta"
}
__________________________________________________________________________________________________

👨‍⚕️ Doctors API
Method	Endpoint	Description
GET	/doctors/get	Get all doctors
POST	/doctors/add	Add new doctor
PUT	/doctors/update/<id>	Update doctor
DELETE	/doctors/delete/<id>	Delete doctor
📥 Sample JSON (Add / Update Doctor)
{
  "name": "Dr. Mehta",
  "specialty": "Cardiology"
}
__________________________________________________________________________________________________

🧪 Testing Tools
You can test APIs using:
•	Postman
•	Thunder Client (VS Code)
•	curl
__________________________________________________________________________________________________

⚠️ Notes
•	Debug mode is enabled (debug=True) — disable it in production.
•	Add proper validation & error handling for production use.
•	Authentication is not implemented.
