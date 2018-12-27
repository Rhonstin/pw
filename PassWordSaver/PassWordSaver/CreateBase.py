import shelve
shelfFile = shelve.open("password")
shelfFile["password"] = "password"
shelfFile.close()