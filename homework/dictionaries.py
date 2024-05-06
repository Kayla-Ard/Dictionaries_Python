# Lesson 1: Assignments | Dictionaries
# 1. Real-World Python Dictionary Applications
# Task 1: Restaurant Menu Update

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}
# Add a new category called "Beverages" with at least two items.
restaurant_menu_additions = {"Beverages": {"Beer": 5.00, "Mixed Drinks": 9.00}}
restaurant_menu.update(restaurant_menu_additions)
print(restaurant_menu)

# Update the price of "Steak" to 17.99.
restaurant_menu["Main Course"]["Steak"] = 17.99
print(restaurant_menu)

# Remove "Bruschetta" from "Starters".
del(restaurant_menu["Starters"]["Bruschetta"])
print(restaurant_menu)




# 2. Python Programming Challenges for Customer Service Data Handling
# Task 1: Customer Service Ticket Tracker
# Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.

# Problem Statement: Develop a program that:

# Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
# Implement functions to:
# Open a new service ticket.
# Update the status of an existing ticket.
# Display all tickets or filter by status.
# Initialize with some sample tickets and include functionality for additional ticket entry.

service_tickets = {
        "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
        "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
    }
id_ticket_num_counter = int(3)

def open_new_ticket(tickets, counter):
    id_ticket_num_counter = int(3)
    print("Let's get your information for your new ticket!")
    counter = "Ticket00"+str(id_ticket_num_counter)
    print("Your unique id ticket number has been created! It is " + counter)
    
    name = input("Enter first name to appear on new ticket: ").lower()
    if name == {name}.isalpha():
        print("Thank you! Your name was stored successfully!")
    else:
        print("Please enter a valid name consisting of letters only!")
    
    issue = input('Enter issue description: Either "login problem", "payment issue", or "lost ticket"').lower()
    if issue == "login problem" or issue == "payment issue" or issue == "lost ticket":
        print("Thank you! Your issue was stored successfully!")
    else:
        print("Please enter a valid response!")
    
    status = input('Enter status: (Either "open" or "closed"): ').lower()
    if status == "open" or status == "closed":
        print("Thank you! Your status was stored successfully!")
    else:
        print("Please enter a valid response!")
        

def update_status(tickets):
    pass
        
def display_tickets(tickets):
    pass

def track_service_tickets(tickets, counter):
    id_ticket_num_counter = int(2)
    print("Welcome to the Service Tickets App!")
    
    while True:
        action = input("""What would you like to do? Select an option from the menu: 
        
        Menu:
            "open" = To open a new service ticket         
            "update" = To update the status of an existing ticket 
            "display" = To display all tickets or filter by status           
            "done" = To exit the program    
            """)
        
        if action == "open":
            id_ticket_num_counter += int(1)
            open_new_ticket(tickets, counter)
            print(service_tickets = {counter : {"Customer": {name}, "Issue": {issue}, "Status": {status}}})        
            
        elif action == "update":
            update_status(tickets)
        
        elif action == "display":
            display_tickets(tickets)
            break
        else:
            print("Thanks for using the service tickets app. Good-bye!")
            
track_service_tickets(service_tickets, id_ticket_num_counter) 