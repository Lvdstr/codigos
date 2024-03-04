#include <stdio.h>

void repetirCodigo(int vezes) {//#1
    for (int i = 0; i < vezes; i++) {//#2
        // Seu código a ser repetido #3
        printf("Este código está sendo repetido pela %dª vez.\n", i + 1);//#4
    }
}

int main() {//#5
    int quantidadeRepeticoes = 10;//#6
    
    repetirCodigo(quantidadeRepeticoes);//#7

    return 0;
}

/*

#1 aqui é a declaração da função repetircodigo que tem o parametro int vezes,o tipo void indica que a funcão não retorna nenhum valor.
#2 esse lop for inicia a variavel i em 0,e executa o codigo se ele for menor que vezes(no caso ele executa o codigo enquanto ele for menor que 10 que esta contido em quantidadeRepeticoes mas tudo bem) e icrementa i apos cada iteração.
#3 aqui fica o codigo que vai ser repetido.
#4 dentro do loop tem um print que indica a contagem atual de iteracoes.
#5 inicia a funcao main que é o inicio do programa
#6 declaracao de variavel e valor dela.que no caso é a quantidade de vezes que o codigo é repetido
#7 chama a funcão repetircodigo passando o quantidadeRepeticoes como argumento
*/