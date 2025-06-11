import json
from difflib import get_close_matches

def best_matches(user_questions: str, question) -> str | None:
    questions: list[str] = [word for word in question]
    matches: list = get_close_matches(user_questions, questions, n=1, cutoff=0.4)

    if matches:
        return matches
    
def chat_bot(knowledge):
    while True:
        user_input: str = input("You: ")
        best_match: str | None = best_matches(user_input, knowledge)
        if  best_match == None:
            join = None
        else:
            join = '_'.join(best_match)

        if answer := knowledge.get(join):
            print(f"Bot: {answer}" )
            if answer == 'bye':
                break
        else:
            print("Bot: I don't understand")

if __name__ == '__main__':
    with open('udemy\data.json', 'r') as file:
        data = json.load(file)

    chat_bot(data)
