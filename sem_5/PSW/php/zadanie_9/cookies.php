<main class="d-flex">
    <?php require_once('./layouts/aside.php') ?>

    <div class="right-part" style="padding: 15px">
        <p>Your cookies : </p>
        <?php
        foreach ($_COOKIE as $key => $value) {
            print("<p>$key: $value</p>");
        }
        ?>
    </div>
</main>