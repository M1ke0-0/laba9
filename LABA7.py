class Employee:
    def __init__ (self, name,id):
        self.name = name
        self.id = id

    def get_info(self):
        return "Name: {}".format(self.name), "Id: {}".format(self.id)


class Manager(Employee):
    def __init__ (self,department,name,id, *args):
        super().__init__(name, id, *args)
        self.department = department

    def manage_project(self):
        return "Project: {}".format(self.department)

    def get_info(self):
        return "Name: {}".format(self.name), "Id: {}".format(self.id), "Poject: {}".format(self.department)


class Technician(Employee):
    def __init__(self,name,id,specialization, *args):
        super().__init__(name,id, *args)
        self.specialization = specialization

    def perform_maintenance(self):
        return "Maintenance: {}".format(self.specialization)

    def get_info(self):
        return "Name: {}".format(self.name), "Id: {}".format(self.id),"Maintenance: {}".format(self.specialization)


class TechManager(Manager,Technician):
    def __init__(self, id, name, specialization,department):
        super().__init__(id, name, specialization, department)
        self.team = []

    def get_info(self):
        return "Name: {}".format(self.name), "Id: {}".format(self.id), "Poject: {}".format(self.department),"Maintenance: {}".format(self.specialization)

    def add_employee(self, data):
        self.team.append(data)

    def get_team_info(self):
        result = ""
        for joiner in self.team:
            result += f"{joiner.get_info()}\n"
        return result


Rab = TechManager(12,"Imya","Prof_rav","13")
R1 = Employee("Dima",1 )
R2 = Employee("Ivan",2)
R3 = Employee("Sasha",3)
team = [R1, R2, R3]
for joiner in team:
    Rab.add_employee(joiner)
print(Rab.get_info())
print(Rab.get_team_info())
