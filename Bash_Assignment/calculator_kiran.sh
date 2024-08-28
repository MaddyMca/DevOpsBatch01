#!/bin/bash

# Prompt the user for two numbers and an operator
echo "Enter the 1st number:"
read number1
echo "Enter the 2nd number:"
read number2
echo "Enter the operator (+, -, *, /):"
read operator

# Perform the calculation based on the operator provided
case "$operator" in
    +)
        Result=$((number1 + number2))
        ;;
    -)
        Result=$((number1 - number2))
        ;;
    *)
        Result=$((number1 * number2))
        ;;
    /)
        Result=$((number1 / number2))
        ;;
    *)
        echo "Invalid operator"
        exit 1
        ;;
esac

# Display the result
echo "Result: $Result"