
def calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b == 0:
            return "Cannot divide by zero"
        return a / b


def agent(user_goal):
    print("Understanding goal:", user_goal)

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if "add" in user_goal.lower():
        operation = "add"
    elif "multiply" in user_goal.lower():
        operation = "multiply"
    elif "subtract" in user_goal.lower():
        operation = "subtract"
    elif "divide" in user_goal.lower():
        operation = "divide"
    else:
        return "I don't know how to perform this task."

    print("Action: Calling calculator tool")

    result = calculator(a, b, operation)

    print("Observation:", result)

    return f"Task completed. Result: {result}"


response = agent("multiply two numbers")
print(response)
