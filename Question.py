class Question():
    def __init__(self, sr, question_desc, ansA, ansB, ansC, ansD):
        self.sr = sr
        self.question_desc = question_desc
        self.ansA = ansA
        self.ansB = ansB
        self.ansC = ansC
        self.ansD = ansD

    def print_question(self):
        print(f"\n*********** Question No: {self.sr} ************")
        print(f"Q: {self.question_desc}")
        print(f"*************** Choices ***************")
        print(f"A. {self.ansA}  B. {self.ansB} C. {self.ansC} D. {self.ansD}\n")