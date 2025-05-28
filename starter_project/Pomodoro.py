import customtkinter as ctk

class Pomodoro:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("POMODORO")
        self.window._set_appearance_mode("System")
        self.window.geometry('280x300')
        self.get_input()

    def timer(self):
        try:
            self.load_time = int(self.time_enter.get())
        except ValueError:
            self.time_display.configure(text ="Invalid Input!")
            return
        self.countdown()
    
    def countdown(self):
        if self.load_time > 0:
            mins, sec = divmod(self.load_time,60)
            formet_time = f"{mins}:{sec}"
            self.time_display.configure(text =f"Time: {formet_time}")
            print(f"Time: {formet_time}")
            self.load_time -= 1
            self.window.after(1000, self.countdown)
        else:
            self.time_display.configure(text =f"TimeOut")
        #    self.window._set_appearance_mode("dark")

    def get_input(self):
        self.time_enter= ctk.CTkEntry(self.window,text_color='black', placeholder_text="Enter time in sec", placeholder_text_color='black')
        self.time_enter.pack(pady=20)

        self.press_button = ctk.CTkButton(self.window, text="Start", corner_radius=50, command= self.timer)
        self.press_button.pack(pady=20)

        self.time_display = ctk.CTkLabel(self.window, text="Timer: 0", width=100, height= 30)
        self.time_display.pack(pady=20)



    def run(self):
        self.window.mainloop()

if __name__ == '__main__':
    app = Pomodoro()
    app.run()
