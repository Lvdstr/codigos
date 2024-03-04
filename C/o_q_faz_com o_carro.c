#include <stdio.h>

void repetirCodigo(int vezes) {
    for (int i = 0; i < vezes; i++) {
        int idade;
        
        printf("descubra o estado do carro\n");
        printf("\ndigite a idade do carro: ");
        scanf("%d", &idade);
        if(idade < 10){
            printf("o carro tem %d ano(s) entao ta novo ainda\n",idade);
        } else if (idade < 20){
               printf("o carro ta semi-novo,ja tem %d anos\n",idade);
          } else if (idade > 20 && idade < 30 ) {
              printf("joga essa porra fora po kkkk %d anos ja",idade);
          }
          else{
              printf("o carro ta velho chapa ta com %d anos ja",idade);
          }
            
            printf("\nEste código está sendo repetido pela %dª vez.\n", i + 1);
        }
    }

int main() {
    int quantidadeRepeticoes = 5;
    
    repetirCodigo(quantidadeRepeticoes);

    return 0;
}
