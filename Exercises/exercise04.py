## Exercise 4: Primitive Quiz - 30 Marks
##In this exercise, you'll create a simple program that asks the user a question, evaluates their answer, and provides feedback.
primative_quiz={"United Kingdom": "London",
                "Germany": "Berlin",
                "Italy": "Rome", 
                "France": "Paris",
                "Spain": "Madrid",
                "Russia": "Moscow",
                "Greece": "Athens",
                "Portugal": "Lisbon",
                "Netherlands": "Amsterdam",
                "Montenegro": "Podgorica",
}
for country, capital in primative_quiz.items():
    while True:
        answer=input(f"What is the capital of {country}:?")
        answer=answer.lower()

        if answer==capital.lower():
            print("Correct!")
            break
        else:
            print("Incorrect, Please try")

