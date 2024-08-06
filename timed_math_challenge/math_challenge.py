import random 
import time

operators = ["+", "-", "*"]
min_operand = 5
max_operand = 15
total_problems = 10

def generate_problem():
    left = random.randint(min_operand, max_operand)
    right = random.randint(min_operand, max_operand)
    operator = random.choice(operators)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer

wrong_answers = 0
input("Press Any key to Start!!")
print("------------------------")

start_time = time.time()
 
for i in range(total_problems):
    expr, answer = generate_problem()
    while True:
       guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
       if guess == str(answer):
            break
       wrong_answers += 1

end_time = time.time()
total_time = round(end_time - start_time , 2)

print("Nice Try!!")
print("----------")
print("You Finished in: ", total_time)