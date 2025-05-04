import streamlit as st
import math

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero!"
    return num1 / num2

def power(num, exponent):
    return num ** exponent

def square_root(num):
    if num < 0:
        return "Cannot calculate square root of a negative number"
    return math.sqrt(num)

def logarithm(num, base):
    if num <= 0 or base <= 0 or base == 1:
        return "Invalid input for logarithm"
    return math.log(num, base)

def natural_log(num):
    if num <= 0:
        return "Invalid input for natural logarithm"
    return math.log(num)

def exponential(num):
    return math.exp(num)

def sine(angle_degrees):
    return math.sin(math.radians(angle_degrees))

def cosine(angle_degrees):
    return math.cos(math.radians(angle_degrees))

def tangent(angle_degrees):
    return math.tan(math.radians(angle_degrees))

st.title("Scientific Calculator")

operation_type = st.selectbox(
    "Select Operation Type",
    ("Basic", "Scientific")
)

num1 = st.number_input("Enter first number", value=0.0)
num2_optional = None

if operation_type == "Basic":
    operation = st.selectbox(
        "Select Basic Operation",
        ("Add", "Subtract", "Multiply", "Divide")
    )
    num2 = st.number_input("Enter second number", value=0.0)
elif operation_type == "Scientific":
    operation = st.selectbox(
        "Select Scientific Operation",
        ("Power", "Square Root", "Logarithm (base y)", "Natural Log (ln)", "Exponential (e^x)", "Sine (sin)", "Cosine (cos)", "Tangent (tan)")
    )
    if operation not in ["Square Root", "Natural Log (ln)", "Exponential (e^x)"]:
        num2 = st.number_input("Enter second number", value=0.0)

if st.button("Calculate"):
    result = None
    if operation_type == "Basic":
        if operation == "Add":
            result = add(num1, num2)
        elif operation == "Subtract":
            result = subtract(num1, num2)
        elif operation == "Multiply":
            result = multiply(num1, num2)
        elif operation == "Divide":
            result = divide(num1, num2)
    elif operation_type == "Scientific":
        if operation == "Power":
            result = power(num1, num2)
        elif operation == "Square Root":
            result = square_root(num1)
        elif operation == "Logarithm (base y)":
            result = logarithm(num1, num2)
        elif operation == "Natural Log (ln)":
            result = natural_log(num1)
        elif operation == "Exponential (e^x)":
            result = exponential(num1)
        elif operation == "Sine (sin)":
            result = sine(num1)
        elif operation == "Cosine (cos)":
            result = cosine(num1)
        elif operation == "Tangent (tan)":
            result = tangent(num1)

    if result is not None:
        st.write(f"Result: {result}")