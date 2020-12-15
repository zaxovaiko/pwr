<?php
define('ADS_TEXT', '-20%');
?>

<main class="d-flex">
    <?php require('./layouts/aside.php'); ?>

    <div class="content content-main">
        <div class="content-main__ads mb-15">
            <h1 id="ads"><?= ADS_TEXT ?></h1>
        </div>

        <!-- List of products -->
        <article class="content-main__products products">
            <h2>Resent Products</h2>

            <div id="resent-products" class="d-flex">
                <?php

                $products = [
                    ['Product', rand(100, 2000), './images/product1.jpg'],
                    ['Product', rand(100, 2000), './images/product2.jpg'],
                    ['Product', rand(100, 2000), './images/product3.jpg'],
                    ['Product', rand(100, 2000), './images/product4.jpg'],
                ];

                for ($i = 0; $i < count($products); $i++) : ?>
                    <div class="product">
                        <a href="/product">
                            <img class="product__img" src="<?= $products[$i][2] ?>" alt="Product image" />
                        </a>
                        <div>
                            <a class="product__title" href="#"><?= $products[$i][0] . ' ' . (intval($i) + 1) ?></a>
                            <h3 class="product__price"><?= $products[$i][1] ?> zł</h3>
                        </div>
                    </div>
                <?php endfor; ?>
            </div>
        </article>
    </div>
</main>