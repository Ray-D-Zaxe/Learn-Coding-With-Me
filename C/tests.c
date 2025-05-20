int main()
{
    int a, i;
    scanf("%d\n", &a);
    int b[a];
    int c[a];
    for(i = 0; i < a; i++)
        c[i] = 0;
    for(i = 0; i < a; i++)
        scanf("%d\n", &b[i]);
    for(i = 0; i < a; i++){
        while(b[i] > 0){
            c[i] *= 10;
            c[i] += b[i] % 10;
            b /= 10;
        }
    }
    for(i = 0; i < a; i++)
        printf("%d\n", c[i]);
    return 0;
}