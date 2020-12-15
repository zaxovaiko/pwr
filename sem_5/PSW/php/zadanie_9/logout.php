<?php

if (isset($_SESSION['loggedIn'])) {
    session_destroy();
    setcookie('loggedIn', null, 0);
    setcookie('email', null, 0);
    header('location: login');
}
