<?php

// error_reporting (E_ALL);

include('kcaptcha.php');

session_start();

$captcha = new KCAPTCHA($_GET['string']);

if($_REQUEST[session_name()]){
	$_SESSION['captcha_keystring'] = $captcha->getKeyString();
}

?>