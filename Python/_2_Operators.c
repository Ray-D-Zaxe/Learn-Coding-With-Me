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
    a % b;                  // returns 5



    // Unary Operators
    a;                      // returns 5
    a++;                    // returns 5
    a;                      // returns 6
    ++a;                    // returns 7

    a;                      // returns 7
    a--;                    // returns 7
    a;                      // returns 6
    --a;                    // returns 5
    a;                      // returns 5



    // Relational Operators
    //#include<stdbool.h>
    a == b;                 // returns 0
    a != b;                 // returns 1
    a < b;                  // returns 1
    a > b;                  // returns 0
    a <= b;                 // returns 1
    a >= b;                 // returns 0



    // Logical Operators
    (a == b) || (a <= b);    // returns 1
    (a == b) && (a <= b);   // returns 0
    !(a == b);              // returns 1
}