class Book:
    species ='Книга'

    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return "Название книги: {}".format(self.title),"Автор: {}".format(self.author),"Год издания: {}".format(self.year)

knizka = Book("Net",'chelovek','1111')
print(knizka.get_info())

class Circle:

    species = 'Круг'

    def __init__(self,radius):
        self.radius = radius

    def get_radius(self):
        return "Значение радиуса: {}".format(self.radius)

    def new_radius(self,new_radius):
        self.radius = new_radius
        return "Новое значение радиуса: {}".format(self.radius)

krug = Circle(10)

print(krug.get_radius())

print(krug.new_radius(18))
