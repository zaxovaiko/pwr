<?php

spl_autoload_register(function ($class_name) {
    include_once __DIR__ . '\\..\\' . str_replace("\\", DIRECTORY_SEPARATOR, $class_name) . '.php';
});
