class QuizBrain:

    def __init__(self, q_list):
        self.question_list = q_list
        self.question_number = 0
        self.current_score = 0
        self.current_question = None

    def still_has_questions(self):
        return len(self.question_list) > self.question_number

    def _process_answer(self, answer):
        if answer == self.current_question.answer:
            self.current_score += 1
            print("You got it right!")
        else:
            print("That's wrong.")

        print(f"The correct answer was: {self.current_question.answer}")
        print(f"Your current score is: {self.current_score}/{self.question_number}\n")

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        user_answer = input(f"Q.{self.question_number+1}: "
                            f"{self.current_question.text}. (True/False): ").capitalize()
        self.question_number += 1
        self._process_answer(user_answer)
