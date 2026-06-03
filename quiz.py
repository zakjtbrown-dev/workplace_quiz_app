class Question:
    """Represents one quiz question."""

    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer.upper()


class Quiz:
    """Manages quiz questions, answers, and scoring."""

    def __init__(self, questions):
        self.questions = questions
        self.user_answers = []

    def add_answer(self, answer):
        """Adds a user's answer after converting it to uppercase."""
        self.user_answers.append(answer.upper())

    def calculate_score(self):
        """Calculates the user's final score."""
        score = 0

        for index, question in enumerate(self.questions):
            if self.user_answers[index] == question.correct_answer:
                score += 1

        return score


def validate_name(name):
    """Checks that the user has entered a valid name."""
    return len(name.strip()) > 0


def validate_answer(answer):
    """Checks that the answer is A, B, C or D."""
    return answer.upper() in ["A", "B", "C", "D"]