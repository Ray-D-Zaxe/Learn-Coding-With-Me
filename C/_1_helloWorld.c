#include<stdio.h>



// This is a single line comment

/* This is a multi line comment
before c99, released in 1999, only this was used to comment*/



void main()
{
    int i, j = 10, k, m, n = 8;

    printf("Hello World\n");
    
    
    
    printf("Enter a number: ");
    scanf("%d", &i);
    
    //printf(i);                                        Does nothing, exits the program
    printf("The number is %d\n", i);


    
    printf("n = %d\n", n);
    printf("%d, %d, %d\n", i, j, k, m, ++n);            /* the values of i and j are printed successfully, k returns a grabadge value,
                                                        m does nothing, the value of n is incremented */
    printf("%d\n");                                     // prints garbadge value
    printf("n = %d\n", n);                              // the value of n was incremented by 1 previously



    printf("%%d = %d, %%c = %c, %%c = %c, %%d = %d, %%f = %f\n", 7, 7, 'A', 'A', 'a');
                                                        // Format specifiers can be used to print values directly, using %d, %c, %f etc

    

    int a = i = j = k = 9;                              // same value can be assigned in this fashion to multiple variables as lon as they are all initilized
    
}