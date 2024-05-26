from cryptography.fernet import Fernet

def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key

key = load_key
fer = fernet(key)

def view():
    with open('passwords.text','r') as f:
        for line in f.readlines():
            data =line.rstrip()
            user,passw = data.split("|")
            print("User:", user,"Password:", 
            fer.decrypt(passw.encode()).decode())

def add():
    name = input('Account Name: ')
    pwd = input("Password : ")

    with open('passwords.text','a') as f:
        f.write(name + "|" + pwd + "\n")


while True:
    mode = input(
        "Would you like to add new password or view existing ones (view, add), press q to quit? ")
    if mode == "q":
        break

    if mode == "view":
        view()
    if mode == "add":
        add()
    else:
        print("Invalid mode")
        continue
