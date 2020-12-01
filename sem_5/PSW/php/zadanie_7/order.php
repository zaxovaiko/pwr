<?php

function validate()
{
    $to_validate = array(
        'name' => function ($name) {
            return (bool)preg_match('/^[A-Za-z\s]+$/', $name, $matches);
        },
        'gender' => function ($gender) {
            return strcmp($gender, 'male') == 0 || strcmp($gender, 'women') == 0;
        },
        'address' => function ($address) {
            return (bool)preg_match('/^ul. */', $address);
        },
        'color' => function ($color) {
            $colors = ['white', 'black', 'blue', 'pink'];
            return in_array($color, $colors);
        },
        'number' => function ($number) {
            return filter_var($number, FILTER_VALIDATE_INT);
        },
        'comment' => function ($comment) {
            return strlen($comment) < 256;
        },
        'notify' => function ($notify) {
            return $notify == 'yes';
        },
        'delivery' => function ($delivery) {
            return $delivery == 'yes';
        },
        'terms' => function ($terms) {
            return $terms == 'yes';
        }
    );

    $errors = [];
    foreach ($_POST as $key => $value) {
        if (array_key_exists($key, $to_validate)) {
            $res = $to_validate[$key]($value);
            if (!$res) {
                $errors[$key] = [$value, $res];
            }
        }
    }

    return $errors;
}
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta name="author" content="Volodymyr Zakhovaiko, Illia Hrebenko" />
    <meta name="designer" content="Volodymyr Zakhovaiko" />
    <meta name="description" content="Order page" />
    <meta name="keywords" content="shop,e-commerce" />
    <meta name="title" content="Ecom - Strona zamówienia" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Ecom - Zamówienie</title>
    <link rel="stylesheet" href="css/main.css" />
    <link rel="stylesheet" href="css/style.css" />
    <style>
        #tip {
            background: #000;
            opacity: 0.8;
            position: fixed;
            right: 15px;
            bottom: 15px;
            color: #fff;
            padding: 15px;
            display: none;
        }
    </style>
</head>

