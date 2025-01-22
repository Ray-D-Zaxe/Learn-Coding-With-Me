#include<stdio.h>

// Functions
void bsc_prt_1(){                                   // Functions without declaration must be defined before their function call
    printf("This is the bsc_prt_1()\n");
}

// ----------------------------------------------------------------------------------------------------------------------------------------------
// Functions declaration/prototyping
// ----------------------------------------------------------------------------------------------------------------------------------------------

void bsc_prt_2();

void arg_func_1(int x, int y);                      // x and y are parameters types/list, the focus is on the type and not the actual name

void arg_func_2(int, int y, int);                   // only mentioning the data type is enough as well

int ret_func_1(int a, int b);                       // the parameter names doesn't need to be the same as formal parameters

// ----------------------------------------------------------------------------------------------------------------------------------------------
// Function call in main function
// ----------------------------------------------------------------------------------------------------------------------------------------------

void main(){
    bsc_prt_1();
    bsc_prt_2();

    arg_func_1(10, 20);
    arg_func_2(10, 20, 30);

    printf("ret_func_1(10, 20) = %d\n", ret_func_1(10, 20));
    int a = ret_func_1(10, 20);
    printf("a = ret_func_1(10, 20) : %d\n", a);
}

// ----------------------------------------------------------------------------------------------------------------------------------------------
// Functions definition
// ----------------------------------------------------------------------------------------------------------------------------------------------

void bsc_prt_2(){
    printf("This is the bsc_prt_2()\n");
}

void arg_func_1(int a, int b){
    printf("a = %d, b = %d\n", a, b);
}

void arg_func_2(int a, int b, int c){
    printf("a = %d, b = %d, c = %d\n", a, b, c);
}

int ret_func_1(int a, int b){
    return a + b;
}