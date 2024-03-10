var start = confirm("acresimo de uma porcentagem em um valor");
if(start == true){
    var porcentagem = parseFloat(prompt("por favor digite um valor: "));
    var value = parseFloat(prompt("agora digite outro: "));
    var original = porcentagem;
    var divisão = original / 10;
    var uni = original + divisão;
    var value = value * uni;
    alert("aqui esta o valor com acresimo: " + value);
} else{
    alert("tudo bem o programa foi finalizado");
}
