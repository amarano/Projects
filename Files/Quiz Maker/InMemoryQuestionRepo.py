class NoRecordFoundException(BaseException):
    pass


class InMemoryQuestionRepo:
    
    def __init__(self):
        self.questions = []
        
    def add(self, question):
        self.questions.append(question)

    def remove(self, question):
        if question in self.questions:
            self.questions.remove(question)
            
    def findAll(self, predicate):
        return filter(predicate, self.questions)
    
    def findOneOrNone(self, predicate):
        filtered = self.findAll()
        if (len(filtered) == 1):
            return filtered[0]
        else:
            return None
        
    def findOne(self, predicate):
        filtered = self.findAll()
        if len(filtered) > 0:
            return filtered[0]
        else:
            NoRecordFoundException()
            