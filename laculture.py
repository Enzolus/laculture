import json

with open('laculturequestions.json', 'r', encoding='utf-8') as file:
    questions = json.load(file)

def ask_question(question):
    print(question["question"])
    for option in question["options"]:
        print(option)
    user_answer = input("Votre réponse (a, b, c, d) : ")
    return user_answer.lower() == question["answer"][0].lower()

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
