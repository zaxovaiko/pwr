<?php

namespace controllers;

use core\Controller;

class HomeController extends Controller
{
    static function index()
    {
        self::render('home');
    }
}
