import csv

def quiz_creation(listofquestions):

    titleslist = ["Sr.", "Question", "Option A", "Option B", "Option C", "Option D", "Correct Answer"]
    with open("Quiz.csv","w") as quizfile:
        write = csv.writer(quizfile)
        write.writerow(titleslist)
        write.writerows(listofquestions)

def quiz_csvtolist():
    with open("Quiz.csv","r") as quizfile:
        questions = csv.reader(quizfile)
        listofquestions = []
        for line in questions:
            question = []
            question += line
            listofquestions.append(question)
        listofquestions_witoutserial = listofquestions[1:]
        return listofquestions_witoutserial

def no_of_questions(quizlistwithouttitle):
    return len(quizlistwithouttitle)

def add_a_question(question_serial):
    question = []
    print("**** Enter Question Details below *****")
    question_title, answerA, answerB, answerC, answerD, correctanswer = input("\nEnter Question: "),input("Enter answer A: "),input("Enter answer B: "),input("Enter answer C: "),input("Enter answer D: "),input("Enter correct answer: ")
    question.append(str(question_serial))
    question.append(question_title)
    question.append(answerA)
    question.append(answerB)
    question.append(answerC)
    question.append(answerD)
    question.append(correctanswer)
    return question

def quiz_correct_answers():
    quizlist = quiz_csvtolist()
    correctanswers = []
    for question in quizlist:
        correctanswers.append(question[6])
    return correctanswers

def checkquiz(user_answers):
    correctanswers = quiz_correct_answers()
    counter = 0
    correct_choices = 0
    for ans in user_answers:
        if ans == correctanswers[counter]:
            correct_choices+=1
            counter+=1
    return(correct_choices)

def createresultfile(name, result):
    with open(f"{name}_result.txt", "w") as result_file:
        result_file.write(f"Name = name\nResult = {result}%")
