try:
    name = input("Enter your name: ")
    feedback = input("Enter your feedback: ")

    if name.strip() == "" or feedback.strip() == "":
        raise ValueError("Error: Name and feedback cannot be empty.")

    print("\nThank you for your feedback!")
    print("Name:", name)
    print("Feedback:", feedback)

except ValueError as e:
    print(e)

except Exception:
    print("An unexpected error occurred.")

finally:
    print("\nFeedback system closed.")