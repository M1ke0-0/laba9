class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password

    def set_password(self, new_password):
        self.__password = new_password

    def chek_password(self, password):
        if password == self.__password:
            return "True"
        else:
            return  "False"
    def getinfo(self):
        return "Username: {}".format(self.username), "Email: {}".format(self.email), "Password: {}".format(self.__password)

User_1 = UserAccount('Imya','email@email.com','parol')
print(User_1.getinfo())
User_1.set_password('parol_new')
print(User_1.chek_password('parol_test'))

class Vehicle():
    def __init__(self, mark, model):
        self.mark = mark
        self.model = model

    def get_info(self):
        return "Марка: {}".format(self.mark), "Модель: {}".format(self.model)

class Car(Vehicle):
    def __init__(self, mark, model, fuel_type):
        super().__init__(mark, model)
        self.fuel_type = fuel_type

    def get_info(self):
        return "Марка: {}".format(self.mark), "Модель: {}".format(self.model), "Тип топлива: {}".format(self.fuel_type)
carr = Car('marka_machini', 'model_machini', '98')

print(carr.get_info())







