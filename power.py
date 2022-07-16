base = int(input("ENter number: "))
exponent = int(input("ENter number: "))

result = 1

while exponent != 0:
    result *= base
    exponent-=1

print("Answer = " + str(result))
