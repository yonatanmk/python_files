#city = "Los Angeles"
#days = 5
#spending_money = 600

print ("Please tell us what city you're traveling to from the following options:")
print ("Charlotte")
print ("Tampa")
print ("Pittsburgh")
print ("Los Angeles")
city_input = input('-->').lower()


print ("How many days will you be spending there?")
days_input = int(input('-->'))


print ("How much spending money would you want?")
spending_money_input = int(input('-->'))


def hotel_cost(nights):
    return 140 * nights

def plane_ride_cost(city):
    if city == "charlotte":
        return 183
    elif city == "tampa":
        return 220
    elif city == "pittsburgh":
        return 222
    elif city == "los angeles":
        return 475

def rental_car_cost (days):
    if days >= 7:
        return days * 40 - 50
    elif days >= 3:
        return days * 40 - 20
    else:
        return days * 40

def trip_cost(city, days, spending_money):
    return hotel_cost(days) + plane_ride_cost(city) + rental_car_cost (days) + spending_money


print (trip_cost(city_input, days_input, 600))
