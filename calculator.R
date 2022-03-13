# This calculator was coded by Sami Elsayed

add <- function(x, y) {
    return(x + y)
}

subtract <- function(x, y) {
    return(x - y)
}

multiply <- function(x, y) {
    return(x * y)
}

divide <- function(x, y) {
    return(x / y)
}

# take input from the user
print("Select operator: ")
print("Addition (+)")
print("Subtraction (-)")
print("Multiplication (*)")
print("Division (/)")

choice = as.integer(readline(prompt = "Enter choice [+, -, *, /]: "))
num1 = as.integer(readline(prompt = "Enter first number: "))
num2 = as.integer(readline(prompt = "Enter second number: "))
operator <- switch(choice,
                   "+", 
                   "-", 
                   "*", 
                   "/")
result <- switch(choice, 
                 add(num1, num2), 
                 subtract(num1, num2), 
                 multiply(num1, num2), 
                 divide(num1, num2))

print(paste(num1, operator, num2, "=", result))
