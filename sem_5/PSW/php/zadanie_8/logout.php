<?php

if (isset($_SESSION['loggedIn'])) {
    $_SESSION['loggedIn'] = null;
    header('location: login');
}
