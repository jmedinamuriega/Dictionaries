# 3. Python Programming Challenges for Customer Service Data Handling
# Objective:
# This assignment is designed to test and enhance your Python programming skills, focusing on real-world applications in customer service data management. You will practice correcting code, organizing customer data, and implementing a feedback system using Python dictionaries.

# Task 1: Customer Service Ticket Tracker
# Demonstrate your ability to use nested collections and loops by creating a system to 
# track customer service tickets.

# Problem Statement:
# Develop a program that:

# Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
# Implement functions to:
# Open a new service ticket.
# Update the status of an existing ticket.
# Display all tickets or filter by status.
# Initialize with some sample tickets and include functionality for additional ticket entry.
# Example ticket structure:

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}   

user_decition=input('''What you want to do?
                    1-Open a new service ticket.
                    2-Update the status of an existing ticket.
                    3-Display all tickets or filter by status.
                    ''')

if user_decition=="1":
    number_of_ticket=len(service_tickets)+1
    ticket="Ticket00"+str(number_of_ticket)
    print(ticket)
    customer=input("please introduce the name of the costumer")
    issue=input("Please introduce the issue")
    status="open"
    service_tickets[ticket]={"Customer": customer, "Issue":issue,"Status":status }
elif user_decition=="2":
    try:
        ticket_num=input("Introduce the number of ticket, remember the 0")
        ticket="Ticket"+str(ticket_num)
        decition=input("Want to (c)lose or re (o)pen a ticket?")
        if decition=="c":
            service_tickets[ticket]["status"]="closed"
            print(service_tickets)
        elif decition=="o":
            service_tickets[ticket]["status"]="open"
    except KeyError:
        print("Introduce a valid ticket")
elif user_decition=="3":
   for ticket_number, ticket_info in service_tickets.items():
    print(f"Ticket Number: {ticket_number}, Status: {ticket_info['Status']}") 
    
    

# 4. Python Essentials for Business Analytics
# Objective:
# This assignment aims to strengthen your proficiency in Python by tackling challenges that simulate real-world business analytics scenarios. You'll practice copying dictionaries, utilizing built-in methods, managing nested collections, and implementing try-except blocks for error handling.

# Task 1: Sales Data Cloning and Modification
# Gain practical experience in copying dictionaries and modifying data, crucial skills in data analysis.

# Problem Statement:
# You have a dictionary representing weekly sales data for a store. Your task is to create a deep copy of this data and update the sales figures for a specific week.

# Given Sales Data:

weekly_sales = {
"Week 1": {"Electronics": 12000, "Clothing": 5000, "Groceries": 7000},
"Week 2": {"Electronics": 15000, "Clothing": 6000, "Groceries": 8000}
}

import copy

# Original data
weekly_sales = {
    "Week 1": {"Electronics": 12000, "Clothing": 5000, "Groceries": 7000},
    "Week 2": {"Electronics": 15000, "Clothing": 6000, "Groceries": 8000}
}

weekly_sales_copy = copy.deepcopy(weekly_sales)
weekly_sales_copy["Week 2"]["Electronics"] = 18000
print(weekly_sales_copy)



# Create a deep copy of weekly_sales.
# Update the sales figure for "Electronics" in "Week 2" to 18000 in the copied data.