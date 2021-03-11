<?php

/**
 * Plugin Name:       Newly Added Post Highliter
 * Plugin URI:        https://example.com/plugins/Newly Added Post Highliter/
 * Description:       Highlight newly posts with tag
 * Version:           1.0.0
 * Requires at least: 5.2
 * Requires PHP:      7.2
 * Author:            Volodymyr Zakhovaiko
 * Author URI:        https://github.com/zaxoavoki
 * License:           GPL v2 or later
 * License URI:       https://www.gnu.org/licenses/gpl-2.0.html
 * Text Domain:       newly-added-post-highlighter
 */

function naph_admin_actions_register_menu()
{
    add_options_page("Newly Added Post Highliter", "New Post Highliter", 'manage_options', "naph", "naph_admin_page");
}

function naph_admin_page()
{
    global $_POST;
    if (isset($_POST['naph_do_change'])) {
        if ($_POST['naph_do_change'] == 'Y') {
            $opDays = $_POST['naph_days'];
            echo '<div class="notice notice-success isdismissible"><p>Settings saved.</p></div>';
            update_option('naph_days', $opDays);
        }
    }

    $opDays = get_option('naph_days');
?>
    <div class="wrap">
        <h1>Newly Added Post Highliter</h1>
        <form name="naph_form" method="post">
            <input type="hidden" name="naph_do_change" value="Y">
            <p>Highlight post title for
                <input type="number" name="naph_days" min="0" max="30" value="<?= $opDays ?>"> days
            </p>
            <p class="submit"><input type="submit" value="Submit"></p>
        </form>
    </div>
<?php
}

function naph_mark_new_post_title($content, $id)
{
    $date = get_the_date('Ymd', $id);
    $now = date('Ymd');
    $opDays = get_option('naph_days');

    $arr = ['New', 'Newest', 'Extra new'];
    shuffle($arr); // get random value from array

    if ($now - $date <= $opDays)
        return "<sup class=\"naph_marker\">" . $arr[0] . "</sup> " . $content;
    return $content;
}

function naph_register_styles()
{
    wp_register_style('naph_styles', plugins_url('/css/style.css', __FILE__));
    wp_enqueue_style('naph_styles');
}

add_action('admin_menu', 'naph_admin_actions_register_menu');
add_filter("the_title", "naph_mark_new_post_title", 10, 2);
add_action('init', 'naph_register_styles');
