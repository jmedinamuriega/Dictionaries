# 2. Advanced Data Handling with Python
# Objective:
# The aim of this assignment is to deepen your knowledge and practical skills in handling complex data structures using Python. You will work on real-world inspired tasks that require advanced manipulation of dictionaries, nested collections, and implementing custom functions for specific data processing needs.

# Task 1: Hotel Room Booking Tracker
# Enhance your ability to work with nested collections by developing a system to track room bookings for a hotel.

# Problem Statement:
# Develop a program that:

# Manages room bookings, where each room has details such as booking status (booked/available) and customer name.
# Implement functions to:
# Book a room (mark as booked and assign to a customer).
# Check-out a customer (mark room as available and remove customer name).
# Display the status of all rooms.
# Start with this initial hotel room structure:

hotel_rooms = {
    "101": {"status": "available", "customer": ""},
    "102": {"status": "booked", "customer": "John Doe"}
 }

attempts=0
rooms_managment=input("Hello, do you want to (a)dd or (r)emove a customer? ")
if rooms_managment.lower()=="a":
    room=input("Please introduce the number of the room: ")
    while True:
        try: 
            if hotel_rooms[room]["status"] == "available":
                attemps=0
                user=input("Please introduce the name of the customer")
                hotel_rooms[room]={"status":"booked","customer":user}
                break
            elif hotel_rooms[room]["status"] == "booked":
                print("Actually that room is booked!")
                break
        except KeyError:
            room=input("Please put a valid room number!")
            attempts+=1
            if attempts==4:
                print("too much attempts leaving")
                break
            else:
                continue
    
elif rooms_managment.lower()=="r":
    while True:
        try:
            room=input("Please introduce the number of the room")
            if hotel_rooms[room]["status"] == "booked":
                hotel_rooms[room]={"status":"available","customer":""}
                break
            elif hotel_rooms[room]["status"] == "available":
                print("Actually that room is available!")
                break
        except KeyError:
            room=input("Please put a valid room number!")
            attempts+=1
            if attempts==4:
                print("too much attempts leaving")
                break
            else:
                continue
for room, aviability in hotel_rooms.items():
    print(f"{room} is now {aviability['status']}")








# Task 2: E-commerce Product Search Feature
# Put your data handling and string manipulation skills to the test by creating a product search feature for an e-commerce platform.

# Problem Statement:
# Create a system that:

# Holds a dictionary of products where each product has attributes like name, category, and price.
# Implement a search function that allows searching for products by name, returning a list of matching products (case-insensitive search).
# Handle cases where no matches are found.
# Example product dictionary:

products = {
    "1": {"name": "Laptop", "category": "Electronics", "price": 800},
    "3": {"name": "Socks", "category": "Clothing", "price": 5},
    "4": {"name": "Hat", "category": "Accessories", "price": 15},
    "5": {"name": "Scarf", "category": "Accessories", "price": 10},
    "6": {"name": "Jacket", "category": "Outerwear", "price": 100},
    "7": {"name": "Sweater", "category": "Winterwear", "price": 50},
    "8": {"name": "Gloves", "category": "Accessories", "price": 15} 
}
def product_finder():
    i=0
    product_match=[]
    name = input("What are you searching for?")
    for product in products.values():
        if product["name"].lower() == name.lower():
            product_match.append(product["name"])
            print(f"here is the product!{product_match}")
    if len(product_match)==0:
        print("Here is not the item")
product_finder()