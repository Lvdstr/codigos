function calc(value1, value2, operador){
    switch (operador) {
    	case '+':
        	alert(value1 + value2);
        	break;
        case '-':
            alert(value1 - value2);
            break;
          
        case '*':
            alert(value1 * value2);
            break;
            
        case '/':
            alert(value1 / value2);
            break;
          
        case '%':
            alert(value1 % value2);
            break;
          
        case '**':
            alert(value1 ** value2);
            break;
          
        default:
            alert("fatal error");
        }
      }
      
      var value_one = parseInt(prompt("digite o primeiro numero: "));
      var value_two = parseInt(prompt("digite o segundo numero: "));
      alert("operações disponíveis: +, -, *, /, %, **");
      var operação = prompt("agora escolha a operação:");
      calc(value_one, value_two, operação);
