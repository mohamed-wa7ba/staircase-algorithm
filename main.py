# Import required modules
import random
from questions import questions

# Define the main quiz class
class PythonProgrammingQuiz:
    def __init__(self):
        # Initialize quiz parameters
        self.current_level = 3  # Start at medium difficulty (level 3 out of 5)
        self.questions = questions  # Load questions from external file
        self.score = 0  # Track correct answers
        self.questions_answered = 0  # Track total questions attempted


    def get_question(self):
        #Select a random question from current difficulty level
        return random.choice(self.questions[self.current_level])


    def evaluate_answer(self, user_answer, correct_answer):
        #Check if user's answer matches correct answer(s)
        # Handle multiple possible correct answers
        if isinstance(correct_answer, list):
            return user_answer.upper() in [x.upper() for x in correct_answer]
        # Handle single correct answer
        return user_answer.upper() == correct_answer.upper()


    def run_quiz(self):
        #Main method to run the quiz interface
        # Display quiz introduction
        print("Python Programming Quiz")
        print("Choose the correct answer (A/B/C/D)")
        print("Type 'quit' to exit\n")

        # Main quiz loop
        while True:
            # Get current question
            question = self.get_question()

            # Display question and level
            print(f"\n[Level {self.current_level}] {question['q']}")

            # Display all answer options
            for option in question["o"]:
                print(option)

            # Get user input
            user_input = input("Your answer: ").strip()

            # Check for quit command
            if user_input.lower() == 'quit':
                break

            # Evaluate answer
            if self.evaluate_answer(user_input, question["a"]):
                print("✅ Correct!")
                self.score += 1
                # Increase level if not at maximum
                if self.current_level < 5:
                    self.current_level += 1
            else:
                print("Incorrect!")
                # Decrease level if not at minimum
                if self.current_level > 1:
                    self.current_level -= 1

            # Update and display stats
            self.questions_answered += 1
            print(f"Score: {self.score}/{self.questions_answered}")
            print(f"Current level: {self.current_level}/5")

        # Display final results
        print("\nQuiz completed!")
        print(f"Final score: {self.score}/{self.questions_answered}")
        print(f"Final level: {self.current_level}/5")


# Run the quiz if executed as main program
if __name__ == "__main__":
    quiz = PythonProgrammingQuiz()
    quiz.run_quiz()
