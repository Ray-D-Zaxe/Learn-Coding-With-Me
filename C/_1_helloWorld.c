#include<stdio.h>



// This is a single line comment

/* This is a multi line comment
before c99, released in 1999, only this was used to comment*/



void main()
{
    int i, j = 10, k, m, n = 8;

    printf("Hello World\n");
    
    
    
    char ch[100];
    printf("Hi, %s\n", fgets(ch, 100, stdin), printf("Enter your name: "));


    
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
    // when an integer is passed in %c, the character corresponding to the ASCII integer value is printed
    


    char chr = 'Hello', char_ar[] = "Hello";            // char is a single character and only returns the last character, char_ar is an array of characters
    printf("chr(%%c) = %c, char_ar(%%s) = %s\n", chr, char_ar);
    printf("chr(%%s) = %%s, char_ar(%%c) = %c\n", /*ch,*/ char_ar);



    int a = i = j = k = 9;                              // same value can be assigned in this fashion to multiple variables as lon as they are all initilized
    
    float f1 = 35e3, f2 = 22.0/7;                       // f2 is implicitly typecasted to float
    double d1 = 12E4;                                   // e or E is the exponential operator used to denote a number in scientific notation

    printf("f1 = %f, d1 = %lf\n", f1, d1);
    printf("f2 = %f\n", f2);                            // by default, shows upto 6 decimal places
    printf("f2 = %.1f\n", f2);                          // shows upto 1 decimal place, upto the number mentioned after %. and before f
    printf("f2 = %.2f\n", f2);                          // shows upto 2 decimal places, i.e, %.nf, where n is the number of decimal places
    printf("f2 = %.3f\n", f2);                          // shows upto 3 decimal places
    printf("f2 = %.0f\n", f2);                          // shows upto 0 decimal places

    f2 = (float) a;                                     // explicit typecasted to float



    const int const_int = 7;                            // constant integer, can't be changed



    // Booleans

    printf("%d\n", k == m);                             // returns 0, k is not equal to m
    printf("%d\n", k != m);                             // returns 1, k is not equal to m

    #include<stdbool.h>
    bool b1 = true;
    printf("%d\n", b1);                                 // returns 1
    printf("%d\n", false);                              // returns 0
}