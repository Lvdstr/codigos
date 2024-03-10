function calcularIMC(altura, peso) {
  if (altura > 0 && peso > 0) {
    var imc = peso / (altura * altura);
    return imc.toFixed(2);
  } else {
    return 'Altura e peso devem ser valores maiores doq zero chefe.';
  }
}

var altura = prompt('Digite sua altura em metros:');
var peso = prompt('Digite seu peso em quilogramas:');

var resultado = calcularIMC(parseFloat(altura), parseFloat(peso));

console.log('Seu IMC é: ' + resultado);