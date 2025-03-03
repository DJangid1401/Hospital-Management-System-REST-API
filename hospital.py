from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

# Flask app initialize karte hain
app = Flask(__name__)

# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'  # MySQL server ka host
app.config['MYSQL_USER'] = 'root'  # MySQL username
app.config['MYSQL_PASSWORD'] = 'root'  # MySQL password (default empty)
app.config['MYSQL_DB'] = 'hospital_db'  # Humari hospital database ka naam

# MySQL object banate hain
mysql = MySQL(app)

# Home route - Basic welcome message
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Hospital Management System!"})

# API to get all patients
@app.route('/patients/get', methods=['GET'])
def get_patients():
    # SQL query likhte hain saare patients ko fetch karne ke liye
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM patients")
    
    # Result fetch karte hain
    patients = cur.fetchall()
    
    # Result ko list mein convert karte hain
    patient_list = []
    for patient in patients:
        patient_list.append({
            'id': patient[0],
            'name': patient[1],
            'age': patient[2],
            'gender': patient[3],
            'diagnosis': patient[4],
            'doctor': patient[5]
        })
    
    # Return patients ka data
    return jsonify({"patients": patient_list})

# API to get a specific patient by id
@app.route('/patient/get/<int:id>', methods=['GET'])
def get_patient(id):
    # SQL query likhte hain ek specific patient ka data lene ke liye
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM patients WHERE id = %s", (id,))
    
    # Result fetch karte hain
    patient = cur.fetchone()
    
    if patient:
        return jsonify({
            'id': patient[0],
            'name': patient[1],
            'age': patient[2],
            'gender': patient[3],
            'diagnosis': patient[4],
            'doctor': patient[5]
        })
    else:
        # Agar patient nahi mila to error message return karenge
        return jsonify({"message": "Patient not found"}), 404

# API to add a new patient
@app.route('/patient/add', methods=['POST'])
def add_patient():
    # Request se patient ki details lete hain (JSON format mein)
    patient_data = request.get_json()
    
    # SQL query likhte hain naye patient ko insert karne ke liye
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO patients (name, age, gender, diagnosis, doctor) VALUES (%s, %s, %s, %s, %s)",
                (patient_data['name'], patient_data['age'], patient_data['gender'], patient_data['diagnosis'], patient_data['doctor']))
    
    # Changes commit karte hain
    mysql.connection.commit()
    
    # Naye patient ka data return karte hain
    return jsonify({"message": "Patient added successfully", "patient": patient_data}), 201

# API to update a patient's information
@app.route('/patient/update/<int:id>', methods=['PUT'])
def update_patient(id):
    # Patient ki details update karne ke liye, request se data lete hain
    patient_data = request.get_json()
    
    # SQL query likhte hain patient ko update karne ke liye
    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE patients SET name = %s, age = %s, gender = %s, diagnosis = %s, doctor = %s WHERE id = %s
    """, (patient_data['name'], patient_data['age'], patient_data['gender'], patient_data['diagnosis'], patient_data['doctor'], id))
    
    # Changes commit karte hain
    mysql.connection.commit()
    
    # Patient ki updated details return karte hain
    return jsonify({"message": "Patient updated successfully", "patient": patient_data})

# API to delete a patient
@app.route('/patient/del/<int:id>', methods=['DELETE'])
def delete_patient(id):
    # SQL query likhte hain patient ko delete karne ke liye
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM patients WHERE id = %s", (id,))
    
    # Changes commit karte hain
    mysql.connection.commit()
    
    # Success message return karte hain
    return jsonify({"message": "Patient deleted successfully"})

# API to get all doctors
@app.route('/doctors/get', methods=['GET'])
def get_doctors():
    # Doctors ka data fetch karte hain
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM doctors")
    
    # Result fetch karte hain
    doctors = cur.fetchall()
    
    # Doctors ke details list mein convert karte hain
    doctor_list = []
    for doctor in doctors:
        doctor_list.append({
            'id': doctor[0],
            'name': doctor[1],
            'specialty': doctor[2]
        })
    
    return jsonify({"doctors": doctor_list})

# POST request to add a new doctor
@app.route('/doctors/add', methods=['POST'])
def add_doctor():
    data = request.get_json()
    name = data['name']
    specialty = data['specialty']
    
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO doctors (name, specialty) VALUES (%s, %s)", (name, specialty))
    mysql.connection.commit()
    cur.close()
    
    return jsonify({"message": "Doctor added successfully!"}), 201

# PUT request to update an existing doctor's details
@app.route('/doctors/update/<int:doctor_id>', methods=['PUT'])
def update_doctor(doctor_id):
    data = request.get_json()
    name = data['name']
    specialty = data['specialty']
    
    cur = mysql.connection.cursor()
    cur.execute("UPDATE doctors SET name = %s, specialty = %s WHERE id = %s", (name, specialty, doctor_id))
    mysql.connection.commit()
    cur.close()
    
    return jsonify({"message": "Doctor updated successfully!"})

# DELETE request to remove a doctor by id
@app.route('/doctors/delete/<int:doctor_id>', methods=['DELETE'])
def delete_doctor(doctor_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM doctors WHERE id = %s", (doctor_id,))
    mysql.connection.commit()
    cur.close()
    
    return jsonify({"message": "Doctor deleted successfully!"})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
