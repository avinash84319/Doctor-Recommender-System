import csv
import random

def calculate_rating(doctor_age, patient_age, doctor_location, patient_location, doctor_type, patient_type):
    # Calculate age difference
    age_difference = abs(doctor_age - patient_age)

    # Adjust rating based on age difference
    age_rating = max(5 - age_difference // 5, 0)

    # Adjust rating based on location and type preferences
    location_rating = 2.5 if doctor_location == patient_location else 0
    type_rating = 1.5 if doctor_type == patient_type else 0

    # Combine all factors to get the final rating
    final_rating = min(5, age_rating + location_rating + type_rating)

    return final_rating

def generate_fake_appointments(num_appointments, doctor_data, patient_data):
    header = ["AppointmentID", "PatientID", "DoctorID", "AppointmentDate", "Rating"]
    data = [header]

    for i in range(1, num_appointments + 1):
        print(i)
        appointment_id = i
        patient_id = random.choice(patient_data[1:])[0]  # Randomly select a patient ID from the patient dataset
        eligible_patients = [patient for patient in patient_data[1:] if patient[0] != patient_id]

        if not eligible_patients:
            print(f"No eligible patients found for appointment {i}. Skipping appointment.")
            continue

        patient_data.remove(eligible_patients[0])  # Remove the selected patient from the patient dataset

        # Find any available doctor
        eligible_doctors = doctor_data[1:]
        
        if not eligible_doctors:
            print(f"No eligible doctors found for patient {i}. Skipping appointment.")
            continue

        chosen_doctor = random.choice(eligible_doctors)
        doctor_id = chosen_doctor[0]
        doctor_age = int(chosen_doctor[1])
        doctor_location = chosen_doctor[4]
        doctor_type = chosen_doctor[2]

        patient_age = int(eligible_patients[0][1])
        patient_location = eligible_patients[0][4]
        patient_type = eligible_patients[0][6]

        appointment_date = random.randint(1, 365)  # Representing days from now
        rating = calculate_rating(doctor_age, patient_age, doctor_location, patient_location, doctor_type, patient_type)

        row = [appointment_id, patient_id, doctor_id, appointment_date, rating]
        data.append(row)

    return data

def write_csv(data, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

if __name__ == "__main__":
    num_appointments = 20000  # You can change this to the desired number of appointments
    doctor_data = [row for row in csv.reader(open("doctor_information.csv"))]
    patient_data = [row for row in csv.reader(open("patient_information.csv"))]
    
    generated_data = generate_fake_appointments(num_appointments, doctor_data, patient_data)
    write_csv(generated_data, "appointments.csv")
