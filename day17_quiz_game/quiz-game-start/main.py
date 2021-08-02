from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

if __name__ == "__main__":
    for item in question_data:
        question = Question(item["text"], item["answer"])
        quiz = QuizBrain(question)
        quiz.ask_question()

    print("You've completed the quiz")
    print(f"Your final score was: {QuizBrain.current_score}/{QuizBrain.question_number}")
