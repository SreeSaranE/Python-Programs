import customtkinter as ctk
import tkinter as tk
import json
from difflib import get_close_matches

class ai_chatbot:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("MyAI")
        self.window._set_appearance_mode("System")
        self.window.geometry('400x350')
        self.window.resizable(False,False)
        self.chat_history = []

    def show(self):
        self.bottom_frame = ctk.CTkFrame(master=self.window)
        self.bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)
        self.middle_frame = ctk.CTkFrame(master=self.window)
        self.middle_frame.pack(side=tk.RIGHT, fill=tk.X, padx=10, pady=10)

        self.header = ctk.CTkLabel(self.window,
                                   text="AI ChatBot\n\nHistory",
                                   width=60, height=10
                                   ,font=("Arial", 15))
        self.header.pack(pady=10)

        self.chats = ctk.CTkLabel(master=self.middle_frame, text_color='white',
                                  fg_color='#24252B',
                                  text="Chat History",
                                  width=260, height=300,
                                  justify="left", anchor="sw"
                                  )
        self.chats.pack(pady=10)
        
        self.user_input = ctk.CTkEntry(master=self.bottom_frame, text_color='black',
                                      placeholder_text="ask me",
                                      fg_color="#CFCFCF",
                                      placeholder_text_color='black',
                                      corner_radius=50,
                                      width=290, height=28,
                                      justify="right"
                                      )
        self.user_input.pack(side=ctk.LEFT, pady=10, padx= 10)

    def button(self):
        self.send_button = ctk.CTkButton(master=self.bottom_frame,
                                         text="Send",
                                         corner_radius=50,
                                         width=15, height=27,
                                         command= self.aiBot)
        self.send_button.pack(side=ctk.RIGHT, pady=10, padx= 5)

    def best_matches(self, user_questions: str, question) -> str | None:
        questions: list[str] = [word for word in question]
        matches: list = get_close_matches(user_questions, questions, n=1, cutoff=0.4)

        if matches:
            return matches

    def aiBot(self):
     #   while True:
            self.load_user_input = self.user_input.get()
            best_match: str | None = self.best_matches(self.load_user_input, self.data)
            if  best_match == None:
                join = None
            else:
                join = '_'.join(best_match)

            if answer := self.data.get(join):
                self.chat_history.append(f"you: {self.load_user_input}")
                self.chat_history.append(f"Bot: {answer}\n")
            #    for i in self.chat_history:
            #        print(i)
                print(self.chat_history)
                self.print_chat_history= '\n'.join(self.chat_history)
                self.chats.configure(text = self.print_chat_history)
                if answer == 'bye':
                    pass
      #              break

            else:
                print("Bot: I don't understand")

    def run(self):
        with open('udemy\data.json', 'r') as file:
            self.data = json.load(file)
        self.show()
        self.button()
        self.window.mainloop()

if __name__ == '__main__':
    app = ai_chatbot()
    app.run()
