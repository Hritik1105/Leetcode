// Java program to find factorial of a number using recursion
// https://www.geeksforgeeks.org/problems/factorial5739/1

class Solution {
    // Function to calculate factorial of a number.
    int factorial(int n) {
        if(n<=1) return 1;
        return n*factorial(n-1);
        
    }
}
