import pandas as pd
import random
from faker import Faker

fake = Faker()

# List of actual pizza toppings
pizza_toppings = ['Pepperoni', 'Mushrooms', 'Onions', 'Sausage', 'Bacon', 'Extra Cheese', 'Black Olives', 'Green Peppers', 'Pineapple', 'Spinach']

# Generate pizza data
data = pd.DataFrame(columns=['Place Name', 'Pizza Size', 'Pizza Style', 'Pizza Sauce', 'Toppings', 'Price by Slice', 'Price by Size', 'Customer'])

# Generate data and populate the DataFrame
num_places = 10  # Number of pizza places
for _ in range(num_places):
    place_name = fake.last_name() + " Pizza"
    pizza_size = fake.random_element(elements=('sm', 'md', 'lg'))
    pizza_style = fake.random_element(elements=('NY', 'Sicilian', 'Chicago', 'Detroit', 'Deep Dish'))
    pizza_sauce = fake.random_element(elements=('tomato', 'white', 'pesto'))

    # Generate unique toppings
    num_toppings = random.randint(1, 5)
    toppings_list = []
    while len(toppings_list) < num_toppings:
        topping = random.choice(pizza_toppings)
        if topping not in toppings_list:
            toppings_list.append(topping)
    
    toppings = ', '.join(toppings_list)  # Convert the list to a comma-separated string

    price_slice = fake.random_int(min=5, max=10)
    price_size = price_slice * fake.random_int(min=2, max=4)
    customer = fake.name()
    
    # Access the data using .loc[]
    data.loc[len(data)] = {
        'Place Name': place_name,
        'Pizza Size': pizza_size,
        'Pizza Style': pizza_style,
        'Pizza Sauce': pizza_sauce,
        'Toppings': toppings,
        'Price by Slice': price_slice,
        'Price by Size': price_size,
        'Customer': customer
    }

# Save the DataFrame to an Excel file
data.to_excel('pizza_data.xlsx', index=False)
