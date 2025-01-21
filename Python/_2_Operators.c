// Operators
#include<stdio.h>

void main(){
    int a, b;
    a = 5; b = 11;



    // Arithmetic Operators
    a + b;                  // returns 16
    a - b;                  // returns -6
    a * b;                  // returns 55
    a / b;                  // returns 0
    b / a;                  // returns 2
    b % a;                  // returns 1, remainder of b divided by a



    // Unary Operators
    a;                      // returns 5
    a++;                    // returns 5, returns a then increments a by 1
    a;                      // returns 6
    ++a;                    // returns 7, increments a by 1 and returns it

    a;                      // returns 7
    a--;                    // returns 7, returns a then decrements a by 1
    a;                      // returns 6
    --a;                    // returns 5, decrements a by 1 and returns it
    a;                      // returns 5



    // Relational Operators
    //#include<stdbool.h>
    a == b;                 // returns 0, checks if a is equal to b
    a != b;                 // returns 1, checks if a is not equal to b
    a < b;                  // returns 1
    a > b;                  // returns 0
    a <= b;                 // returns 1
    a >= b;                 // returns 0



    // Logical Operators
    (a == b) || (a <= b);   // returns 1, Logical OR
    (a == b) && (a <= b);   // returns 0, Logical AND
    !(a == b);              // returns 1, Logical NOT



    // Bitwise Operators
    a & b;                  // returns 1, bitwise AND
    a | b;                  // returns 15, bitwise OR
    a ^ b;                  // returns 14, bitwise XOR
    ~a;                     // returns -6, bitwise NOT
    a << 2;                 // returns 20, bitwise left shift
    a >> 1;                 // returns 2, bitwise right shift



    // Assignment Operators
    a = 5;                  // returns 5
    a += b;                 // returns 16, a = a + b
    a -= b;                 // returns 5, a = a - b
    a *= b;                 // returns 55, a = a * b
    a /= b;                 // returns 5, a = a / b
    a %= b;                 // returns 5, a = a % b
    a &= b;                 // returns 1, a = a & b
    a |= 7;                 // returns 7, a = a | 7
    a ^= b;                 // returns 12, a = a ^ b
    a <<= 2;                // returns 48, a = a << 2
    a >>= 1;                // returns 24, a = a >> 1



    // Ternary Operator
    // (condition) ? returns (code if condition true) : returns (code if condition false);
    (a > b) ? a : b;        // returns 24, a
}