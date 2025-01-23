#include<stdio.h>

int main(){
    int arr1[5] = {2, 4, 6, 8, 0};
    int arr2[] = {1, 2, 3, 4, 5};
    int arr3[5];

    int mul1[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int mul2[][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int mul3[3][3];

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
    printf("*&arr1 = %d\n\n", *&arr1);
    for(i = 0; i < 5; i++)
        arr3[i] = arr1[i] + arr2[i];
    for(i = 0; i < 5; i++)
        printf("%d\t", arr3[i]);
    printf("\n");

    printf("arr3[5] = %d\n", arr3[5]);              // arr1[5] doesn't actually exists
    arr3[5] = 6;                                    // arrays have a fixed size and can't be modified in this way
    printf("arr3[5] = %d\n", arr3[5]);              // this then results in garbadge values being accessed insted

    for(i = 0; i < 5; i++)
        arr3[i] += (i + 1) * 2;
    for(i = 0; i < 6; i++)
        printf("%d\t", arr3[i]);                    // again, at arr3[5], we can see garbadge values being accessed
    printf("\n\n");



    for(i = 0; i < 3; i++){
        for(j = 0; j < 3; j++)
            mul3[i][j] = mul1[i][j] + mul2[i][j];
    }

    printf("mul3[0][0] = %d\n", mul3[0][0]);
    printf("mul3[0] = %d\n", mul3[0]);
    printf("mul3 = %d\n", mul3);
    printf("*mul3[0] = %d\n", *mul3[0]);
    printf("*mul3 = %d\n", *mul3);
    printf("**mul3 = %d\n", **mul3);
    printf("&mul3[0][0] = %d\n", &mul3[0][0]);
    printf("&mul3[0] = %d\n", &mul3[0]);
    printf("&mul3 = %d\n", &mul3);
    printf("mul3[0][0] = %d\n", mul3[0][0]);
    printf("mul3[0][0] = %d\n", mul3[0][0]);

    for(i = 0; i < 3; i++){
        for(j = 0; j < 3; j++)
            printf("%d\t", mul3[i][j]);
        printf("\n");
    }
    printf("\n");



    i = sizeof(arr1) / sizeof(arr1[0]);
    printf("sizeof(arr1) = %d\n", i);



    return 0;
}