<main class="d-flex">
    <?php require_once('./layouts/aside.php') ?>

    <div class="content">
        <h1 class="h1">Log in</h1>
        <form action="login" method="POST">
            <label for="username" class="mb-15">User name:</label>
            <input type="text" name="username" id="username" class="form-input mb-15">

            <label for="password" class="mb-15">Password:</label>
            <input type="password" name="password" id="password" class="form-input mb-15">

            <button class="btn">Log in</button>
            <?php
            $user = ['username' => 'admin', 'password' => 'admin'];

            if (!empty($_POST)) {
                $username = isset($_POST['username']) ? $_POST['username'] : '';
                $password = isset($_POST['password']) ? $_POST['password'] : '';

                if ($user['username'] == $username && $user['password'] == $password) {
                    $_SESSION['user'] = $user;
                    $_SESSION['loggedIn'] = true;
                    header("location: /zadanie_8/");
                } else {
                    echo "<span style='color:red'>Invalid Login Details</span>";
                }
            }
            ?>
        </form>

    </div>
</main>