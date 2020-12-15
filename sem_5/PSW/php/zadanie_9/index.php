<?php

ini_set('error_reporting', E_ALL);
session_start();

require_once('./layouts/index.php');

if (isset($_SESSION['loggedIn']) && $_SESSION['loggedIn'] && isset($_SESSION['email'])) {
	if (isset($_COOKIE['email'])) {
		$_SESSION['email'] = $_COOKIE['email'];
	}

	$mysqli = mysqli_connect("localhost", "root", "", "psw_9");

	if (!$mysqli) {
		die("Failed to connect to MySQL: (" . mysqli_connect_errno() . ") " . mysqli_connect_error());
	}

	$user = mysqli_query($mysqli, "SELECT id, email, username FROM users WHERE email = '" . $_SESSION['email'] . "'");
	$rows = mysqli_num_rows($user);
	$data = mysqli_fetch_row($user);

	$_SESSION['user']['id'] = $data[0];
	$_SESSION['user']['username'] = $data[2];
	$_SESSION['user']['email'] = $data[1];
}

$path = isset($_GET['path']) ? $_GET['path'] : '';

$routes = [
	'404' => ['Not found', './404.php'],
	'' => ['Main page', './main.php'],
	'logout' => ['Log out', './logout.php', true],
	'terms' => ['Terms', './terms.php'],
	'order' => ['Order', './order.php', true],
	'comments' => ['Comments', './comments.php'],
	'settings' => ['Settings', './settings.php', true],
	'cookies' => ['Cookies', './cookies.php', true],
	'login' => ['Log in', './login.php'],
	'register' => ['Sign in', './register.php'],
	'diagnostic' => ['Skrypt diagnostyczny', './diagnostic.php', true],
];

function showErrorPage($route)
{
	return load($route[0], $route[1]);
}

if (!isset($routes[$path])) {
	showErrorPage($routes['404']);
	exit();
}

if (isset($routes[$path][2]) && $routes[$path][2] && (!isset($_SESSION['loggedIn']) || !$_SESSION['loggedIn'])) {
	showErrorPage($routes['404']);
	exit();
}

load($routes[$path][0], $routes[$path][1]);
