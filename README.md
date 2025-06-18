### Quiz App - Python CustomTkinter Project

**Quiz App** is a sleek, interactive quiz application built using **Python** and **CustomTkinter**. It presents multiple-choice questions with images, a timer, sound feedback, navigation, and a review mode — making it a great tool for fun learning or assessments.

---

## What Does the Program Do?

This application allows users to:

- Answer image-based multiple-choice questions
- Track time for each question (15 seconds)
- Switch between **Light** and **Dark** themes
- Navigate freely with **Next** and **Previous** buttons
- View a **progress bar timer**
- Receive sound cues for correct/wrong answers
- View a **final review** screen showing all questions, correct answers (✅ green), and wrong ones (❌ red)

---

## Main Window

- A title bar with a **"Toggle Theme"** button
- Current question displayed in the center
- Corresponding image (e.g., Mars for planet question)
- Four large answer buttons (click to select)
- Timer and visual progress bar on the top right
- Navigation buttons: **Next** and **Previous**

---

## Preview

### Quiz Window

![Screenshot 2025-06-18 151745](https://github.com/user-attachments/assets/0e7c4032-9883-4d9f-a700-582e340f87cf)

---

## Usage Guide

- Read the question and image.
- Choose the correct answer before the timer ends.
- Use Next or Previous to navigate.
- After the quiz ends, the app shows your score and a full answer review.

---

## Functional Modules

# Quiz System

- Supports multiple-choice questions
- Shuffles question order and options randomly

# Image Handling

- Each question displays a relevant image using Pillow

# Timer & Progress

- 15-second countdown with visual progress bar
- Automatic skip when time runs out

# Sound Feedback

- Windows beep for correct and incorrect answers

# Theme Toggle

- Easily switch between Light and Dark modes

# Review Mode

- End screen shows all questions and the correct answers
- Red for incorrect, Green for correct — clean and scrollable

---

## Tech Stack

- `Python 3.10+`

- `customtkinter` for GUI

- `Pillow` for image rendering

- `winsound` for sound feedback (Windows only)

- `threading` & `time` for timers

---

## Features

- Multiple-choice question system

- Image-based quiz UI

- Timer with progress bar

- Sound effects for correct/incorrect answers

- Light/Dark theme switching

- Previous/Next navigation

- Final review with color-coded feedback

---

## Possible Enhancements

- Add lifelines (50:50, skip, hint)

- Save user scores with a leaderboard

- Export results as a PDF

- Add support for audio questions

- Cross-platform sound support

---

## Features video

https://github.com/user-attachments/assets/c1456bcb-4add-4092-8cef-2e67894bee2d

---

## License

This project is licensed under the MIT License.

---

## Show Your Support

If you like this project, please Star it on GitHub! Contributions and feedback are welcome.

---



