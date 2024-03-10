var ano_atual = parseFloat(prompt("digita em que ano nois tamo:"));
var idade_atual = parseFloat(prompt("blz agora digita quantos ano tu tem agora: "));
var ano_nascimento = ano_atual - idade_atual;
    
if(ano_nascimento <= 10){
    alert("você é da geração alpha");
}else if(ano_nascimento <= 27){
    alert("você é da geração z");
}else if(ano_nascimento <= 43){
    alert("você é da geração millenials");
}else if(ano_nascimento <= 59){
    alert("você é da geração x");
}else if(ano_nascimento <= 78){
    alert("você é da geração baby boomers(kkk)");
}else if(ano_nascimento <= 96){
    alert("você é da geração silenciosa(shhh)");
}