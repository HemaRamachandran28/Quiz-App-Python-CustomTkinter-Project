import customtkinter as ctk
from PIL import Image, ImageTk
import threading
import time
import winsound
import random
import os

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

questions = [
    {"question": "What is the capital of France?", "options": ["Paris", "Rome", "Berlin", "Madrid"], "answer": "Paris", "image": "paris.jpg"},
    {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Venus"], "answer": "Mars", "image": "mars.jpg"},
    {"question": "Who wrote 'Romeo and Juliet'?", "options": ["William Wordsworth", "William Shakespeare", "John Keats", "Leo Tolstoy"], "answer": "William Shakespeare", "image": "william.jpg"},
]

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz Application")
        self.master.geometry("900x650")

        self.question_index = 0
        self.score = 0
        self.time_left = 15
        self.timer_running = False
        self.answered_questions = {}
        self.user_answers = {}

        self.theme_button = ctk.CTkButton(master, text="Toggle Theme", command=self.toggle_theme)
        self.theme_button.place(x=750, y=20)

        self.question_counter = ctk.CTkLabel(master, text="", font=("Arial", 14))
        self.question_counter.place(x=20, y=20)

        self.question_label = ctk.CTkLabel(master, text="", font=("Arial", 20), wraplength=700, text_color="blue")
        self.question_label.place(relx=0.5, y=80, anchor="center")

        self.image_frame = ctk.CTkFrame(master, width=320, height=220, corner_radius=10)
        self.image_frame.place(relx=0.5, y=190, anchor="center")
        self.image_label = ctk.CTkLabel(self.image_frame, text="")
        self.image_label.pack()

        self.options = []
        for i in range(4):
            btn = ctk.CTkButton(master, text="", font=("Arial", 14), width=600, command=lambda i=i: self.check_answer(i))
            btn.place(relx=0.5, y=320 + i * 60, anchor="center")
            self.options.append(btn)

        self.timer_label = ctk.CTkLabel(master, text="", font=("Arial", 16))
        self.timer_label.place(x=750, y=60)

        self.progress_bar = ctk.CTkProgressBar(master, orientation="horizontal", width=200)
        self.progress_bar.set(1)
        self.progress_bar.place(x=650, y=90)

        self.next_button = ctk.CTkButton(master, text="Next", command=self.next_question)
        self.next_button.place(relx=0.8, y=570, anchor="center")

        self.prev_button = ctk.CTkButton(master, text="Previous", command=self.prev_question)
        self.prev_button.place(relx=0.2, y=570, anchor="center")

        self.shuffle_questions()
        self.display_question()

    def toggle_theme(self):
        mode = ctk.get_appearance_mode()
        ctk.set_appearance_mode("Dark" if mode == "Light" else "Light")

    def shuffle_questions(self):
        for q in questions:
            random.shuffle(q["options"])
        random.shuffle(questions)

    def display_question(self):
        self.time_left = 15
        self.timer_running = True
        self.update_timer()

        q = questions[self.question_index]
        self.question_label.configure(text=q["question"])
        for i, option in enumerate(q["options"]):
            self.options[i].configure(text=option, state="normal")

        self.question_counter.configure(text=f"Question {self.question_index + 1} of {len(questions)}")
        self.load_question_image(q["image"])

        self.timer_thread = threading.Thread(target=self.run_timer)
        self.timer_thread.daemon = True
        self.timer_thread.start()

    def load_question_image(self, path):
        if path and os.path.exists(path):
            img = Image.open(path)
            img = img.resize((300, 200), Image.Resampling.LANCZOS)
            self.photo = ImageTk.PhotoImage(img)
            self.image_label.configure(image=self.photo, text="")
        else:
            self.image_label.configure(image="", text="Image not found", font=("Arial", 14))

    def update_timer(self):
        self.timer_label.configure(text=f"Time left: {self.time_left}s")
        self.progress_bar.set(self.time_left / 15)

    def run_timer(self):
        while self.time_left > 0 and self.timer_running:
            time.sleep(1)
            self.time_left -= 1
            self.master.after(0, self.update_timer)
        if self.time_left == 0:
            self.master.after(0, self.auto_next)

    def check_answer(self, index):
        if self.question_index in self.answered_questions:
            return

        self.answered_questions[self.question_index] = True
        self.timer_running = False

        selected = self.options[index].cget("text")
        correct = questions[self.question_index]["answer"]
        self.user_answers[self.question_index] = selected

        if selected == correct:
            self.score += 1
            winsound.MessageBeep(winsound.MB_ICONASTERISK)
        else:
            winsound.MessageBeep(winsound.MB_ICONHAND)

        for btn in self.options:
            btn.configure(state="disabled")

        self.master.after(500, self.next_question)

    def auto_next(self):
        if self.question_index not in self.answered_questions:
            self.answered_questions[self.question_index] = True
            self.user_answers[self.question_index] = None
        self.next_question()

    def next_question(self):
        if self.question_index < len(questions) - 1:
            self.question_index += 1
            self.display_question()
        else:
            self.show_result()

    def prev_question(self):
        if self.question_index > 0:
            self.question_index -= 1
            self.display_question()

    def show_result(self):
        self.timer_running = False
        for widget in self.master.winfo_children():
            widget.place_forget()

        title_label = ctk.CTkLabel(self.master, text="Quiz Completed!", font=("Arial", 26, "bold"), text_color="#4169E1")
        title_label.place(relx=0.5, y=30, anchor="center")

        score_label = ctk.CTkLabel(self.master, text=f"Your Score: {self.score}/{len(questions)}", font=("Arial", 20), text_color="green")
        score_label.place(relx=0.5, y=70, anchor="center")

        y_offset = 120
        for i, q in enumerate(questions):
            correct = q["answer"]
            user_ans = self.user_answers.get(i)
            question_text = f"Q{i+1}: {q['question']}"
            correct_text = f"✔ Correct: {correct}"
            selected_text = f"✘ Your Answer: {user_ans}" if user_ans and user_ans != correct else ""

            q_label = ctk.CTkLabel(self.master, text=question_text, font=("Arial", 14))
            q_label.place(x=100, y=y_offset)

            correct_label = ctk.CTkLabel(self.master, text=correct_text, font=("Arial", 14), text_color="green")
            correct_label.place(x=120, y=y_offset + 25)

            if selected_text:
                selected_label = ctk.CTkLabel(self.master, text=selected_text, font=("Arial", 14), text_color="red")
                selected_label.place(x=120, y=y_offset + 50)
                y_offset += 90
            else:
                y_offset += 70

if __name__ == "__main__":
    root = ctk.CTk()
    app = QuizApp(root)
    root.mainloop()
