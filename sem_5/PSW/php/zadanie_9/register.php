<?php

// Database connection
$mysqli = mysqli_connect("localhost", "root", "", "psw_9");

if (!$mysqli) {
    // header('Location: /zadanie_9');
    die("Failed to connect to MySQL: (" . mysqli_connect_errno() . ") " . mysqli_connect_error() . '</body></html>');
}

if (isset($_POST['username']) && isset($_POST['email']) && isset($_POST['password']) && isset($_POST['password_confirmation'])) {
    $to_validate = array(
        'username' => function ($name) {
            return (bool)preg_match('/^[A-Za-z\s]+$/', $name, $matches);
        },
        'email' => function ($email) {
            return filter_var($email, FILTER_VALIDATE_EMAIL);
        },
        'password' => function ($password) {
            return strlen($password) > 0 && strlen($password) < 32;
        },
        'password_confirmation' => function ($pc) {
            return $pc == $_POST['password'];
        }
    );

    $errors = [];
    foreach ($_POST as $key => $value) {
        if (isset($to_validate[$key])) {
            $res = $to_validate[$key]($value);
            if (!$res) {
                $errors[$key] = [$value, $res];
            }
        }
    }

    if (!$errors) {
        $name = $_POST['username'];
        $email = $_POST['email'];
        $password = password_hash($_POST['password'], PASSWORD_BCRYPT, ['cost' => 8]);

        $user = mysqli_query($mysqli, "SELECT * FROM users WHERE email = '$email'");

        if (isset($_SESSION['loggedIn']) && $_SESSION['loggedIn']) {
            $id = $_SESSION['user']['id'];
            $update = mysqli_query($mysqli, "UPDATE users SET username='$name', email='$email', password='$password' WHERE id = '$id'");
        } else {
            $result = mysqli_query($mysqli, "INSERT INTO users (username, email, password) VALUES ('$name', '$email', '$password')");
        }
        mysqli_close($mysqli);
    }
}

?>

<main class="d-flex">
    <?php require_once('./layouts/aside.php') ?>

    <div class="content">
        <h1 class="h1">
            <?= isset($_SESSION['loggedIn']) && $_SESSION['loggedIn'] ? 'Set up profile' : 'Sign in'; ?>
        </h1>
        <form action="register" method="POST">
            <label for="username" class="mb-15">Name:</label>
            <input <?= 'value="' . (isset($_SESSION['user']) ? $_SESSION['user']['username'] : '') . '"' ?> type="text" name="username" id="username" class="form-input mb-15">

            <label for="email" class="mb-15">Email:</label>
            <input <?= 'value="' . (isset($_SESSION['user']) ? $_SESSION['user']['email'] : '') . '"' ?> type="text" name="email" id="email" class="form-input mb-15">

            <label for="password" class="mb-15">Password:</label>
            <input type="password" name="password" id="password" class="form-input mb-15">

            <label for="password_confirmation" class="mb-15">Password confirmation:</label>
            <input type="password" name="password_confirmation" id="password_confirmation" class="form-input mb-15">

            <button class="btn mb-15"><?= isset($_SESSION['loggedIn']) && $_SESSION['loggedIn'] ? 'Save changes' : 'Create account' ?></button>
            <?php
            if (isset($result) && $result) {
                $_SESSION['loggedIn'] = true;
                $_SESSION['email'] = $_POST['email'];

                setcookie('loggedIn', true);
                setcookie('email', $_POST['email']);

                header('Location: /zadanie_9');
            } else  if (isset($result) && !$result) {
                echo '<p style="color: red">User already exists</p>';
            }

            if (isset($update) && $update) {
                $_SESSION['email'] = $email;
                $_SESSION['notification'] = 'Changes saved';
                header('Refresh: 0');
                die();
            } else if (isset($update) && !$update) {
                $msg = 'User already exists you can not update your data.';
                $var = 'msg';
                echo '<p style="color: red">' . $$var . '</p>';
            }
            ?>
        </form>
        <div>
            <?php
            if (isset($_SESSION['notification'])) {
                echo '<p style="color: green">' . $_SESSION['notification'] . '</p>';
                $_SESSION['notification'] = null;
            }
            ?>
            <?php
            if (isset($errors) && $errors) {
                foreach ($errors as $key => $error) {
                    echo "<p>Invalid data on field $key with value: <b>$error[0]</b></p>";
                }
            }
            ?>
        </div>

    </div>
</main>