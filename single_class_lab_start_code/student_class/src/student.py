

class Student:
    def __init__(self, name, cohort):
        self.name = name
        self.cohort = cohort
        # self.talk = "I can talk!"
        
    def talk(self):
        return "I can talk!"
        
    def say_favourite_language(self, language):
        return f"I love {language}"
    