#include <stdio.h>

int main() {
  int ano_nasc;
  int ano_atual;
  
  printf("calculadora de idade");
  
  printf("digite o ano em que vc nasceu: ");
  scanf("%d", &ano_nasc);
  
  printf("agora digite o ano atual: ");
  scanf("%d", &ano_atual);
  
  int res = ano_atual - ano_nasc;
  
  if(ano_nasc < ano_atual){
    printf("sua idade eh %d anos",res);
  } else if (ano_nasc > ano_atual){
    printf("tem parada errado ai :⁠-⁠(")
  }
  return 0;
}
