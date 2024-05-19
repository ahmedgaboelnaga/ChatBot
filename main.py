import json
from difflib import get_close_matches


def load_knowledge_base(file_path: str) -> dict:
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        data = {"questions": []}
    return data


def save_knowledge_base(file_path: str, data: dict) -> None:
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)


def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None


def get_answer_to_question(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]
    return None


def chat_bot():
    knowledge_base: dict = load_knowledge_base("Knowledge_base.json")
    while True:
        user_input = input("You: ")

        if user_input.lower() == "quit":
            break
        else:
            best_match = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])
            if best_match:
                answer = get_answer_to_question(best_match, knowledge_base)
                print(f"Bot: {answer}")
            else:
                print(f"Bot: I don't know the answer to this! Can you teach me?")
                new_answer = input("Type your answer or write skip to skip the question: ")
                if new_answer.lower() != "skip":
                    knowledge_base["questions"].append({"question": user_input, "answer": new_answer})
                    save_knowledge_base("Knowledge_base.json", knowledge_base)
                    print("Thank you! I have learned a lot!")


if __name__ == "__main__":
    chat_bot()
