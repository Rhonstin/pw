#Программа для незащищенного хранения паролей.
PASSWORDS = {"email" : "HEHEHE", "blog" : "hahaha", "vk" : "1234"}
import sys, paperclip
if len(sys.argv) < 2:
    print("Использование: ")
    sys.exit()
account = sys.argv[1]
if account in PASSWORDS:
    pyperclip.copy(Passwords[account])
    print("Пароль для " + account +  " скопирован в буфер" )
else:
    print("Учетная запись " + account + "отсутствует в списке.")

