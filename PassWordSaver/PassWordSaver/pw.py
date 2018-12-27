#python3
#Программа для незащищенного хранения паролей.

import shelve,sys,pyperclip
print("Привет, введите пароль:")
passwords = input()
if passwords == "password":
    print("Добро пожаловать, от чего нужен пароль?")
    answer = input()
    shelfFile = shelve.open("password")
    PASSWORDS = {"email" : shelfFile["password"]}
    shelfFile.close()
    if answer == "email":
        account = answer
        if account in PASSWORDS:
            pyperclip.copy(PASSWORDS[account])
            print("Пароль для " + account +  " скопирован в буфер" )
        else:
            print("Учетная запись " + account + "отсутствует в списке.")

