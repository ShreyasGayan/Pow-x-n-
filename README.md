50. Pow(x, n)
Problem Statement

Implement pow(x, n), which calculates x raised to the power n (xⁿ).

Examples
Example 1
Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2
Input: x = 2.10000, n = 3
Output: 9.26100
Example 3
Input: x = 2.00000, n = -2
Output: 0.25000

Explanation:

2⁻² = 1 / 2² = 1 / 4 = 0.25
Approach

A naive solution would multiply x by itself n times, resulting in O(n) time complexity.

A more efficient approach is Binary Exponentiation (Exponentiation by Squaring).

Key Observations
If n is even:
xⁿ = (x²)^(n/2)
If n is odd:
xⁿ = x × xⁿ⁻¹
For negative powers:
x⁻ⁿ = 1 / xⁿ

By repeatedly squaring the base and halving the exponent, we reduce the number of operations from O(n) to O(log n).

Algorithm
If n is negative:
Replace x with 1/x
Convert n to positive
Initialize:
result = 1
While n > 0:
If n is odd, multiply result by x
Square x
Divide n by 2
Return result


Complexity Analysis
Time Complexity
O(log n)

The exponent is halved in every iteration.

Space Complexity
O(1)

Only a few variables are used.

Concepts Used
Binary Exponentiation
Exponentiation by Squaring
Bit Manipulation Logic
Mathematical Optimization
