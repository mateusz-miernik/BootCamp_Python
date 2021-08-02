class QuizBrain:
    question_number = 0
    current_score = 0

    def __init__(self, question_obj):
        self.question_obj = question_obj
        QuizBrain.question_number += 1

    def _process_answer(self, answer):
        if answer == self.question_obj.answer:
            QuizBrain.current_score += 1
            print("You got it right!")
        else:
            print("That's wrong.")

        print(f"The correct answer was: {self.question_obj.answer}")
        print(f"Your current score is: {QuizBrain.current_score}/{QuizBrain.question_number}\n")

    def ask_question(self):
        user_answer = input(f"Q.{QuizBrain.question_number}: {self.question_obj.text}. (True/False): ").capitalize()
        self._process_answer(user_answer)
