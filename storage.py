import csv
from quiz import Question


def load_questions(filename):
    """Loads quiz questions from a CSV file."""

    questions = []

    try:
        with open(filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                question = Question(
                    row["question"],
                    {
                        "A": row["option_a"],
                        "B": row["option_b"],
                        "C": row["option_c"],
                        "D": row["option_d"]
                    },
                    row["correct_answer"]
                )

                questions.append(question)

    except FileNotFoundError:
        print("Question file not found.")

    return questions


def save_result(filename, name, score, total_questions):
    """Saves quiz results to a CSV file."""

    try:
        with open(filename, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            writer.writerow([
                name,
                score,
                total_questions
            ])

    except Exception as error:
        print(f"Error saving results: {error}")