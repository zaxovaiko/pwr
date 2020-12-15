<main class="d-flex">
    <?php require_once('./layouts/aside.php') ?>

    <div class="content">
        <h1 class="h1">Diagnostic</h1>

        <form action="diagnostic" method="post">
            <select name="field" id="field">
                <option value="id">id</option>
                <option value="username">username</option>
                <option value="email">email</option>
                <option value="password">password</option>
            </select>

            <select name="operator" id="operator">
                <option value="like">Contains</option>
                <option value="=">Equal</option>
                <option value=">">Greater</option>
                <option value="<">Less</option>
            </select>

            <input type="text" name="tofind">

            <button type="submit">Filter</button>
        </form>

        <table id="diagnostic">
            <thead>
                <th>ID</th>
                <th>Name</th>
                <th>Email</th>
                <th>Password hash</th>
            </thead>
            <pre>
            <tbody>
                <?php

                $mysqli = mysqli_connect("localhost", "root", "", "psw_9");

                if (!$mysqli) {
                    echo "Failed to connect to MySQL: (" . mysqli_connect_errno() . ") " . mysqli_connect_error();
                    die();
                }

                if (isset($_POST['field']) && isset($_POST['operator']) && isset($_POST['tofind'])) {
                    $field = $_POST['field'];
                    $op = $_POST['operator'];
                    $tofind = $_POST['tofind'];

                    $query = "SELECT * FROM users WHERE $field $op '$tofind'";
                } else {
                    $query = "SELECT * FROM users";
                }

                echo $query;
                $res = mysqli_query($mysqli, $query);


                if ($res) {
                    $rows = mysqli_fetch_all($res);

                    foreach ($rows as $row) {
                        echo '<tr>';
                        foreach ($row as $field) {
                            echo '<td>' . $field  . '</td>';
                        }
                        echo '</tr>';
                    }
                } else {
                    echo 'There is no any user yet.';
                }

                ?>
            </tbody>
        </table>

    </div>
</main>