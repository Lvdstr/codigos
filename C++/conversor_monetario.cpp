#include <iostream>
#include <string>
using namespace std;

int main() {
    cout << "Conversor de moedas" << endl;
    string escolha;
    cout << "Primeiro, deseja converter dólar ou real?" << endl;
    cin >> escolha;
    
    if (!isalpha(escolha[0])) {
        cout << "Não vai não em" << endl;
    } else {
        if (escolha == "dolar") {
            int dolar;
            cout << "Digite o valor para converter: ";
            cin >> dolar;
            int conversao = dolar * 5;
            cout << dolar << " dólar(es) convertido(s) para real dá " << conversao << " real(ais)" << endl;
        } else if (escolha == "real") {
            int real;
            cout << "Digite o valor para converter: ";
            cin >> real;
            int conversao = real / 5;
            cout << real << " real(ais) convertido(s) para dólar dá " << conversao << " dólar(es)" << endl;
        }
    }
    return 0;
}