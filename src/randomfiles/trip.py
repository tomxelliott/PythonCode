def hotel_cost(nights):
    return 140 * nights
    
def plane_ride_cost(city):
    if city == "Charlotte":
        price = 183
    elif city == "Tampa":
        price = 220
    elif city == "Pittsburgh":
        price = 222
    elif city == "Los Angeles":
        price = 475
    return price
    
def rental_car_cost(days):
    cost = days * 40
    if days >= 7:
        cost -= 50
    elif days >= 3:
        cost -= 20
    return cost
    
def trip_cost(city, days, spending_money):
    total = rental_car_cost(days)
    total += hotel_cost(days)
    total += plane_ride_cost(city)
    total += spending_money
    return total
    
# sample input
print trip_cost("Los Angeles", 5, 600)
