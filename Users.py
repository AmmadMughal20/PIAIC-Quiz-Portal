import csv
from Question import Question

class User():
    def __init__(self, userid, password, role):
        self.userid = userid
        self.password = password
        self.role = role

    def authentication(userid, password):
        with open("UserData.csv", "r") as users:
            usersdata = csv.reader(users)
            usersdatalist = []
            for line in usersdata:
                usersdatalist += line

            found_userid_index = usersdatalist.index(userid)
            if found_userid_index != "":
                found_password_index = found_userid_index+1
                found_role_index = found_password_index+1 
                if password == usersdatalist[found_password_index]:
                    user = User(usersdatalist[found_userid_index], usersdatalist[found_password_index], usersdatalist[found_role_index])
                    return user

    def attemptquiz(self, quiz):
        user_answers = []
        for ques in quiz:
            questiontoprint = Question(ques[0],ques[1],ques[2],ques[3],ques[4],ques[5])
            questiontoprint.print_question()
            answertoquestion = input('Answer with correct value: ')
            user_answers.append(answertoquestion)
        return user_answers