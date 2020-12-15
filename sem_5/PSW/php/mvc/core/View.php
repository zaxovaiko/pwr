<?php

namespace core;

class View
{
    static function load($view, $data)
    {
        // $data
        require_once __DIR__ . '\\views\\' . $view . 'php';
    }
}
