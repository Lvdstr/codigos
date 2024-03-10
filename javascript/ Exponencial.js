function exponencial(value){
  var potencia = prompt("exponencial de um numero: ");
  var resul = value ** potencia;
  return "resultado: " + number + " ** " + potencia + " = " + resul;
}
var inicial = confirm("esse programa calcula a potência de um numero,se deseja continuar digite ok:")
if(inicial == true){
	var number = parseInt(prompt("digite um numero: "));
	var func = exponencial(number);
	console.log(func)
}else{
	console.log("tudo bem,programa cancelado");
}
