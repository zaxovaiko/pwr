<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="UTF-8" />
	<meta name="author" content="Volodymyr Zakhovaiko, Illia Hrebenko" />
	<meta name="designer" content="Volodymyr Zakhovaiko" />
	<meta name="description" content="Terms" />
	<meta name="keywords" content="shop,e-commerce" />
	<meta name="title" content="Ecom - Terms" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
	<title>Ecom - Terms</title>
	<link rel="stylesheet" href="css/main.css" />
	<link rel="stylesheet" href="css/style.css" />
	<link rel="stylesheet" href="css/dom.css" />

	<style>
		.wrapper {
			position: relative;
			left: -15px;
			right: -15px;
			top: -15px;
			width: 100vw;
			background-attachment: fixed;
			background-repeat: no-repeat;
			background-image: url("./images/wall.jpg");
			background-size: cover;
			background-position: center;
			height: 500px;
			margin-bottom: 15px;
		}
	</style>
</head>

<body style="position: relative">
	<div class="wrapper"></div>
	<?php require_once('./layouts/header.php'); ?>

	<main class="d-flex">
		<?php require_once('./layouts/aside.php'); ?>

		<!-- Rightside content part -->
		<div class="content">
			<div class="terms__wrapper"></div>
			<article class="terms">
				<h1 id="bigheading" class="highlighted">Terms and Conditions</h1>

				<!-- main section -->
				<section>
					<h4 id="smallheading">Welcome to Ecom!</h4>
				</section>

				<!-- license -->
				<section>
					<h2>License</h2>
					<p>
						Unless otherwise stated, Company Name and/or its licensors own the intellectual property rights for all material on Ecom. All intellectual property
						rights are reserved. You may access this from Ecom for your own personal use subjected to restrictions set in these terms and conditions.
					</p>
					<p>You must not:
						<ul id=" list">
							<li id="item1">Republish material from Ecom</li>
							<li id="item2">Sell, rent or sub-license material from Ecom</li>
							<li id="item3">Reproduce, duplicate or copy material from Ecom</li>
							<li id="item4">Redistribute content from Ecom</li>
						</ul>
					</p>

					<p>This Agreement shall begin on the date hereof.</p>
				</section>

				<!-- cookies -->
				<section>
					<h2>Cookies</h2>
					<p>We employ the use of cookies. By accessing Ecom, you agreed to use cookies in agreement with the Company Name's Privacy Policy.</p>
					<p>
						Most interactive websites use cookies to let us retrieve the user's details for each visit. Cookies are used by our website to enable the functionality
						of certain areas to make it easier for people visiting our website. Some of our affiliate/advertising partners may also use cookies.
					</p>
				</section>

				<!-- iframes -->
				<section>
					<h2>iFrames</h2>
					<p>
						Without prior approval and written permission, you may not create frames around our Webpages that alter in any way the visual presentation or appearance
						of our Website.
					</p>
				</section>

				<!-- Removal of links from our website -->
				<section>
					<h2>Removal of links from our website</h2>
					<p>
						If you find any link on our <mark>Website</mark> that is offensive for any reason, you are free to contact and inform us any moment. We will consider
						requests to remove links but we are not obligated to or so or to respond to you directly.
					</p>
					<p>
						We do not ensure that the information on this website is correct, we do not warrant its completeness or accuracy; nor do we promise to ensure that the
						website remains available or that the material on the website is kept up to date.
					</p>
				</section>
			</article>
		</div>
	</main>

	<?php require_once('./layouts/footer.php'); ?>

	<script src="js/terms.js"></script>
	<script src="js/about.js"></script>
</body>

</html>