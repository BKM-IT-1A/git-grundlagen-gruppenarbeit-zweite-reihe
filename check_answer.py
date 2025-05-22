def is_correct(question, answer_index):
    return question["correct"] == answer_index

if __name__ == "__main__":
    question = {
        "text": "Was ist die Hauptstadt von Frankreich?",
        "options": ["Berlin", "Paris", "Madrid", "Rom"],
        "correct": 1
    }

    answer = 1
    print("Question:", question["text"])
    for i, option in enumerate(question["options"]):
        print(f"{i + 1}. {option}")

    if is_correct(question, answer):
        print("Richtig")
    else:
        print("Falsch")
