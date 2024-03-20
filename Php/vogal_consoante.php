<?php
header('Content-Type: text/html; charset=utf-8');
$resposta = $_POST["pergunta"];

switch ($resposta) {
  case "a":
    echo "A LETRA: A É UMA VOGAL";
    break;
  case "e":
    echo "A LETRA: E É UMA VOGAL";
    break;
  case "i":
    echo "A LETRA: i É UMA VOGAL";
    break;
  case "o":
    echo "A LETRA: o É UMA VOGAL";
    break;
  case "u":
    echo "A LETRA: u É UMA VOGAL";
    break;
  default:
    echo "A LETRA:". $resposta. "É UMA CONSOANTE";
}
?>