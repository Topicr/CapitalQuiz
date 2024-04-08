
# Guess the capital

# Questions
questions = [
    {
        "question": "What is the capital of Italy?",
        "options": ["A: Rome", "B: Florence", "C: Milan", "D: Naples"],
        "answer": "A"
    },

    {
        "question": "What is the capital of Spain",
        "options": ["A: Valencia", "B: Bilbao", "C: Barcelona", "D: Madrid"],
        "answer": "D"
    },

    {
        "question": "What is the capital of Sweden",
        "options": ["A: Gothenburg", "B: Stockholm", "C: Malmö", "D: Rinkeby"],
        "answer": "B"
    },

    {
        "question": "What is the capital of Germany",
        "options": ["A: Frankfurt", "B: Hamburg", "C: Berlin", "D: Munich"],
        "answer": "C"
    },

    {
        "question": "What is the capital of England?",
        "options": ["A: Wales", "B: Manchester", "C: Birmingham", "D: London"],
        "answer": "D"
    },

    {
        "question": "What is the capital of France?",
        "options": ["A: Lyon", "B: Montpellier", "C: Nantes", "D: Paris"],
        "answer": "D"
    },

    {
        "question": "What is the capital of Norway?",
        "options": ["A: Oslo", "B: Drammen", "C: Sandefjord", "D: Fredrikstad"],
        "answer": "A"
    },

    {
        "question": "What is the capital of Poland?",
        "options": ["A: Suwałki", "B: Warsaw", "C: Gdansk", "D: Wroclaw"],
        "answer": "B"
    },
    
    {
        "question": "What is the capital of Austria?",
        "options": ["A: Salzburg", "B: Graz", "C: Vienna", "D: Linz"],
        "answer": "C"
    },

    {
        "question": "What is the capital of Finland?",
        "options": ["A: Turku", "B: Helsinki", "C: Kotka", "D: Tampere"],
        "answer": "B"
    }
]

# This function will define the quiz code on launch
def run_quiz(questions):
    score = 0  # Initialize score to 0 and create a variable "score" to store the value of correct answers

    # Loop through all the questions. This will follow all the questions above until finished
    for question in questions:
        print("\n" + question["question"])  # Print the question
        for option in question["options"]:
            print(option)  # Print all the answer options

        # Get the user's answer
        user_answer = input("Enter your answer (A, B, C, or D): ").strip().upper()

        # Check if the user's answer is correct
        if user_answer == question["answer"]:
            print("Correct!")
            score += 1  # Increment score if correct
        else:
            print("Wrong answer.")

    # Print the final score from the stored variable
    print(f"\nYou got {score} out of {len(questions)} questions correct!")


# Run
run_quiz(questions)


