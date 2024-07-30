from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)                     //here we can add a master password

write_key()'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = (line.rstrip()) 
            user, pswd = data.split("|")
            print("User:", user, " | Password:", fer.decrypt(pswd.encode()).decode())
def add():
    name  = input("Account Name: ")
    pwd = input("Password: ")

    with open('password.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    option = input("Add or View existing password?/Exit (Add/View/q):").lower()
    if option == "q":
        break


    if option == "add":
        add()
    elif option == "view":
        view()
    else:
        print("Enter Correct option!😒")
        continue