<?php

namespace core;

class Controller
{
    static function render($view, $data = null)
    {
        return View::load($view, $data);
    }
}
