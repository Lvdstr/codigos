<h1>testezinho kkkk</h1>
<form action = "Calculazinha.php" method="GET">
	<input type="number" name="value1">
	<input type="number" name="value2">
	<select name="cars" id="cars">
      <option value="+">somar</option>
      <option value="-">subtrair</option>
      <option value="*">multiplicar</option>
      <option value="/">dividir</option>
  </select>
  <input type="submit" value="enviar" />
</form>

<script>
	
</script>

<?php
$a = $_GET["cars"];
$v1 = $_GET["value1"];
$v2 = $_GET["value2"];

switch ($a) {
	case '+':
		echo $v1 + $v2;
		break;
	case '-':
		echo $v1 - $v2;
		break;
	case '*':
		echo $v1 * $v2;
		break;
	case '/':
		echo $v1 / $v2;
		break;
}
?>