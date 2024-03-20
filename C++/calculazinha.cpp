#include <iostream>

int main() {
    char operação;
    double num1, num2, resultado;

    std::cout << "primeiro escolha o operador matematico: +, -, *, / : ";
    std::cin >> operação;

    std::cout << "Digite o primeiro número: ";
    std::cin >> num1;
    
    std::cout << "Digite o segundo número: ";
    std::cin >> num2;

    switch(operação) {
        case '+':
            resultado = num1 + num2;
            break;
        case '-':
            resultado = num1 - num2;
            break;
        case '*':
            resultado = num1 * num2;
            break;
        case '/':
            if(num2 != 0) {
                resultado = num1 / num2;
            } else {
                std::cout << "Erro! Divisão por zero não é permitida." << std::endl;
                return 1; // Saída com erro
            }
            break;
        default:
            std::cout << "operação inválida!" << std::endl;
            return 1; // Saída com erro
    }

    std::cout << "Resultado: " << resultado << std::endl;

    return 0;
}