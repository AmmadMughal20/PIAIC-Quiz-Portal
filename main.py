from QuizManagement import quiz_creation, quiz_csvtolist, no_of_questions, add_a_question, checkquiz, createresultfile
from Users import User
from menus import wellcome_menu, admin_menu, quiz_creation_primary_menu, quiz_creation_secondary_menu, quiz_update_primary_menu, quiz_update_secondary_menu, user_menu

while True:
    wellcome_menu()
    welcome_input = input("Please select the desired action number: ")
    if welcome_input == "1":
        print("\n*********** Authentication ************")
        print("Enter your userid and password!")

        userid, password = input("User ID: "), input("Password: ")

        user = User.authentication(userid, password)

        if user.role == 'Admin':
            while True:
                admin_menu()
                admin_input = input("Please enter the desired action number: ")
                if admin_input == '1':
                    quiz_creation_primary_menu()
                    questions_list = []
                    counter = 0
                    question_serial = 1
                    while True:
                        creation_input = input("Please enter the desired action number: ")
                        if creation_input == "1":
                            question = add_a_question(question_serial)
                            questions_list.append(question)
                            question_serial+=1
                            counter+=1
                            quiz_creation_secondary_menu() 
                        elif creation_input == "2":
                            quiz_creation(questions_list)
                            break
                        elif creation_input == "3":
                            break
                        else:
                            print("Create Menu -> Wrong Selection!!! Try again...")

                elif admin_input == '2':
                    quiz_update_primary_menu()
                    existing_quiz_list = quiz_csvtolist()
                    total_questions = int(no_of_questions(existing_quiz_list))
                    new_question_serial = total_questions+1
                    while True:
                        update_input = input("Please enter the desired action number: ")
                        if update_input == "1":
                            question = add_a_question(new_question_serial)
                            existing_quiz_list.append(question)
                            quiz_update_secondary_menu()
                        elif update_input == "2":
                            quiz_creation(existing_quiz_list)
                            break
                        elif update_input == "3":
                            break
                        else:
                            print("Update Menu -> Wrong Selection!!! Try Again...")

                elif admin_input == '3':
                    existing_quiz_list = quiz_csvtolist()
                    print(existing_quiz_list)
                elif admin_input == '4':
                    print("Signing you out... Bye Bye!!!")
                    break
                else:
                    print("Admin Menu -> Wrong Selection!!! Try again...")

        elif user.role == 'User':
            while True:
                user_menu()
                user_input = input("Please enter the desired action number: ")

                if user_input == '1':
                    quiz = quiz_csvtolist()
                    print("******** PIAIC QUIZ BATCH 36/37 *******\n\nNOTE: Try to select the correct answers\nfor all questions.")
                    user_answers = user.attemptquiz(quiz)
                    correct_choices = checkquiz(user_answers)
                    total_questions = int(no_of_questions(quiz))
                    percentage_result = (correct_choices/total_questions)*100
                    print(f"You got {percentage_result}% marks.")
                    createresultfile(user.userid, percentage_result)

                elif user_input == '2':
                    print("Signing you out... Bye Bye!!!")
                    break
                else:
                    print("User Menu -> Wrong Selection!!! Try again...")


        else:
            print("User Not Found!")

    elif welcome_input == "2":
        print("Exiting Program!!! Bye Bye...")
        exit()
    
    else:
        print("Welcome Menu -> Wrong Input!!! Try Again...")