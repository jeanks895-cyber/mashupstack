grocery_list = ["milk", "bread", "eggs"]

def add_item(item):
    grocery_list.append(item)

def remove_last_item():
    if grocery_list:
        grocery_list.pop()

def count_characters(items):
    return sum(len(item) for item in items)

add_item("butter")

remove_last_item()

for item in grocery_list:
    (lambda x: print("Item:", x))(item)

total_chars = count_characters(grocery_list)
print("Total characters in all item names:", total_chars)