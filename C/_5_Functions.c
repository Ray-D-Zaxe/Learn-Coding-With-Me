#include<stdio.h>

typedef struct arr_ret{
    int a[5];
}arrayStruct;


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

void pass_by_value(int a, int b);                   // a and b are passed by value, i.e., changes in their values inside the function will not be reflected outside unless the values are returned

void pass_by_reference(int *a, int *b);             // a and b are passed by reference, i.e., a and b are pointers and hence changes in their values inside the function will be reflected outside

int ret_func_1(int a, int b);                       // the parameter names doesn't need to be the same as formal parameters

void arr_arg_func_1(int *);                         // arr_arg_fun_1(int x[5]) and arr_arg_fun_1(int x[]) also works, but arr_arg_fun_1(int x) and arr_arg_fun_1(int) does not

void arr_arg_func_2(int arr[], int size);           // This method can be used to pass size as a seprate parameter

void arr_arg_func_3(int *arr, int size);            // This method can also be used to pass size as a seprate parameter

int * ret_arr_arg_func_4(int *arr, int size);       // Returning an array through a pointer

arrayStruct ret_arr_struct_arg_func_5(int * a);     // Returning an arrya through structure, i.e., returning a structure

int w = 10, x = 20;                                 // Global variables
void scope_check(int w, int y);

// ----------------------------------------------------------------------------------------------------------------------------------------------
// Function call in main function
// ----------------------------------------------------------------------------------------------------------------------------------------------

void main(){
    bsc_prt_1();
    bsc_prt_2();
    printf("\n");

    
    
    arg_func_1(10, 20);
    arg_func_2(10, 20, 30);
    printf("\n");

    
    
    printf("ret_func_1(10, 20) = %d\n", ret_func_1(10, 20));
    int ar0 = ret_func_1(10, 20);
    printf("a = ret_func_1(10, 20) : %d\n", ar0);
    printf("\n");

    
    
    int ar[] = {10, 20, 30, 40, 50};
    arr_arg_func_1(ar);
    arr_arg_func_2(ar, 5);
    arr_arg_func_3(ar, 5);
    
    int * ar1 = ret_arr_arg_func_4(ar, 5);
    printf("int ar1[] = arr_arg_func_4(ar, 5) :\n");
    for(int i = 0; i < 5; i++)
        printf("ar1[%d] = %d\t", i, *(ar1 + i));
    printf("\n");

    arrayStruct ars = ret_arr_struct_arg_func_5(ar);
    for(int i = 0; i < 5; i++)
        printf("%d\t", ars.a[i]);
    printf("\n");
    printf("\n");



    int a = 7, b = 9;
    printf("Outside funtion :\na = %d, b = %d\n", a, b);
    pass_by_value(a, b);
    printf("Outside funtion :\na = %d, b = %d\n", a, b);
    pass_by_reference(&a, &b);
    printf("Outside funtion :\na = %d, b = %d\n", a, b);
    printf("\n");



    int y = 30, z = 40;
    printf("Outside funtion :\nw = %d,\tx = %d,\ty = %d,\tz = %d\n", w, x, y, z);
    ++w, ++x, y++, ++z;
    printf("Outside funtion :\nw = %d,\tx = %d,\ty = %d,\tz = %d\n", w, x, y, z);
    scope_check(w, y);                              // only the value of (x) changes since its a global variable and was not passed by value like the other global variable (w) or even the local variable (y)
    printf("Outside funtion :\nw = %d,\tx = %d,\ty = %d,\tz = %d\n", w, x, y, z);
}

// ----------------------------------------------------------------------------------------------------------------------------------------------
// Functions definition
// ----------------------------------------------------------------------------------------------------------------------------------------------

void bsc_prt_2(){
    printf("This is the bsc_prt_2()\n");
}

void arg_func_1(int a, int b){                      // a and b are formal parameters
    printf("arg_func_1(int a, int b) :");
    printf("a = %d, b = %d\n", a, b);
}

void arg_func_2(int a, int b, int c){
    printf("arg_func_2(int a, int b, int c) :");
    printf("a = %d, b = %d, c = %d\n", a, b, c);
}

int ret_func_1(int a, int b){
    printf("ret_func_1(int a, int b) :");
    return a + b;
}

void arr_arg_func_1(int a[]){                       // a[] is an array parameter
    printf("arr_arg_func_1(int a[]) :\n");
    for(int i = 0; i < 5; i++)
        printf("a[%d] = %d\t", i, a[i]);
    printf("\n");
}

void arr_arg_func_2(int a[], int b){                // a[] is an array parameter, and b is the size parameter
    printf("arr_arg_func_2(int a[], int b) :\n");
    for(int i = 0; i < b; i++)
        printf("a[%d] = %d\t", i, a[i]);
    printf("\n");
}

void arr_arg_func_3(int *a, int b){
    printf("arr_arg_func_3(int *a, int b) :\n");
    for(int i = 0; i < b; i++)
        printf("a[%d] = %d\t", i, a[i]);
    printf("\n");
}

int * ret_arr_arg_func_4(int *a, int b){
    printf("arr_arg_func_4(int a[], int b) :\n");
    for(int i = 0; i < b; i++)
        a[i] += i + 1;
    return a;
}

arrayStruct ret_arr_struct_arg_func_5(int * a){
    printf("ret_arr_struct_arg_func_5(int * a) :\n");
    arrayStruct array1;
    for(int i = 0; i < 5; i++)
        array1.a[i] = a[i] +  + 1;
    return array1;
}

void pass_by_value(int a, int b){
    printf("pass_by_value(int a, int b) :");
    a += b;
    b = a - b;
    a -= b;
    printf("(Inside funtion):\na = %d, b = %d\n", a, b);
}

void pass_by_reference(int *a, int *b){
    printf("pass_by_reference(int *a, int *b) :");
    *a += *b;
    *b = *a - *b;
    *a -= *b;
    printf("(Inside Funtion):\na = %d, b = %d\n", *a, *b);
}

void scope_check(int w, int y){
    printf("scope_check(int w, int y) :");
    ++w, ++x, ++y;                                  // can't access (z) as it is a local variable
    printf("(Inside Funtion):\nw = %d, x = %d, y = %d\n", w, x, y);
}