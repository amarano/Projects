__author__ = 'angelo'

class Quiz:

    def __init__(self, subjects, question_repo):
        self.subjects = subjects
        self.question_repo = question_repo
        self.questions = []

    def buildQuestions(self, question_count = 20):
        for x in range(question_count):
            questions = self.question_repo.findAll(lambda x: x.subject in self.subjects)
            self.questions = questions


