<?php

namespace core;

use core\Controller;

class Router
{
    private static $routes = [];

    static function add($route, $array)
    {
        self::$routes[$route] = $array;
    }

    static function view($route, $view)
    {
        self::$routes[$route] = [Controller::class, 'render', $view];
    }

    static function run()
    {
        $uri = preg_replace('/mvc\//', '', $_SERVER['REQUEST_URI']);

        if (array_key_exists($uri, self::$routes)) {
            $params = self::$routes[$uri];

            $controller = $params[0];
            $action = $params[1];

            if (isset($params[2])) {
                $view = $params[2];
                $controller::$action($view);
            } else {

                // WTF ????????????
                $controller::$action();
            }

            $view = $params[2];
                $controller::$action($view);
        } else {
            // call error route
        }
    }
}
