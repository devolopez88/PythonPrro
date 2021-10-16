
def read():
    number = []
    #with open("./Project1/decimal.txt", "r", encoding="utf-8") as f
    with open("./files/decimal.txt", "r", encoding="utf-8") as file:
        for line in file:
            number.append(int(line))
    print(number) 
    
def write():
    names = ["Adriana", "Alvaro", "Andrea", "Angela", "Gabriela", "Luisa", "Oscar"]
    with open("./files/names.txt", "w", encoding="utf-8") as file:
        for lnames in names:
            file.write(lnames + "\n")

def run():
    #read()
    write()

if __name__ == "__main__":
    run()
