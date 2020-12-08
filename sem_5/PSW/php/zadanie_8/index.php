<?php

session_start();

require_once('./layouts/index.php');

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
// FIXME: Change structure of the project
