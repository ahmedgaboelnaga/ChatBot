import json
from difflib import get_close_matches
import tkinter as tk
from tkinter import scrolledtext


def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data = json.load(file)
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


class ChatBotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ChatBot")
        self.root.configure(bg="#202020")

        self.knowledge_base = load_knowledge_base("Knowledge_base.json")

        self.chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, bg="#202020", fg="white", font=("Arial", 18))
        self.chat_area.pack(padx=10, pady=(20, 10), fill=tk.BOTH, expand=True)
        self.chat_area.configure(state=tk.DISABLED)

        self.user_input = tk.Entry(root, font=("Arial", 16), bg="#202020", fg="white")
        self.user_input.pack(padx=10, pady=5, fill=tk.X)
        self.user_input.bind("<Return>", self.send_message)
        self.user_input.focus_set()  # Set focus to the input area

        self.send_button = tk.Button(root, text="Send", command=self.send_message, bg="#3e2d2e", fg="white", font=("Arial", 16), bd=0)
        self.send_button.pack(pady=10)

        self.awaiting_answer = False
        self.last_user_question = ""
        self.prompt_message = "... Type your answer here or write skip to skip..."

    def send_message(self, event=None):
        user_message = self.user_input.get().strip()

        if self.awaiting_answer:
            if user_message.startswith(self.prompt_message):
                user_message = user_message[len(self.prompt_message):].strip()

            if not user_message:
                return

            if user_message.lower() != "skip":
                self.knowledge_base["questions"].append({"question": self.last_user_question, "answer": user_message})
                save_knowledge_base("Knowledge_base.json", self.knowledge_base)
                self.display_message("... Bot: Thank you! I have learned a lot!")
            self.awaiting_answer = False
            self.user_input.delete(0, tk.END)
            self.user_input.config(fg="white")
            self.user_input.insert(0, "")
            return

        if not user_message:
            return

        self.display_message(f"... You: {user_message}")
        self.user_input.delete(0, tk.END)

        best_match = find_best_match(user_message, [q["question"] for q in self.knowledge_base["questions"]])
        if best_match:
            answer = get_answer_to_question(best_match, self.knowledge_base)
            self.display_message(f"... Bot: {answer}")
        else:
            self.display_message("... Bot: I don't know the answer to this! Can you teach me?")
            self.awaiting_answer = True
            self.last_user_question = user_message
            self.user_input.config(fg="gray")
            self.user_input.insert(0, self.prompt_message)

    def display_message(self, message):
        self.chat_area.configure(state=tk.NORMAL)
        self.chat_area.insert(tk.END, f"{message}\n")
        self.chat_area.configure(state=tk.DISABLED)
        self.chat_area.see(tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = ChatBotApp(root)
    root.mainloop()
