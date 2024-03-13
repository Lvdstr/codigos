#include<stdio.h>

int main(){
    int valor;
    int desconto;
    
    printf("calcule um valor com desconto\n");
    
    printf("informe um valor:");
    scanf("%d", &valor);
    
    printf("agora a porcentagem de desconto:");
    scanf("%d", &desconto);

    int valor_com_desconto = valor - (valor * desconto / 100);
    
    printf("\nesse é o valor com desconto: %d", valor_com_desconto);
    return 0;
}
