#include<stdio.h>

int main(){
    int arr[5] = {2, 4, 6, 8, 0};
    int mul[3][3] = {{2, 4, 6}, {8, 10, 12}, {14, 16, 18}};

    int i = 4, j = 5;
    int *w = &i;
    int *x = w, **y = &x, ***z = &y;



    printf("i : %%d = %d\n", i);                                // %d is a format specifier for integer
    printf("i : %%p = %p\n", i);                                // %p is a format specifier for addresses, in this case though it returns the value of (i) in hexadecimal
    printf("i : %%x = %x\n", i);                                // %x is a format specifier for hexadecimal
    printf("&i : %%x = %x\n", &i);                              // (&i) returns the address of (i), %x prints it in hexadecimal form
    printf("&i : %%d = %d\n", &i);                              // (&i) returns the address of (i), %d prints it in integer form
    printf("&i : %%p = %p\n\n", &i);                            // %p prints it in hexadecimal form

    printf("w : %%d = %d\t(*w = &i)\n", w);
    printf("w : %%p = %p\t(*w = &i)\n", w);
    printf("*w : %%d = %d\t\t(*w = &i)\n", *w);
    printf("&w : %%p = %p\t(*w = &i)\n\n", &w);

    printf("x : %%d = %d\t(*x = w)\n", x);
    printf("x : %%p = %p\t(*x = w)\n", x);
    printf("*x : %%d = %d\t\t(*x = w)\n", *x);
    printf("&x : %%p = %p\t(*x = w)\n\n", &x);
    
    printf("y : %%d = %d\t(**y = &x)\n", y);
    printf("y : %%p = %p\t(**y = &x)\n", y);
    printf("*y : %%d = %d\t(**y = &x)\n", *y);
    printf("**y : %%d = %d\t\t(**y = &x)\n", **y);
    printf("&y : %%p = %p\t(**y = &x)\n\n", &y);
    
    printf("z : %%d = %d\t(***z = &y)\n", z);
    printf("z : %%p = %p\t(***z = &y)\n", z);
    printf("*z : %%d = %d\t(***z = &y)\n", *z);
    printf("**z : %%d = %d\t(***z = &y)\n", **z);
    printf("***z : %%d = %d\t\t(***z = &y)\n\n", ***z);
    
    printf("(&i)\t\t: %d\n", (&i));
    printf("(&*&i)\t\t: %d\n", (&*&i));
    printf("(&*&*&i)\t: %d\n", (&*&*&i));
    printf("(*&i)\t\t: %d\n", (*&i));
    printf("(*&*&i)\t\t: %d\n", (*&*&i));
    printf("(*&*&*&i)\t: %d\n\n", (*&*&*&i));



    printf("arr[0] = %d\n\n", arr[0]);                          // returns 2, the value of the 1st element

    printf("arr = %d\n", arr);                                  // returns the base addres of (arr)
    printf("*arr = %d\n", *arr);                                // returns 2, the value of the first element
    printf("arr + 1 = %d\n", arr + 1);                          // returns the address of the next element, address increments by the size of int
    printf("*(arr + 1) = %d\n\n", *(arr + 1));                  // returns 4, the value of the next element
    /*
    arr         = *&arr         = &arr[0]
    *arr ...... = **&arr ...... = *(&arr[0]) ...... = 2
    arr + 1     = *&arr + 1     = &arr[0] + 1
    *(arr + 1)  = *(*&arr + 1)  = *(&arr[0] + 1) .. = 4
    */
    printf("&arr = %d\n", &arr);                                // returns the address of arr as an integer array of 5 elements
    printf("&arr + 1 = %d\n", &arr + 1);                        // returns the address after the address of last element of (arr) (i.e., arr[4]), treates this address like an int array of 5 elementss, increments the address by the size of int array of 5 elements
    printf("*(&arr + 1) - 1 = %d\n", *(&arr + 1) - 1);          // returns the address of the last element of the array, decrements the address (obtained by incrementing the original address by the size of an int array of size 5) by the size of int
    printf("*(*(&arr + 1) - 1) = %d\n\n", *(*(&arr + 1) - 1));  // returns the value of the last element
    


    printf("mul[0][0] = %d\n\n", mul[0][0]);                    // returns 2, the value of the 1st element

    printf("mul[0] = %d\n", mul[0]);                            // returns the base address of (mul[0][0])
    printf("*mul[0] = %d\n", *mul[0]);                          // returns 2, the value of the 1st element
    printf("mul[0] + 1 = %d\n", mul[0] + 1);                    // returns the address of the next element, by incrementing the address by the size of int
    printf("*(mul[0] + 1) = %d\n\n", *(mul[0] + 1));            // returns 4, the value of the next element
    /*
    *mul        = **&mul        = *&mul[0]          = mul[0]        = &mul[0][0]
    **mul ..... = ***&mul ..... = **&mul[0] ....... = *mul[0] ..... = *&mul[0][0] ..... = 2
    *mul + 1    = **&mul + 1    = *&mul[0] + 1      = mul[0] + 1    = &mul[0][0] + 1
    *(*mul + 1) = *(**&mul + 1) = *(*&mul[0] + 1) . = *(mul[0] + 1) = *(&mul[0][0] + 1) = 4
    */
    printf("mul = %d\n", mul);
    printf("mul + 1 = %d\n", mul + 1);
    printf("*(mul + 1) = %d\n", *(mul + 1));
    printf("**(mul + 1) = %d\n", **(mul + 1));
    printf("*mul + 1 = %d\n", *mul + 1);
    printf("*(*mul + 1) = %d\n\n", *(*mul + 1));

    printf("&mul[0][0] = %d\n", &mul[0][0]);
    printf("*&mul[0][0] = %d\n", *&mul[0][0]);
    printf("&mul[0][0] + 1 = %d\n", &mul[0][0] + 1);
    printf("*(&mul[0][0] + 1) = %d\n\n", *(&mul[0][0] + 1));

    printf("&mul[0] = %d\n", &mul[0]);
    printf("*&mul[0] = %d\n", *&mul[0]);
    printf("**&mul[0] = %d\n", **&mul[0]);
    printf("&mul[0] + 1 = %d\n", &mul[0] + 1);
    printf("*(&mul[0] + 1) = %d\n", *(&mul[0] + 1));
    printf("**(&mul[0] + 1) = %d\n", **(&mul[0] + 1));
    printf("*&mul[0] + 1 = %d\n", *&mul[0] + 1);
    printf("*(*&mul[0] + 1) = %d\n\n", *(*&mul[0] + 1));
    
    printf("&mul = %d\n", &mul);
    printf("*&mul = %d\n", *&mul);
    printf("***&mul = %d\n", ***&mul);
    printf("&mul + 1 = %d\n", &mul + 1);
    printf("*(&mul + 1) = %d\n", *(&mul + 1));
    printf("**(&mul + 1) = %d\n", **(&mul + 1));
    printf("***(&mul + 1) = %d\n", ***(&mul + 1));
    printf("*&mul + 1 = %d\n", *&mul + 1);
    printf("*(*&mul + 1) = %d\n", *(*&mul + 1));
    printf("**(*&mul + 1) = %d\n", **(*&mul + 1));

    return 0;
}