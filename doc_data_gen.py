import csv
import random

def generate_doctor_data(num_doctors):
    header = ["ID", "Age", "Type", "Experience", "Hospital Location", "Patients in Queue", "Patients Seen in Lifetime"]
    data = [header]

    for i in range(1, num_doctors + 1):
        doctor_id=random.randint(500,15000)
        age = random.randint(30, 80)
        doctor_type = random.randint(1,100) # Numerical representation for doctor type
        experience = random.randint(0, 30)
        location_id = random.randint(900,1000)
        patients_in_queue = random.randint(1, 30)
        patients_seen_lifetime = random.randint(1000, 10000)


        row = [doctor_id, age, doctor_type, experience, location_id, patients_in_queue, patients_seen_lifetime]
        data.append(row)

    return data

def write_csv(data, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

if __name__ == "__main__":
    num_doctors =100000  # You can change this to the desired number of doctors
    generated_data = generate_doctor_data(num_doctors)
    write_csv(generated_data, "doctor_information.csv")
