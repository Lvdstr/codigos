function verifyletra(value){
  var lista = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"];
  if(isNaN(value) == false){
    console.log("o valor digitado é um numero");
    console.log("essa função so aceita letras");
  } 
  if(lista.includes(value)){
    console.log(value + ":é uma consoante");
  }else{
    console.log(value + ":é uma vogal");
  }
}

var letra = prompt("digite uma letra: ");
var chamada_func = verifyletra(letra);