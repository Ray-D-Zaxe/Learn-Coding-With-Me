#include<stdio.h>

int main(){
    int a = 5, b = 11, c = 15, d;



    (a < b) ? printf("a < b\n") : printf("a > b\n") ;

    d = (a < b) ? a : b;



    if (a < b) printf("1");
    if (a < c) printf("2");
    if (c < b) printf("3");
    else if (a < b) printf("4\n");



    if ((a < b) && (a < c)) printf("a is the min value.\n");
    else if ((b < a) && (b < c)){
        printf("b is the min value.");
        printf("\n");
    }
    else
        printf("c is the min value.\n");
    
    printf("if else-if ladder completed.\n");



    printf("Enter a no. : "); scanf("%d", &a);

    switch (a)
    {
    case 1:
        printf("1\n");
        break;
    case 2:                             // If this is executed then all the subsciquent cases except for defalut case
        printf("2\n");                  // Will also be executed till it finds a break statement
    case 3:
        printf("3\n");
    default:
        printf("Invalid Input!!!\n");
        break;
    }
    printf("Switch-Case statement over.\n");



    return 0;
}