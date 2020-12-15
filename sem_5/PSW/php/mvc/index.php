<?php

ini_set('display_errors', 1);

require_once './helpers/autoload.php';

use core\Router;
// use controllers\HomeController as Home;
// use controllers\AuthController as Auth;

// Router::add('/', Home::class, 'index');
// Router::add('/order', Home::class, 'order');

// Router::add('/login', Auth::class, 'login');
// Router::add('/logout', Auth::class, 'logout');
// Router::add('/register', Auth::class, 'register');

// Router::add('/cookies', Home::class, 'cookies');
// Router::add('/comments', Home::class, 'comments');
// Router::add('/settings', Home::class, 'settings');

Router::view('/terms', 'terms');
Router::run();
