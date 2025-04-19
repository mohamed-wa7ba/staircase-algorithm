🎯 Overview
A dynamic Python programming quiz that adapts to your skill level using the staircase algorithm. The quiz features 50+ multiple-choice questions across 5 difficulty levels.

✨ Features
Adaptive Difficulty: Questions get harder or easier based on your performance

50+ Questions: Covers basic to advanced Python concepts

Multiple Choice: Clear A/B/C/D answer format

Progress Tracking: Real-time scoring and level adjustment

Clean Interface: Easy-to-use command line interface

📂 File Structure
staircase-algorithm/
├── main.py            # Main quiz application
├── questions.py       # Question database (50+ questions)
└── README.md          # This documentation
🚀 Installation
Clone the repository:

git clone https://github.com/mohamed-wa7ba/staircase-algorithm.git
cd staircase-algorithm
Ensure you have Python 3.7+ installed:

python --version
🎮 How to Play
Run the quiz:


python main.py
Answer questions by entering A, B, C, or D

Type 'quit' to end the quiz at any time

🏆 Scoring System
Correct Answer: Move up one level (max level 5)

Wrong Answer: Move down one level (min level 1)

Final Score: Shows your correct/total answers ratio

Final Level: Your achieved skill level (1-5)

📊 Question Levels
Level	Difficulty	Topics Covered
1	Beginner	Basic syntax, data types, operators
2	Intermediate	Data structures, methods
3	Advanced	OOP, file handling, exceptions
4	Expert	Decorators, generators, context managers
5	Master	Metaclasses, concurrency, advanced patterns
🛠 Customization
To add your own questions:

Edit questions.py

Follow the existing format:

python
{
    "q": "Your question here?",
    "o": ["A. Option1", "B. Option2", "C. Option3", "D. Option4"],
    "a": "CorrectAnswer"  # or ["Multiple", "Correct", "Answers"]
}
🤝 Contributing
Contributions are welcome! Please:

Fork the repository

Create your feature branch

Commit your changes

Push to the branch

Open a pull request

📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

✉️ Contact
For questions or feedback:
A full stack devolper at @baianat

Email: mohamed@baianat.com

GitHub: @mohamed-wa7ba
