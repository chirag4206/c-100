class Student(object):
    def __init__(self,name,age,gender,grade):
        self.name=name
        self.age=age
        self.gender=gender
        self.grade=grade

    def setGrade(self,course,grade):
        self.grades[course]=grade
    
    def getGrade(self,course):
        return self.grades[course]

sam=Student("sam",14,"male",8)
print(sam.name)
class Car(object):
    def __init__(self,model,company,seater):
        self.model=model
        self.company=company
        self.seater=seater
    def start(self):
        print("started")
    def stop(self):
        print("stopped")
Xuv=Car("xuv700","mahindra",7)
print(Xuv.model)
MG=Car("MG","hectar",7)
print(MG.model)
        