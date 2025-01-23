#include<stdio.h>

int main(){
    int i = 0, j = 0, k = 0;

    // While Loop, loops till the condition returns false (0)
    // while(condition) 1_line_code; code_outside_loop;
    // while(condition) {code_inside_loop} code_outside_loop;
    printf("while(i < 5) :(i = %d)(j = %d)\n", i, j);
    while(i < 5)
        printf("%d\t", i++, j++);

    printf("\n\tfinal value of (i) = %d\n\tloop run count = %d\n\n", i, j);

    j = 0;
    printf("while(i < 5) :(i = %d)(j = %d)\n", i, j);
    while(i)
        printf("%d\t", i--, j++);
    
    printf("\n\tfinal value of (i) = %d\n\tloop run count = %d\n\n", i, j);

    i = -5, j = 0;
    printf("while(i < 5) :(i = %d)(j = %d)\n", i, j);
    while(i)
        printf("%d\t", i++, j++);
    
    printf("\n\tfinal value of (i) = %d\n\tloop run count = %d\n\n", i, j);



    // Do While Loop, same as while loop
    // Do is executed once before the while condition is checked
    i = 0, j = 0;
    printf("while(i < 5) :(i = %d)(j = %d)\n", i);
    do
        printf("%d\t", i++, ++j);
    while(i < 5);

    printf("\n\tfinal value of (i) = %d\n\tloop run count = %d\n\n", i, j);



    // For Loop
    // for(initilize value, condition, change/updation in value) 1_line_code; code_outside_loop;
    // for(initilize value, condition, change/updation in value) {code_inside_loop} code_outside_loop;
    printf("for(i = 0, j = 0; i < 5; i++) :(i = %d)(j = %d)\n", i);
    for(i = 0, j = 0; i < 5; i++)
        printf("%d\t", i, j++);

    printf("\n\tfinal value of (i) = %d\n\tloop run count = %d\n\n", i, j);



    // For Loop with Continue
    printf("for(i = 0, j = 0; i < 5; i++) :(i = %d)(j = %d)\n", i);
    for(i = 0, j = 0; i < 5; i++){
        printf("%d", i, j++);
        if (i == 2)
            continue;
        printf("\t");
    }
    printf("\n\tfinal value of (i) = %d\n\tloop run count = %d\n\n", i, j);



    // For Loop with Break
    printf("for(i = 0, j = 0; i < 5; i++) :(i = %d)(j = %d)\n", i);
    for(i = 0, j = 0; i < 5; i++){
        printf("%d", i, j++);
        if (i == 2)
            break;
        printf("\t");
    }
    printf("\n\tfinal value of (i) = %d\n\tloop run count = %d\n\n", i, j);



    return 0;
}