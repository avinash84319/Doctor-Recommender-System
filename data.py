import csv
import random

# Function to generate random data for the CSV
def generate_data(num_patients, num_appointments_per_patient):
    data = []
    patient_ratings = {}

    for patient_id in range(1, num_patients + 1):

        patient_age = random.randint(0, 80)
        patient_gender = random.choice([0, 1])  # 0 for Male, 1 for Female
        patient_health_condition = random.randint(0, 100)  # 0 for Healthy, 1 for Condition A, 2 for Condition B
        patient_location = random.randint(0, 100)  # 0 for City A, 1 for City B, 2 for City C
        previous_doctor_type = random.randint(0, 100)  # 0 for General Practitioner, 1 for Specialist
        last_appointment_days = random.randint(1, 300)

        for rating in range(1, 6):

            appointment_id = len(data) + 1
            doctor_id = random.randint(2000, 2999)
            doctor_age = ((5-rating)/5)*80+patient_age
            doctor_location = (patient_location + random.randint(-rating*10, rating*10))
            doctor_type = previous_doctor_type if rating > 3 else random.randint(0, 100)
            experience_in_years = 30*((rating+random.uniform(-1,1))/5)
            patients_in_lifetime = 500*(rating+random.uniform(-1,1)/5)
            patients_in_queue = 10*(rating+random.uniform(-1,1)/5)

            data.append([
                appointment_id, patient_id, patient_age, patient_gender, patient_health_condition,
                patient_location, previous_doctor_type, last_appointment_days, doctor_id,
                doctor_age, doctor_location, doctor_type, experience_in_years, patients_in_lifetime,
                patients_in_queue, rating
            ])

    return data

# Function to write data to CSV
def write_to_csv(file_path, header, data):
    with open(file_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(header)
        csv_writer.writerows(data)

# Define header for the CSV file
csv_header = [
    'Appointment ID', 'Patient ID', 'Patient Age', 'Patient Gender', 'Patient Health Condition',
    'Patient Location', 'Previous Doctor Type', 'Last Appointment (Days)', 'Doctor ID',
    'Doctor Age', 'Doctor Location', 'Doctor Type', 'Experience (Years)', 'Patients in Lifetime',
    'Patients in Queue', 'Rating'
]

# Generate and write data to CSV file
num_patients = 1000
num_appointments_per_patient = 10  # Set to 5 to ensure each rating is used for each patient
csv_data = generate_data(num_patients, num_appointments_per_patient)
write_to_csv('./new_trail/generated_data.csv', csv_header, csv_data)
