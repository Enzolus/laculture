import json

with open('laculturequestions.json', 'r', encoding='utf-8') as file:
    questions = json.load(file)

def ask_question(question):
    print(question["question"])
    for idx, option in enumerate(question["options"], start=1):
        print(f"{idx}. {option}")

    user_answer = input("Votre réponse (1, 2, 3, 4) : ")
    
    try:
        user_answer_idx = int(user_answer) - 1
        return question["options"][user_answer_idx] == question["answer"]
    except (ValueError, IndexError):
        return False

def run_quiz(questions):
    score = 0
    for question in questions:
        if ask_question(question):
            print("Bonne réponse!")
            score += 1
        else:
            print("Mauvaise réponse.")
    print(f"Votre score final est de {score}/{len(questions)}")

# Exécuter le quiz
run_quiz(questions)
