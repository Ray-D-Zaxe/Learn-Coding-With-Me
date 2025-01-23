#include<stdio.h>

int main(){
    int arr[5] = {2, 4, 6, 8, 0};
    int mul[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};

    int i, j;



    printf("arr1[0] = %d\n", arr1[0]);
    printf("arr1 = %d\n", arr1);
    printf("arr1 + 1 = %d\n", arr1 + 1);
    printf("*arr1 = %d\n", *arr1);
    printf("*(arr1 + 1) = %d\n", *(arr1 + 1));
    printf("&arr1[0] = %d\n", &arr1[0]);
    printf("&arr1[0] + 1 = %d\n", &arr1[0] + 1);
    printf("*&arr1[0] = %d\n", *&arr1[0]);
    printf("*(&arr1[0] + 1) = %d\n", *(&arr1[0] + 1));
    printf("&arr1 = %d\n", &arr1);
    printf("*&arr1 = %d\n", *&arr1);
    printf("**&arr1 = %d\n", **&arr1);
    printf("&arr1 + 1 = %d\n", &arr1 + 1);
    printf("*&arr1 + 1 = %d\n", *&arr1 + 1);
    printf("**&arr1 + 1 = %d\n", **&arr1 + 1);
    printf("*(*&arr1 + 1) = %d\n\n", *(*&arr1 + 1));

    printf("mul3[0][0] = %d\n", mul3[0][0]);
    printf("mul3[0] = %d\n", mul3[0]);
    printf("mul3 = %d\n", mul3);
    printf("*mul3[0] = %d\n", *mul3[0]);
    printf("*mul3 = %d\n", *mul3);
    printf("**mul3 = %d\n", **mul3);
    printf("&mul3[0][0] = %d\n", &mul3[0][0]);
    printf("&mul3[0] = %d\n", &mul3[0]);
    printf("&mul3 = %d\n", &mul3);
    printf("*&mul3[0][0] = %d\n", *&mul3[0][0]);
    printf("*&mul3[0] = %d\n", *&mul3[0]);
    printf("*&mul3 = %d\n", *&mul3);
    printf("**&mul3[0] = %d\n", **&mul3[0]);
    printf("**&mul3 = %d\n", **&mul3);
    printf("***&mul3 = %d\n\n", ***&mul3);
}