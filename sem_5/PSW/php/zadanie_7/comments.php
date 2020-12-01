<!DOCTYPE html>
<html lang="zxx">

<head>
	<meta charset="UTF-8" />
	<meta name="author" content="Volodymyr Zakhovaiko, Illia Hrebenko" />
	<meta name="designer" content="Volodymyr Zakhovaiko" />
	<meta name="description" content="Comments for product" />
	<meta name="keywords" content="shop,e-commerce" />
	<meta name="title" content="Ecom - Komentarze do produktu" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
	<title>Ecom - Komentarze do produktu</title>
	<link rel="stylesheet" href="css/main.css" />
	<link rel="stylesheet" href="css/style.css" />
</head>

<body>
	<?php require_once('./layouts/header.php'); ?>

	<main class="d-flex">
		<?php require_once('./layouts/aside.php'); ?>

		<!-- Rightside content part -->
		<div class="content d-flex">
			<!-- Leftside with product description -->
			<div class="content-comments__product">
				<div class="product-desc-sm">
					<img class="product-desc-sm__img" src="images/product1.jpg" alt="Product small image" />
					<h3 class="product-desc-sm__title">Mi Bend 5</h3>
					<p class="product-desc-sm__text">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Itaque, reprehenderit!</p>
				</div>
			</div>

			<!-- Comments section -->
			<div class="content__comments">
				<h1 class="mb-15">Comments</h1>

				<div class="comments">

					<?php
					$comments = [
						['John Doe', 'https://via.placeholder.com/400x400', 'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Ut vel magni enim totam ullam corporis ducimus omnis dolorum ratione, odit quas nam quiasequi est deserunt consequatur, consequuntur dolor illo.'],
						['John Doe', 'https://via.placeholder.com/400x400', 'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Ut vel magni enim totam ullam corporis ducimus omnis dolorum ratione, odit quas nam quiasequi est deserunt consequatur, consequuntur dolor illo.'],
						['John Doe', 'https://via.placeholder.com/400x400', 'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Ut vel magni enim totam ullam corporis ducimus omnis dolorum ratione, odit quas nam quiasequi est deserunt consequatur, consequuntur dolor illo.'],
						['John Doe', 'https://via.placeholder.com/400x400', 'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Ut vel magni enim totam ullam corporis ducimus omnis dolorum ratione, odit quas nam quiasequi est deserunt consequatur, consequuntur dolor illo.'],
						['John Doe', 'https://via.placeholder.com/400x400', 'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Ut vel magni enim totam ullam corporis ducimus omnis dolorum ratione, odit quas nam quiasequi est deserunt consequatur, consequuntur dolor illo.'],
					];

					foreach ($comments as $comment) :
					?>
						<div class="comment">
							<div class="comment__ui d-flex">
								<img class="comment__ui__img" src="<?= $comment[1] ?>" alt="User image" />
								<p class="comment__ui__name"><?= $comment[0] ?></p>
								<small class="comment__ui__time"><?= rand(0, 60) ?> mins ago</small>
							</div>
							<div class="comment__body"><?= $comment[2] ?></div>
						</div>
					<?php endforeach; ?>
				</div>
			</div>
		</div>
	</main>

	<?php require_once('./layouts/footer.php'); ?>
</body>

</html>