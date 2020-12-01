<?php
define('ADS_TEXT', '-20%')
?>

<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="UTF-8" />
	<meta name="author" content="Volodymyr Zakhovaiko, Illia Hrebenko" />
	<meta name="designer" content="Volodymyr Zakhovaiko" />
	<meta name="description" content="Main page of ecom website" />
	<meta name="keywords" content="shop,e-commerce" />
	<meta name="title" content="Ecom - Strona główna" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
	<title>Ecom - Strona główna</title>
	<link rel="stylesheet" href="css/main.css" />
	<link rel="stylesheet" href="css/style.css" />
</head>

<body>
	<?php require('./layouts/header.php'); ?>

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
						['Product', rand(100, 2000), 'images/product1.jpg'],
						['Product', rand(100, 2000), 'images/product2.jpg'],
						['Product', rand(100, 2000), 'images/product3.jpg'],
						['Product', rand(100, 2000), 'images/product4.jpg'],
					];

					for ($i = 0; $i < count($products); $i++) : ?>
						<div class="product">
							<a href="product.php">
								<img class="product__img" src="<?= $products[$i][2] ?>" alt="Product image" />
							</a>
							<div>
								<a class="product__title" href="#"><?= $products[$i][0] . ' ' . intval($i) + 1 ?></a>
								<h3 class="product__price"><?= $products[$i][1] ?> zł</h3>
							</div>
						</div>
					<?php endfor; ?>
				</div>
			</article>
		</div>
	</main>

	<?php require('./layouts/footer.php'); ?>

	<!-- <script src="js/main.js"></script> -->
</body>

</html>