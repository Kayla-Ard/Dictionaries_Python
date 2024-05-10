# create a function with a while loop that will add different shelf categories to your book shelf
# each category should have at least one value
# have at least one nested dictionary with at least 3 key value pairs
# if you're feelin saucy, make one of your nested dictionary values a list
# take some time to plan the structure of your dictionary
# have a nice time

def shelf_func():
    shelf = {}
    while True:
        shelf_addition = input('What would you like to add to the shelf? Enter "book" , "random item", or "picture frame: (Enter "quit" to end!)').lower()
        if shelf_addition == "book":
            genre_of_book = input("What is the genre of the book? ").title()
            name_of_book = input("What is the name of the book? ").title()
            shelf["Book"] = {"Genre": {genre_of_book}, "Title": {name_of_book}}
            print("This book was added to your shelf: ")
            print(shelf["Book"]) 
            
        elif shelf_addition == "random item":
            item = input("What item would you like to add to the shelf? ").title()
            meaning = input("What is the sentimental meaning of this item to you? ").title()
            shelf["Random Item"] = {"Item": {item}, "Meaning": {meaning}}
            print("This item was added to your shelf: ")
            print(shelf["Random Item"]) 
        
        elif shelf_addition == "picture frame":
            frame = input("What size is the picture frame you want to add to the shelf? Small, Medium, or Large? ").title()
            people = input("Who is in the picture in the frame? ").title()
            shelf["Picture Frame"] = {"Size of Frame": {frame}, "People in Picture": {people}}
            print("This picture frame was added to your shelf: ")
            print(shelf["Picture Frame"])

        elif shelf_addition == "quit":
            break

        else:
            print("Invalid response")
    
    print(shelf)
    
print(shelf_func())


