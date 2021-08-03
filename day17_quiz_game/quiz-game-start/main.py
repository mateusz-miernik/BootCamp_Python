from question_model import Question
from new_data import question_data
from quiz_brain import QuizBrain
import textwrap


def wrap(s: str, width: int):
    return textwrap.fill(s, width)


if __name__ == "__main__":
    question_bank = [Question(wrap(question["question"], 75), question["correct_answer"])
                     for question in question_data]
    quiz = QuizBrain(question_bank)

    while quiz.still_has_questions():
        quiz.next_question()

    print("You've completed the quiz")
    print(f"Your final score was: {quiz.current_score}/{quiz.question_number}")
