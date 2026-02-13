book1 = "Python Basics"
price1 = 450

book2 = "Data Science Intro"
price2 = 600

total = price1 + price2

receipt = """Book Store Receipt
Book Title: {} Price: ₹{}
Book Title: {} Price: ₹{}
Total Amount: ₹{}
Thank you for shopping with us!""".format(book1, price1, book2, price2, total)

print(receipt.upper())
