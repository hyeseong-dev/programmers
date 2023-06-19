def solution(food_num, beverage_num):
    food_price = 12000
    beverage_price = 2000

    total_food_price = food_num * food_price
    total_beverage_price = beverage_num * beverage_price
    discount = (food_num // 10) * beverage_price

    return total_food_price + total_beverage_price - discount
