import json
import tkinter as tk
from tkinter import simpledialog, messagebox

from difflib import get_close_matches

def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data:  dict=json.load(file)
    return data

def load_knowledge_base2(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent = 2)

def find_best_match(user_question: str, questions: list[str]) ->str | None:
    matches: list= get_close_matches(user_question,questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]
def save_knowledge_base(filename: str, knowledge_base: dict) -> None:
    with open(filename, 'w') as file:
        json.dump(knowledge_base, file)    

def chat_bot():
    knowledge_base = load_knowledge_base('knowledge_base.json')
    
    def on_send():
        user_input = user_entry.get()
        if user_input.lower() == 'quit':
            root.quit()
            return

        best_match = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])
        
        if best_match:
            answer = get_answer_for_question(best_match, knowledge_base)
            chat_log.config(state=tk.NORMAL)
            chat_log.insert(tk.END, f"You: {user_input}\n")
            chat_log.insert(tk.END, f"Bot: {answer}\n")
            chat_log.config(state=tk.DISABLED)
        else:
            chat_log.config(state=tk.NORMAL)
            chat_log.insert(tk.END, f"You: {user_input}\n")
            chat_log.insert(tk.END, "Bot: I don't know the answer. Can you teach me?\n")
            chat_log.config(state=tk.DISABLED)
            new_answer = simpledialog.askstring("Teach me", "Type the answer or write 'skip':")
            if new_answer and new_answer.lower() != "skip":
                knowledge_base["questions"].append({"question": user_input, "answer": new_answer})
                save_knowledge_base("knowledge_base.json", knowledge_base)
                chat_log.config(state=tk.NORMAL)
                chat_log.insert(tk.END, "Bot: Thank you, I have learned a new answer.\n")
                chat_log.config(state=tk.DISABLED)
        
        user_entry.delete(0, tk.END)

    root = tk.Tk()
    root.title("ChatBot")

    chat_log = tk.Text(root, state=tk.DISABLED, wrap=tk.WORD)
    chat_log.pack(padx=10, pady=10)

    user_entry = tk.Entry(root)
    user_entry.pack(padx=10, pady=10)
    user_entry.bind("<Return>", lambda event: on_send())

    send_button = tk.Button(root, text="Send", command=on_send)
    send_button.pack(pady=5)

    root.mainloop()

if __name__ == '__main__':
    chat_bot()
