# Week 3 Pluralsight Content 

def banner_message(message, banner = "-"):
    
    line = banner * 11
    print(f"\n{line}")
    print(message)
    print(f"{line}\n")

banner_message("Mathmatical Operators")
print("Addition")
int_a = 3
int_b = 2
print(f"Input: '{int_a} + {int_b}'")
output = int_a + int_b
print(f"Output: {output}\n")


print("Subtraction")
int_a = 10
int_b = 5
print(f"Input: '{int_a} - {int_b}'")
output = int_a - int_b
print(f"Output: {output}\n")

print("Multiplication")
int_a = 3
int_b = 15
print(f"Input: '{int_a} * {int_b}'")
output = int_a * int_b
print(f"Output: {output}\n")

print("Division")
int_a = 30
int_b = 6
print(f"Input: '{int_a} / {int_b}'")
output = int_a / int_b
print(f"Output: {output}\n")

print("Exponent")
int_a = 2
int_b = 3
print(f"Input: '{int_a} ** {int_b}'")
output = int_a ** int_b
print(f"Output: {output}\n")

print("Negation")
int_a = -2
int_b = -3
print(f"Input: '{int_a} + {int_b}'")
output = int_a + int_b
print(f"Output: {output}\n")

banner_message("Integers and Floats")
int_a = 35
float_a = 30.5
print("There are only two types of integers")
print(f"Integer: {int_a}")
print(f"Float: {float_a}")
print()

banner_message("Order of Operations")
int_a = 5
int_b = 7
int_c = 3
print(f"Input: '({int_a} + {int_b}) * {int_c}' ")
print(f"-->      '{int_a + int_b} * {int_c}'")
output = (int_a + int_b) * int_c
print(f"Output: {output}\n")

print(f"Input: '{int_a} + {int_b} * {int_c}' ")
print(f"-->      '{int_a} + {int_b * int_c}'")
output = int_a + int_b * int_c
print(f"Output: {output}\n")

banner_message("Can as Swallow carry a coconut?")
weight_swallow = 60
weight_coconut = 1450
carry_weight_denominator = 3
can_carry = False
carry_message = f"Can the Swallow carry the coconut is: {can_carry}"

def get_carry_limit(weight_swallow, carry_weight_denominator):
    carry_limit = weight_swallow / carry_weight_denominator
    print(f"Carry limit is (Weight of Swallow: {weight_swallow}g's) / (Fractional of Swallows weight it can carry: {carry_weight_denominator}) || {weight_swallow}/{can_carry}")

    return carry_limit

def can_swallow_carry_coconut(weight_swallow, weight_coconut, carry_weight_denominator):
    can_carry = False
    carry_limit = get_carry_limit(weight_swallow, carry_weight_denominator)

    if(carry_limit > weight_coconut):
        can_carry = True
    print(f"Boolean for If the Swallow Can Carry is: {can_carry}")
    print(f"Amount needed to carry: {weight_coconut}g's")
    print(f"Can carry {carry_limit}g's")
    return can_carry

can_swallow_carry_coconut(weight_swallow, weight_coconut, carry_weight_denominator)


