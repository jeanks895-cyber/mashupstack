try:
    title = input("Enter book title: ")

    if not all(char.isalpha() or char.isspace() for char in title) or title.strip() == "":
        raise ValueError("Error: Book title must contain only alphabets and spaces.")

    year = input("Enter publication year: ")

    if not (year.isdigit() and len(year) == 4 and (year.startswith("19") or year.startswith("20"))):
        raise ValueError("Error: Publication year must be a 4-digit number starting with 19 or 20.")

    print("Book details accepted successfully!")
    print("Title:", title)
    print("Publication Year:", year)

except ValueError as e:
    print(e)

except Exception:
    print("An unexpected error occurred.")

finally:
    print("Program execution completed.")