class Question:
    def __init__(self, text, choices, correct_choice):
        self.text = text
        self.choices = choices
        self.correct_choice = correct_choice

    def is_correct(self, user_choice):
        return user_choice == self.correct_choice

questions = [
    Question("What is the output of the following for loop and range() function",
             ["-2, -1, -3, -4", "-2, -1, 0, 1, 2, 3", "-2, -1, 0", "-2, -3, -4"],
             "-2, -1, -3, -4"),
    
    Question("Given the nested if-else below, what will be the value x when the code executed successfully",
             ["0", "4", "2", "3"],
             "3"),
    
    Question("Given the nested if-else structure below, what will be the value of x after code execution completes",
             ["2", "0", "3", "4"],
             "2"),
    
    Question("What is the value of the var after the for loop completes its execution",
             ["20", "21", "10", "30"],
             "20"),
    
    Question("What is the value of x",
             ["101", "99", "None of the above, this is an infinite loop", "100"],
             "100"),

    Question("What is the output of print(2%6)",
             ["ValueError", "0.33", "2"],
             "2"),

    Question("What is the output of the expression print(-18 // 4)",
             ["-4", "4", "-5", "5"],
             "-5"),

    Question("What is the output of print(2 ** 3 ** 2)",
             ["64", "512"],
             "512"),

    Question("What is the output of the following Python code\nx = 10\ny = 50\nif x ** 2 > 100 and y < 100:\n    print(x, y)",
             ["100 500", "10 50", "None"],
             "None"),

    Question("What is the output of the following code\nx = 100\ny = 50\nprint(x and y)",
             ["True", "100", "False", "50"],
             "50"),

    Question("What is the output of the following code\nx = 6\ny = 2\nprint(x ** y)\nprint(x // y)",
             ["66 0", "36 0", "66 3", "36 3"],
             "36 3"),

    Question("What is the output of the following addition (+) operator\na = [10, 20]\nb = a\nb += [30, 40]\nprint(a)\nprint(b)",
             ["[10, 20, 30, 40]", "[10, 20, 30, 40]", "[10, 20]", "[10, 20, 30, 40]"],
             "[10, 20, 30, 40]"),

    Question("What is the output of the following code\nprint(bool(0), bool(3.14159), bool(-3), bool(1.0+1j))",
             ["True True False True", "False True True True", "True True False True", "False True False True"],
             "False True False True"),

    Question("What is the value of the following Python Expression\nprint(36 / 4)",
             ["9.0", "9"],
             "9.0")
]

string_questions = [
    Question("Select the correct output of the following String operations\n\nstrOne = str('pynative')\nstrTwo = 'pynative'\nprint(strOne == strTwo)\nprint(strOne is strTwo",
             ["False False", "True True", "True False", "False True"],
             "True False"),

    Question("What is the output of the following string comparison\n\nprint('John' > 'Jhon')\nprint('Emma' < 'Emm')",
             ["True False", "False False", "False True", "True True"],
             "False False"),

    Question("Python does not support a character type; a single character is treated as strings of length one.\n\nTrue\nFalse",
             ["False", "True"],
             "True"),

    Question("Which method should I use to convert String 'welcome to the beautiful world of python' to 'Welcome To The Beautiful World Of Python'\n\ncapitalize()\ntitle()",
             ["capitalize()", "title()"],
             "title()"),

    Question("What is the output of the following code\n\nstr1 = 'My salary is 7000';\nstr2 = '7000'\n\nprint(str1.isdigit())\nprint(str2.isdigit())",
             ["False True", "True False", "True True", "False False"],
             "False True"),

    Question("Select the correct output of the following String operations\n\nstr1 = 'Welcome'\nprint(str1[:6] + ' PYnative')",
             ["Welcome PYnative", "WelcomPYnative", "Welcom PYnative", "WelcomePYnative"],
             "Welcome PYnative"),

    Question("What is the output of the following string operations\n\nstr = 'My salary is 7000';\nprint(str.isalnum())",
             ["True", "False"],
             "False"),

    Question("Guess the correct output of the following String operations\n\nstr1 = 'Welcome'\nprint(str1*2)",
             ["WelcomeWelcome", "TypeError unsupported operand type(s)"],
             "WelcomeWelcome"),

    Question("Choose the correct function to get the ASCII code of a character\n\nchar('char')\nord('char')\nascii('char')",
             ["char('char')", "ord('char')", "ascii('char')"],
             "ord('char')"),

    Question("Select the correct output of the following string operations\n\nmyString = 'pynative'\nstringList = ['abc', 'pynative', 'xyz']\n\nprint(stringList[1] == myString)\nprint(stringList[1] is myString)",
             ["True False", "False False", "True True", "False True"],
             "True True"),

    Question("Select the correct output of the following String operations\n\nstr1 = 'my isname isisis jameis isis bond';\nsub = 'is';\nprint(str1.count(sub, 4))",
             ["5", "6", "7"],
             "7")
]

def run_quiz():
    print("Python Beginner Quiz - If Else, Loops, Operators, and Expressions")

    score = 0

    for i, question in enumerate(questions + string_questions, start=1):
        print(f"\nQuestion {i}: {question.text}")
        for j, choice in enumerate(question.choices, start=1):
            print(f"{j}. {choice}")

        user_choice = input("Your choice (enter the number): ")

        if question.is_correct(user_choice):
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer is: {question.correct_choice}\n")

    print(f"You scored {score}/{len(questions + string_questions)}.")

if __name__ == "__main__":
    run_quiz()
print("Thank you for taking the quiz! Have a great day! :) ")
