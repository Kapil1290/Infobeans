class Patient:
    __total_patient = 0
    def __init__(self, name, id, disease, doctor_assigned):
        self.__name = name
        self.__id = id
        self.__disease = disease
        self.__doctor = doctor_assigned

        Patient.__total_patient += 1
        

    def __str__(self):
        return f"Patient: {self.__name}\nId: {self.__id}\nDisease: {self.__disease}\nDoctor Assigned: {self.__doctor}"
    
    def change_doctor(self, doctor):
        print(f"Doctor changed from {self.__doctor.upper()} to {doctor.upper()}")
        self.__doctor = doctor
        return
    
    @staticmethod
    def total_patient():
        print(Patient.__total_patient)
        return

p1 = Patient("jay", 101, "hedache", "Manoj pandey")
p2 = Patient("om", 102, "lung infection", "deepak tiwari")
Patient.total_patient()
p1.change_doctor("ajay kumar")
    

