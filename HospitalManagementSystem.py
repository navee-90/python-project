class Patient:
    def __init__(self, patient_id, name, age, disease):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease

class Doctor:
    def __init__(self, doctor_id, name, specialty):
        self.doctor_id = doctor_id
        self.name = name
        self.specialty = specialty

class Appointment:
    def __init__(self, patient_name, doctor_name, date):
        self.patient_name = patient_name
        self.doctor_name = doctor_name
        self.date = date

class Hospital:
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.appointments = []

    # Adding new patients
    def add_patient(self):
        patient_id = input("Enter Patient ID: ")
        name = input("Enter Patient Name: ")
        age = input("Enter Patient Age: ")
        disease = input("Enter Disease: ")
        self.patients.append(Patient(patient_id, name, age, disease))
        print(f"Patient {name} added successfully.\n")

    # Viewing all patients
    def view_patients(self):
        if not self.patients:
            print("No patients found.\n")
            return
        print("\nList of Patients:")
        for p in self.patients:
            print(f"ID: {p.patient_id}, Name: {p.name}, Age: {p.age}, Disease: {p.disease}")
        print("")

    # Deleting a patient
    def delete_patient(self):
        patient_id = input("Enter Patient ID to delete: ")
        for p in self.patients:
            if p.patient_id == patient_id:
                self.patients.remove(p)
                print(f"Patient {p.name} deleted successfully.\n")
                return
        print("Patient not found.\n")

    # Adding new doctors
    def add_doctor(self):
        doctor_id = input("Enter Doctor ID: ")
        name = input("Enter Doctor Name: ")
        specialty = input("Enter Specialty: ")
        self.doctors.append(Doctor(doctor_id, name, specialty))
        print(f"Doctor {name} added successfully.\n")

    # Viewing all doctors
    def view_doctors(self):
        if not self.doctors:
            print("No doctors found.\n")
            return
        print("\nList of Doctors:")
        for d in self.doctors:
            print(f"ID: {d.doctor_id}, Name: {d.name}, Specialty: {d.specialty}")
        print("")

    # Scheduling an appointment
    def schedule_appointment(self):
        patient_name = input("Enter Patient Name: ")
        doctor_name = input("Enter Doctor Name: ")
        date = input("Enter Appointment Date (YYYY-MM-DD): ")
        self.appointments.append(Appointment(patient_name, doctor_name, date))
        print(f"Appointment for {patient_name} with Dr. {doctor_name} scheduled on {date}.\n")

    # Viewing all appointments
    def view_appointments(self):
        if not self.appointments:
            print("No appointments scheduled.\n")
            return
        print("\nList of Appointments:")
        for a in self.appointments:
            print(f"Patient: {a.patient_name}, Doctor: {a.doctor_name}, Date: {a.date}")
        print("")

# Menu-driven interface
def main():
    hospital = Hospital()
    while True:
        print("\nHospital Management System")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Delete Patient")
        print("4. Add Doctor")
        print("5. View Doctors")
        print("6. Schedule Appointment")
        print("7. View Appointments")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            hospital.add_patient()
        elif choice == "2":
            hospital.view_patients()
        elif choice == "3":
            hospital.delete_patient()
        elif choice == "4":
            hospital.add_doctor()
        elif choice == "5":
            hospital.view_doctors()
        elif choice == "6":
            hospital.schedule_appointment()
        elif choice == "7":
            hospital.view_appointments()
        elif choice == "8":
            print("Exiting system...")
            break
        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    main()
