<header class="header">
  <nav class="d-flex">
    <a class="header__sitename" href="">Ecom</a>
    <ul class="header__nav list-style-none">
      <li><a href="comments">Comments</a></li>
      <li><a href="settings">Settings</a></li>
      <li><a href="cookies">Cookies</a></li>
    </ul>
    <p class="header__user">
      <?= (isset($_SESSION['loggedIn']) && $_SESSION['loggedIn']) ? "Hi, <a href='order'>" .
        $_SESSION['user']['username'] .
        "</a><a style='margin-left: 15px' href='logout'>Log out</a>" : "<a href='login'>Log in</a>" ?>
    </p>
  </nav>
</header>