print("Nomer 1")
def reading(filee):
    with open('filee', "r") as file:
        content = file.read()
    return content

def reading_strok(filee):
    with open('filee', "r") as file:
        line = file.readlines()
    return line


print("Nomer 2")

with open("text.txt", "w") as file: #Это с удаление прошлого
    file.write("appended text")

with open("text.txt", "a") as file: #Это без удаления прошлого
    file.write("appended text")


print("Nomer 3")

def reading(filee):
    try:
        with open('filee', "r") as file:
            content = file.read()
        return content
    except FileNotFoundError as e:
        return e