<?php function load($title, $path)
{ ?>
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <base href="http://localhost/zadanie_9/">
        <meta charset="UTF-8" />
        <meta name="author" content="Volodymyr Zakhovaiko, Illia Hrebenko" />
        <meta name="designer" content="Volodymyr Zakhovaiko" />
        <meta name="description" content="<?= $title ?>" />
        <meta name="keywords" content="shop,e-commerce" />
        <meta name="title" content="Ecom - <?= $title ?>" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Ecom - <?= $title ?></title>
        <link rel="stylesheet" href="./css/main.css" />
        <link rel="stylesheet" href="./css/style.css" />
        <link rel="stylesheet" href="./css/dom.css" />
        <?php if (isset($_SESSION['loggedIn']) && $_SESSION['loggedIn'] && isset($_COOKIE['bg']) && isset($_COOKIE['textColor']) && isset($_COOKIE['textWeight'])) : ?>
            <style>
                body {
                    background: <?= $_COOKIE['bg'] ?> !important;
                    font-weight: <?= $_COOKIE['textWeight'] ?> !important;
                    color: <?= $_COOKIE['textColor'] ?> !important;
                }
            </style>
        <?php endif; ?>
    </head>

    <body>
        <?php require_once('./layouts/header.php'); ?>
        <?php require_once($path); ?>
        <?php require_once('./layouts/footer.php'); ?>
    </body>

    </html>
<?php } ?>