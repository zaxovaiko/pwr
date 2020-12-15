<?php

$mysqli = mysqli_connect("localhost", "root", "", "psw_9");

if (!$mysqli) {
    echo "Failed to connect to MySQL: (" . mysqli_connect_errno() . ") " . mysqli_connect_error();
    die();
}

if (isset($_POST) && isset($_POST['username']) && isset($_POST['password'])) {
    $username = $_POST['username'];
    $password = $_POST['password'];

    $username = mysqli_real_escape_string($mysqli, $username);
    $result = mysqli_query($mysqli, "SELECT * FROM users WHERE username = '$username'");

    if ($result) {
        $row = mysqli_fetch_row($result);

        if (password_verify($_POST['password'], $row[3])) {
            $_SESSION['loggedIn'] = true;
            $_SESSION['email'] = $row[2];

            setcookie('loggedIn', true);
            setcookie('email', $row[2]);
            header("location: /zadanie_9/");
        } else {
            $error = 'Wrong password';
        }
    } else {
        $error = 'User was not found';
    }
}
?>


<main class="d-flex">
    <?php require_once('./layouts/aside.php') ?>

    <div class="content">
        <h1 class="h1">Log in</h1>
        <form action="login" method="POST">
            <label for="username" class="mb-15">User name:</label>
            <input type="text" name="username" id="username" class="form-input mb-15">

            <label for="password" class="mb-15">Password:</label>
            <input type="password" name="password" id="password" class="form-input mb-15">

            <button class="btn mb-15">Log in</button>
            <?php
            if (isset($error) && $error) {
                echo "<p style='color: red;'>$error</p>";
            }
            ?>
        </form>
        <div>
            <?php
            if (isset($result) && !$result) {
                $Invalid = "<span style='color:red'>User was not found. (Check your input data)</span>";
                $str = "Invalid";
                echo quotemeta($$str);
            }
            ?>
        </div>
    </div>
</main>