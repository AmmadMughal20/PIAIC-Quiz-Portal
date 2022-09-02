stars = 39

def wellcome_menu():
    print("*"*stars+"\n"+"*** Welcome to PIAIC Testing Portal ***"+"\n"+"*"*stars+"\n\n1. Login\n2. Exit\n")

def admin_menu():
    print("\n"+"*"*stars+"\n******** Welcome to Admin portal ******\n"+"*"*stars+"\n\n************** Admin Menu *************\n\n1. Create new quiz.\n2. Add another question to quiz. \n3. print quiz questions.\n4. Logout.\n")

def quiz_creation_primary_menu():
    print("*"*stars+"\n********** Quiz Creation Menu *********\n"+stars*"*"+"\n\n1. Add a question\n2. Back\n")

def quiz_creation_secondary_menu():
    print("********* Quiz Creation Menu **********"+"\n\n1. Add another question"+"\n2. Save Quiz \n3. Back")

def quiz_update_primary_menu():
    print("*"*stars+"\n********** Quiz Update Menu ***********\n"+"*"*stars+"\n\n1. Add another question\n2. Back\n")

def quiz_update_secondary_menu():
    print("********** Quiz Update Menu ***********\n1. Add another question\n2. Save Quiz\n3. Back\n")

def user_menu():
    print("\n"+"*"*stars+"\n******** Welcome to User portal ******\n"+"*"*stars+"\n\n************** User Menu *************\n\n1. Attempt quiz.\n2. Logout.\n")
