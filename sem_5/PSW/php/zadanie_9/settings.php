<?php

if (isset($_POST['bgColor']) && isset($_POST['textColor']) && isset($_POST['textWeight'])) {
    setcookie('bg', $_POST['bgColor'], time() + 3600 * 30);
    setcookie('textColor', $_POST['textColor'], time() + 3600 * 30);
    setcookie('textWeight', $_POST['textWeight'], time() + 3600 * 30);
    header("Refresh:0");
}

?>

<main class="d-flex">
    <?php require_once('./layouts/aside.php') ?>

    <div class="content">
        <h1 class="h1">Settings</h1>
        <form action="settings" method="POST">
            <label for="bgColor" class="mb-15">Background color:</label>
            <select name="bgColor" id="bgColor" class="form-input mb-15">
                <option value="#fff">White</option>
                <option value="#000">Black</option>
                <option value="blue">Blue</option>
                <option value="green">Green</option>
                <option value="red">Red</option>
            </select>

            <label for="textColor" class="mb-15">Text color:</label>
            <input class="mb-15 form-input" type="color" name="textColor" id="textColor" />

            <label for="textWeight" class="mb-15">Text weight:</label>
            <select name="textWeight" id="textWeight" class="form-input mb-15">
                <option value="300">300</option>
                <option value="400">400</option>
                <option value="500">500</option>
                <option value="600">600</option>
                <option value="700">700</option>
            </select>
            <button class="btn">Set new styles</button>
        </form>
    </div>
</main>