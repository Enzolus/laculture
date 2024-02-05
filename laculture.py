import json

def load_questions(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def ask_question(question):
    print(question["question"])
    for option in question["options"]:
        print(option)
    user_answer = input("Votre réponse (a, b, c, d) : ")
    return user_answer.lower() == question["answer"][0].lower()

def run_quiz(questions):
    while True:
        score = 0
        for question in questions:
            if ask_question(question):
                print("Bonne réponse!")
                score += 1
            else:
                print("Mauvaise réponse.")
        print(f"Votre score final est de {score}/{len(questions)}")

        replay = input("Voulez-vous rejouer ? (oui/non) : ")
        if replay.lower() != "oui":
            break

# Exécuter le quiz
questions = load_questions('laculturequestions.json')
run_quiz(questions)

