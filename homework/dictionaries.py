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

def open_new_ticket(tickets, counter):
    print("Let's get your information for your new ticket!")
    counter = "Ticket00"+str(counter)
    print("Your unique id ticket number has been created! It is: " + counter)
    
    name = input("Enter first name to appear on new ticket: ").lower().strip()
    if name.isalpha() == True: 
        print("Thank you! Your name was stored successfully!")
    else:
        print("Please enter a valid name consisting of letters only!")
    
    issue = input('Enter issue description: (Either "Login Problem", "Payment Issue", or "Lost Ticket:" ').title().strip()
    if issue == "Login Problem" or issue == "Payment Issue" or issue == "Lost Ticket":
        print("Thank you! Your issue was stored successfully!")
    else:
        print("Please enter a valid response!")
    
    status = input('Enter status: (Either "open" or "closed"): ').lower()
    if status == "open" or status == "closed":
        print("Thank you! Your status was stored successfully!")
    
    else:
        print("Please enter a valid response!")
    
    tickets[counter] = {"Customers": name, "Issue": issue, "Status": status}

def update_status(tickets): #This function is not working!
    print("Let's get your status changed!")
    status = input("Enter you unique id ticket number you would like to change the status on: ").title()
    if status in tickets:
        if tickets[status]["Status"] == "Open":
            tickets[status]["Status"] = "Closed"
            print("Your status was updated successfully!")
        elif tickets[status]["Status"] == "Closed":
            tickets[status]["Status"] = "Open"
            print("Your status was updated successfully!")
    else:
        print("That unique id ticket number does not exist")
            
def display_tickets(tickets):
    display = input("""Choose an option from the menu below on which tickets you would like to view: 
    Menu:
        "1" = View all active tickets 
        "2" = View all tickets with a login problem issue
        "3" = View all tickets with a payment issue
        "4" = View all tickets with lost ticket issue 
        "5" = View all tickets with an open status
        "6" = View all tickets with a closed status 
        "7" = Return to Main Menu
        """)
    
    if display == "1":
        print(tickets)
        
    elif display == "2":
        for key in tickets:
            if tickets[key]["Issue"] == "Login Problem":
                print(f"Here are all tickets with Login Problems:\nTicket Number: {key} Customer Name: {tickets[key]["Customer"]} ")
            
    elif display == "3":
        for key in tickets:
            if tickets[key]["Issue"] == "Payment Issue":
                print(f"Here are all tickets with Payment Issues:\nTicket Number: {key} Customer Name: {tickets[key]["Customer"]} ")
    
    elif display == "4":
        for key in tickets:
            if tickets[key]["Issue"] == "Lost Ticket":
                print(f"Here are all tickets with Lost Ticket Issues:\nTicket Number: {key} Customer Name: {tickets[key]["Customer"]} ")
    
    elif display == "5":
        for key in tickets:
            if tickets[key]["Status"] == "Open":
                print(F"Here are all tickets with an Open Status:\nTicket Number: {key} Customer Name: {tickets[key]["Customer"]} ")
    
    elif display == "6":
        for key in tickets:
            if tickets[key]["Status"] == "Closed":
                print(F"Here are all tickets with a Closed Status:\nTicket Number: {key} Customer Name: {tickets[key]["Customer"]} ")
    
    elif display == "7":
        print("Returning to Main Menu")
        
    else:
        print("You entered an invalid option!")

def track_service_tickets():
    service_tickets = {
        "Ticket001": {"Customer": "Alice", "Issue": "Login Problem", "Status": "Open"},
        "Ticket002": {"Customer": "Bob", "Issue": "Payment Issue", "Status": "Closed"}
    }
    id_ticket_num_counter = 3
    print("Welcome to the Service Tickets App!")
    
    while True:
        action = input("""What would you like to do? Select an option from the menu: 
        
        Menu:
            "open" = To open a new service ticket         
            "update" = To update the status of an existing ticket 
            "display" = To display all tickets or filter by status           
            "done" = To exit the program    
            """).lower()
        
        if action == "open":
            open_new_ticket(service_tickets, id_ticket_num_counter)
            id_ticket_num_counter += 1
            print(service_tickets)
            
        elif action == "update":
            update_status(service_tickets)
        
        elif action == "display":
            display_tickets(service_tickets)
        
        elif action == "done":
            print("Thanks for using the service tickets app. Good-bye!")
            break
        
        else:
            print("Invalid response!")
    
    print(service_tickets)       
track_service_tickets() 