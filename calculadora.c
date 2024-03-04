#include <stdio.h>
#include <string.h>
#include <math.h>

int main(){
    int value_one;
    int value_two;
    char resposta[10];
    
    printf("bem vindo a versão da caclulazinha em c ");
    printf("\ndigite o primeiro valor:");
    scanf("%d", &value_one);
    printf("digite o segundo valor:");
    scanf("%d", &value_two);
    printf("essas são as operaçoes disponiveis:\n");
    printf("+ = soma\n- = subtrair\n* = multiplicar\n");
    printf("/ = dividir\n‰ = modular\n** = potencia:");
    scanf("%s", resposta);
    
    if(strcmp(resposta, "+") == 0){
        int operacao = value_one + value_two;
        printf("aqui esta o resultado da operacao\n");
        printf("%d %s %d = %d", value_one, resposta, value_two, operacao);
        printf("\nfim do programa (⁠•⁠‿⁠•⁠)");
    } 
    
    else if(strcmp(resposta, "-") == 0){
        int operacao = value_one - value_two;
        printf("aqui esta o resultado da operacao\n");
        printf("%d %s %d = %d", value_one, resposta, value_two, operacao);
        printf("\nfim do programa (⁠•⁠‿⁠•⁠)");
    } 
    
    else if (strcmp(resposta, "*") == 0){
        int operacao = value_one * value_two;
        printf("aqui esta o resultado da operacao\n");
        printf("%d %s %d = %d", value_one, resposta, value_two, operacao);
        printf("\nfim do programa (⁠•⁠‿⁠•⁠)");
    } 
    
    else if (strcmp(resposta, "/") == 0){
        int operacao = value_one / value_two;
        printf("aqui esta o resultado da operacao\n");
        printf("%d %s %d = %d", value_one, resposta, value_two, operacao);
        printf("\nfim do programa (⁠•⁠‿⁠•⁠)");
    } 
    
    else if (strcmp(resposta, "%") == 0){
        int operacao = value_one % value_two;
        printf("aqui esta o resultado da operacao\n");
        printf("%d %s %d = %d", value_one, resposta, value_two, operacao);
        printf("\nfim do programa (⁠•⁠‿⁠•⁠)");
    }
    
    else if (strcmp(resposta, "**") == 0){
        int operacao = pow(value_one, value_two);
        printf("aqui esta o resultado da operacao\n");
        printf("%d %s %d = %d", value_one, resposta, value_two, operacao);
        printf("\nfim do programa (⁠•⁠‿⁠•⁠)");
    }

    return 0;
}