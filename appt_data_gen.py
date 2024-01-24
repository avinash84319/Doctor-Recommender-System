import csv
import random

def calculate_rating(age_difference):
    # Function to calculate a sensible rating based on age difference
    return random.randint(2,4) if age_difference < 10 else random.randint(4, 10)

def generate_fake_appointments(num_appointments, doctor_data, patient_data):
    header = ["AppointmentID", "PatientID", "DoctorID", "AppointmentDate", "Rating"]
    data = [header]

    for i in range(1, num_appointments + 1):
        appointment_id = i
        patient_id = random.choice(patient_data[1:])[0]  # Randomly select a patient ID from the patient dataset
        eligible_patients = [patient for patient in patient_data[1:] if patient[0] != patient_id]

        if not eligible_patients:
            print(f"No eligible patients found for appointment {i}. Skipping appointment.")
            continue

        patient_data.remove(eligible_patients[0])  # Remove the selected patient from the patient dataset

        # Find a doctor with matching location and type preferences
        eligible_doctors = [doctor for doctor in doctor_data[1:] if doctor[4] == eligible_patients[0][4] and doctor[2] == eligible_patients[0][6]]
        
        if not eligible_doctors:
            print(f"No eligible doctors found for patient {i}. Skipping appointment.")
            continue

        doctor_id = random.choice(eligible_doctors)[0]
        doctor_age = int(eligible_doctors[0][1])
        patient_age = int(eligible_patients[0][2])
        age_difference = abs(doctor_age - patient_age)

        appointment_date = random.randint(1, 365)  # Representing days from now
        rating = calculate_rating(age_difference)

        row = [appointment_id, patient_id, doctor_id, appointment_date, rating]
        data.append(row)

    return data

def write_csv(data, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

if __name__ == "__main__":
    num_appointments = 5000  # You can change this to the desired number of appointments
    doctor_data = [row for row in csv.reader(open("doctor_information.csv"))]
    patient_data = [row for row in csv.reader(open("patient_information.csv"))]
    
    generated_data = generate_fake_appointments(num_appointments, doctor_data, patient_data)
    write_csv(generated_data, "appointments.csv")
