def rental_car_cost(d):
    discount = 50 if d >= 7 else 20 if (d >= 3) and not (d >= 7) else 0
    return d * 40 - discount

print(rental_car_cost(1),40)
print(rental_car_cost(4),140)
print(rental_car_cost(7),230)
print(rental_car_cost(8),270)