def is_correct(question, answer_index): 
  return question ["correct"] == answer_index

if __name__ == "__main__":
    questions = {
      "text": "Was ist das Chemische Zeichen von Wasser"
      "option": ["H2O","NaOH","CO2","O2"]
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
