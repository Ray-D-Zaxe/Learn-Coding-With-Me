#include<stdio.h>

int main(){
    int arr[5] = {2, 4, 6, 8, 0};
    int mul[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};

    int i, j;



    printf("arr[0] = %d\n\n", arr[0]);

    printf("arr = %d\n", arr);
    printf("arr + 1 = %d\n", arr + 1);
    printf("*arr = %d\n", *arr);
    printf("*(arr + 1) = %d\n\n", *(arr + 1));
    
    printf("&arr[0] = %d\n", &arr[0]);
    printf("&arr[0] + 1 = %d\n", &arr[0] + 1);
    printf("*&arr[0] = %d\n", *&arr[0]);
    printf("*(&arr[0] + 1) = %d\n\n", *(&arr[0] + 1));

    printf("&arr = %d\n", &arr);
    printf("(&arr + 1) = %d\n", (&arr + 1));
    printf("*&arr = %d\n", *&arr);
    printf("*(&arr + 1) = %d\n", *(*(&arr + 1) - 1));
    printf("*(&arr + 1) = %d\n", *(&arr + 1));
    printf("*&arr + 1 = %d\n", *&arr + 1);
    printf("**(&arr + 1) = %d\n", **(&arr + 1));
    printf("**&arr = %d\n", **&arr);
    printf("*(*&arr + 1) = %d\n\n", *(*&arr + 1));


/*
    printf("mul[0][0] = %d\n", mul[0][0]);
    printf("mul[0] = %d\n", mul[0]);
    printf("mul = %d\n", mul);
    printf("*mul[0] = %d\n", *mul[0]);
    printf("*mul = %d\n", *mul);
    printf("**mul = %d\n", **mul);
    printf("&mul[0][0] = %d\n", &mul[0][0]);
    printf("&mul[0] = %d\n", &mul[0]);
    printf("&mul = %d\n", &mul);
    printf("*&mul[0][0] = %d\n", *&mul[0][0]);
    printf("*&mul[0] = %d\n", *&mul[0]);
    printf("*&mul = %d\n", *&mul);
    printf("**&mul[0] = %d\n", **&mul[0]);
    printf("**&mul = %d\n", **&mul);
    printf("***&mul = %d\n\n", ***&mul);
*/
    return 0;
}