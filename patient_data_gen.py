import csv
import random

def generate_patient_data(num_patients):
    header = ["ID", "Age", "Gender", "Health Condition", "Hospital Location", "Preferred Doctor Type", "Last Appointment"]
    data = [header]

    for i in range(1, num_patients + 1):
        patient_id = random.randint(1000, 5000)
        age = random.randint(18, 90)
        gender = random.choice([1, 2])  # Representing numerical values for gender
        health_condition = random.randint(1,100)  # Numerical representation for health condition
        location_id = random.randint(900, 1000)
        preferred_doctor_type = random.randint(1, 100)  # Numerical representation for doctor type
        last_appointment = random.randint(1, 365)  # Representing days since the last appointment

        row = [patient_id, age, gender, health_condition, location_id, preferred_doctor_type, last_appointment]
        data.append(row)

    return data

def write_csv(data, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

if __name__ == "__main__":
    num_patients = 50000  # You can change this to the desired number of patients
    generated_data = generate_patient_data(num_patients)
    write_csv(generated_data, "patient_information.csv")
