#include <stdio.h>

int main(){
    int number;
    printf("acresimo de 10 por cento no valor digitadl\n");
    printf("digite um valor:");
    scanf("%d", &number);
    int operação = number * (1 + 0.10);
    printf("aqui esta o valor com o acresimo: %d", operação);
    return 0;
}