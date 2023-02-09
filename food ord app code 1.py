# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 14:11:36 2023

@author: Admin
"""

# Initialize food items with FoodID, Name, Quantity, Price, Discount, Stock
food_items = [
    {'FoodID': 1, 'Name': 'Tandoori Chicken', 'Quantity': '4 pieces', 'Price': 240, 'Discount': 10, 'Stock': 50},
    {'FoodID': 2, 'Name': 'Vegan Burger', 'Quantity': '1 Piece', 'Price': 320, 'Discount': 5, 'Stock': 20},
    {'FoodID': 3, 'Name': 'Truffle Cake', 'Quantity': '500gm', 'Price': 900, 'Discount': 15, 'Stock': 10},
]

# Initialize user database with Full Name, Phone Number, Email, Address, Password
user_db = []

# Function to generate next FoodID
def generate_foodid():
    return max([food_item['FoodID'] for food_item in food_items]) + 1

# Function to add new food item
def add_food_item(name, quantity, price, discount, stock):
    food_items.append({
        'FoodID': generate_foodid(),
        'Name': name,
        'Quantity': quantity,
        'Price': price,
        'Discount': discount,
        'Stock': stock
    })

# Function to edit food item
def edit_food_item(foodid, name, quantity, price, discount, stock):
    for food_item in food_items:
        if food_item['FoodID'] == foodid:
            food_item['Name'] = name
            food_item['Quantity'] = quantity
            food_item['Price'] = price
            food_item['Discount'] = discount
            food_item['Stock'] = stock
            break

# Function to view list of all food items
def view_food_items():
    for food_item in food_items:
        print(f'{food_item["FoodID"]}. {food_item["Name"]} ({food_item["Quantity"]}) [INR {food_item["Price"]}]')

# Function to remove food item
def remove_food_item(foodid):
    for i, food_item in enumerate(food_items):
        if food_item['FoodID'] == foodid:
            del food_items[i]
            break

# Function to register user
def register_user(full_name, phone_number, email, address, password):
    user_db.append({
        'Full Name': full_name,
        'Phone Number': phone_number,
        'Email': email,
        'Address': address,
        'Password': password
    })

# Function to login user
def login_user(email, password):
    for user in user_db:
        if user['Email'] == email and user['Password'] == password:
            return True
    return False

# Function to show menu for the user
def show_menu():
    print('---------------------------------------------')
    print('Food Menu')
    print('---------------------------------------------')
    for food_item in food_items:
        print(f'{food_item["FoodID"]}. {food_item["Name"]} ({food_item["Quantity"]})
