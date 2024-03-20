<!DOCTYPE html>
<html>
  <head lang="pt-br">
    <meta http-equiv="content-type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>calculadora p.a.ga</title>
  </head>
  <body>
    <div class="container">
      <h1>calculadora</h1>
      <form action = "calculadora.php" method = "POST">
        <label>PRIMEIRO NÚMERO</label>
        <input type="number" name="first_number">
        <label>SEGUNDO NÚMERO</label>
        <input type="number" name="second_value">
        <select name="operações">
          <option value="" selected disabled>selecione</option>
          <option value="somar">somar</option>
          <option value="subtrair">subtrair</option>
          <option value="multiplicar">multiplicar</option>
          <option value="dividir">dividir</option>
          <option value="modulo">modulo</option>
        </select>
      </form>
      <button>enviar</button>
    </div>
    <?php
      header('Content-Type: text/html; charset=utf-8');
      $first_value = $_POST["first_number"];
      $second_value = $_POST["second_value"];
      $operação = $_POST["operações"];
      
      switch($operação){
        case "somar":
          $resultado = $first_value + $second_value;
          echo $resultado;
          break;
        case "subtrair":
          $resultado = $first_value - $second_value;
          echo $resultado;
          break;
        case "multiplicar":
          $resultado = $first_value * $second_value;
          echo $resultado;
          break;
        case "dividir":
          $resultado = $first_value / $second_value;
          echo $resultado;
          break;
        case "modulo":
          $resultado = $first_value % $second_value;
          echo $resultado;
          break;
  }
    ?>
  </body>
</html>