<body>
    <?php require_once('./layouts/header.php'); ?>

    <main class="d-flex">
        <p id="tip"></p>

        <?php require_once('./layouts/aside.php'); ?>

        <!-- Rightside content part -->
        <div class="content d-flex">
            <div class="order-form">
                <h1 class="h1">Order Confirmation</h1>

                <?php if (empty($_POST)) : ?>

                    <form id="order-form" action="order.php" method="post">
                        <div class="form-group">
                            <label for="name">Name</label>
                            <input class="form-input" autofocus value="John Doe" type="text" placeholder="Name" name="name" id="name" required />
                        </div>

                        <div class="form-group">
                            <label for="male">Gender</label>
                            <div class="form-check-inline">
                                <input class="form-check-input" name="gender" id="male" value="male" type="radio" checked required />
                                <label class="form-check-label" for="male">Male</label>
                            </div>
                            <div class="form-check-inline">
                                <input class="form-check-input" name="gender" id="female" value="female" type="radio" required />
                                <label class="form-check-label" for="female">Female</label>
                            </div>
                            <div class="form-check-inline">
                                <input class="form-check-input" name="gender" id="other" value="other" type="radio" required disabled />
                                <label class="form-check-label" for="other">Other</label>
                            </div>
                        </div>

                        <div class="form-group">
                            <label for="address">Address</label>
                            <input class="form-input" type="text" value="ul. Stanislawa Wysokiego 24" placeholder="Address" name="address" id="address" required />
                        </div>

                        <div class="form-group">
                            <label for="color">Color</label>
                            <select class="form-input" name="color" id="color" required>
                                <option value="" selected hidden disabled>Choose color</option>
                                <optgroup label="Light colors">
                                    <option value="pink">Pink</option>
                                    <option value="white" selected>White</option>
                                </optgroup>
                                <optgroup label="Dark colors">
                                    <option value="blue">Blue</option>
                                    <option value="black">Black</option>
                                </optgroup>
                            </select>
                        </div>

                        <div class="form-group">
                            <label for="number">Number of items</label>
                            <input class="form-input" type="number" min="1" max="100" placeholder="Number of items" name="number" id="number" value="1" required />
                        </div>

                        <div class="form-group">
                            <label for="comment">Comment from customer</label>
                            <textarea class="form-input" placeholder="Your comment" maxlength="200" name="comment" id="comment" rows="3"></textarea>
                        </div>

                        <div class="form-group form-inside">
                            <div class="form-check-inline">
                                <input checked class="form-check-input" name="notify" id="notify" value="yes" type="checkbox" />
                                <label class="form-check-label" for="notify">I want to be notified about this product</label>
                            </div>
                            <br />
                            <div class="form-check-inline">
                                <input class="form-check-input" name="delivery" id="delivery" value="yes" type="checkbox" />
                                <label class="form-check-label" for="delivery">Ask for delivery to my house</label>
                            </div>
                        </div>

                        <div class="form-group">
                            <input checked class="form-check-input" name="terms" id="terms" value="yes" type="radio" required />
                            <label class="form-check-label" for="terms">I agree with terms and privacy</label>
                        </div>

                        <div class="form-buttons">
                            <button class="btn" type="reset">Reset</button>
                            <button class="btn">Buy</button>
                        </div>
                    </form>

                <?php else : ?>

                    <div style="padding: 15px; border: solid 1px #ddd; margin-bottom: 15px;">
                        <?php
                        $errors = validate();
                        if (empty($errors)) : ?>
                            <h3>Form was submitted.</h3>
                            <p>Client IP: <?= $_SERVER['REMOTE_ADDR'] ?></p>
                            <p>Delivary address: <?= preg_replace('/ul./', 'st. ', $_POST['address']) ?></p>
                            <p>You need to pay: <?= $_POST['number'] * 2 ?> zł</p>
                        <?php else : ?>
                            <h3 style="color: red;">Form was submitted incorrectly.</h3>
                            <?php foreach ($errors as $key => $error) :  ?>
                                <p>Invalid data on this field: <?= $key . " with value: <b>" . $error[0] . '</b>' ?></p>
                            <?php endforeach; ?>
                            <button style="margin-top: 15px;" onclick="location.href='/zadanie_7/order.php'">Try again</button>
                        <?php endif; ?>
                    </div>

                <?php endif; ?>

                <!-- Suggested products panel -->
                <article>
                    <h3 class="order-form__suggested-products__title">Suggested Products</h3>
                    <div id="resent-products" class="products d-flex">
                        <?php
                        // $json = json_decode(require_once('./data/products.json'), true);
                        $products = [
                            ['Product', rand(10, 1000), 'images/product1.jpg', 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Itaque rem cum doloremque? Voluptates fugit, itaque quod maiores excepturi ex libero officia ea laboriosam, rerum repellat quam maxime alias totam adipisci.'],
                            ['Product', rand(10, 1000), 'images/product2.jpg', 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Itaque rem cum doloremque? Voluptates fugit, itaque quod maiores excepturi ex libero officia ea laboriosam, rerum repellat quam maxime alias totam adipisci.'],
                            ['Product', rand(10, 1000), 'images/product3.jpg', 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Itaque rem cum doloremque? Voluptates fugit, itaque quod maiores excepturi ex libero officia ea laboriosam, rerum repellat quam maxime alias totam adipisci.'],
                            ['Product', rand(10, 1000), 'images/product4.jpg', 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Itaque rem cum doloremque? Voluptates fugit, itaque quod maiores excepturi ex libero officia ea laboriosam, rerum repellat quam maxime alias totam adipisci.'],
                        ];

                        while ($product = current($products)) : ?>
                            <div class="product">
                                <a href="product.php">
                                    <img class="product__img" src="<?= $product[2] ?>" alt="Product image" />
                                </a>
                                <div>
                                    <a class="product__title" href="#"><?= $product[0] . ' ' . (key($products) + 1) ?></a>
                                    <h3 class="product__price"><?= $product[1] ?> zł</h3>
                                </div>
                            </div>
                        <?php
                            next($products);
                        endwhile;
                        ?>
                    </div>
                </article>
            </div>

            <!-- Rightside with product description -->
            <div class="order-product">
                <article class="product-desc-sm">
                    <img class="product-desc-sm__img" src="images/product4.jpg" alt="Product small image" />
                    <h3 class="product-desc-sm__title">IPhone 12</h3>
                    <p class="product-desc-sm__text">
                        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Itaque, reprehenderit!
                    </p>
                </article>
            </div>
        </div>
    </main>

    <?php require_once('./layouts/footer.php'); ?>

    <script src="js/order.js"></script>
    <!-- <script src="js/main.js"></script> -->
</body>

</html>