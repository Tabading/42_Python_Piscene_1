
from give_bmi import give_bmi, apply_limit
height = [2.71, 1.15]
weight = [165.3, 38.4]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))

print("test leght err")
bmi = give_bmi([2.71, 1.15, 1], [165.3, 38.4])
print("test value err")
bmi = give_bmi([2.71, 1.15, "a"], [165.3, 38.4, 1])
print("test err")
bmi = give_bmi([], None)
