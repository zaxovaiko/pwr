<?php

/**
 * Plugin Name:       Custom plugin for Lab_2
 * Plugin URI:        https://example.com/plugins/custom_plugin_for_lab_2
 * Description:       Inserts random ad between title and post
 * Version:           1.0.0
 * Requires at least: 5.2
 * Requires PHP:      7.2
 * Author:            Volodymyr Zakhovaiko
 * Author URI:        https://github.com/zaxoavoki
 * License:           GPL v2 or later
 * License URI:       https://www.gnu.org/licenses/gpl-2.0.html
 * Text Domain:       custom-plugin-lab-2
 */

define('OPENWEATHER_API_KEY', 'b858d37e1324d289241c87a0f3fa70d3');

$cities = $wpdb->get_results('SELECT * FROM ' . $wpdb->prefix . 'cities');

function cpf2_admin_actions_register_menu()
{
    add_options_page("Custom Plugin For Lab2", "Custom Plugin Lab2", 'manage_options', "cpf2", "cpf2_admin_page");
}

function generate_weather_card()
{
    global $cities;
    $random_key = array_rand($cities);

    $city = $cities[$random_key];
    $weather = make_request_openweather($city->name);
    
    return "
        <div class=\"cpf2_card\">
            <img src=\"http://openweathermap.org/img/wn/" . $weather->weather[0]->icon . "@2x.png\">
            <div class=\"cpf2_card_body\">
                <div>
                    <h6>" . $city->name . "</h6>
                    <small>" . round($weather->coord->lat, 3) . ", " . round($weather->coord->lon, 3) . "</small>
                </div>
                <div>
                    <h6>" . $weather->main->temp . "&deg; C</h6>
                    <small>Min: " . $weather->main->temp_min . ", Max:" . $weather->main->temp_max . "</small>
                </div>
            </div>
        </div>";
}

function cpf2_admin_page()
{
    global $wpdb;
    global $_POST;
    global $cities;

    $wpdb->show_errors();

    if (isset($_POST['cpf2_delete_id'])) {
        $cityId = $_POST['cpf2_delete_id'];
        $wpdb->delete($wpdb->prefix . 'cities', ['id' => $cityId]);
        echo '<div class="notice notice-success isdismissible"><p>City was deleted.</p></div>';
    }

    $cities = $wpdb->get_results('SELECT * FROM ' . $wpdb->prefix . 'cities');
?>
    <div class="wrap">
        <h1>Custom Plugin for Lab2</h1>
        <p>Inserts weather card between post title and text</p>

        <table class="cpf2_table">
            <thead>
                <th>ID</th>
                <th>City</th>
                <th>Action</th>
            </thead>
            <tbody>
                <?php foreach ($cities as $city) : ?>
                    <tr>
                        <td><?= $city->id ?></td>
                        <td><?= $city->name ?></td>
                        <td style="text-align: center; cursor: pointer" onclick="deleteCity(<?= $city->id ?>)">❎</td>
                    </tr>
                <?php endforeach; ?>
            </tbody>
        </table>

        <form id="cpf2_form_delete" method="post">
            <input type="hidden" name="cpf2_delete_id">
        </form>

        <script>
            function deleteCity(id) {
                const form = document.querySelector('#cpf2_form_delete');
                const input = document.querySelector('input[name=cpf2_delete_id]');
                input.value = id;
                form.submit();
            }
        </script>
        
        <form name="cpf2_form" method="post">
            <input type="hidden" name="cpf2_do_change" value="Y">
            <h3>Add new city</h3>
            <input type="text" name="city" placeholder="City name">
            <button>Add city</button>
        </form>
    </div>
<?php
}

function cpf2_add_section_after_post_title($content)
{
    $card = generate_weather_card();
    return $card . $content;
}

function cpf2_register_styles()
{
    wp_register_style('cpf2_styles', plugins_url('/css/main.css', __FILE__));
    wp_enqueue_style('cpf2_styles');
}

function make_request_openweather($city = 'Wroclaw')
{
    return json_decode(file_get_contents('http://api.openweathermap.org/data/2.5/weather?units=metric&q=' . $city . '&appid=' . OPENWEATHER_API_KEY));
}

add_action('admin_menu', 'cpf2_admin_actions_register_menu');
add_filter("the_content", "cpf2_add_section_after_post_title", 10, 2);
add_action('init', 'cpf2_register_styles');
