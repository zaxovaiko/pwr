package com.dao;

import com.User;
import java.sql.*;


public class UserDAO {
    private final static String DB_URL = "jdbc:mysql://localhost:3306/products";
    private final static String DB_USER = "root";
    private final static String DB_PASS = "";

    public User getUserByEmail(String email) {
        String sql = "SELECT * FROM users WHERE email = " + '"' + email + '"';

        User user = null;
        try {
            Connection connection = DriverManager.getConnection(DB_URL, DB_USER, DB_PASS);
            Statement statement = connection.createStatement();

            ResultSet rs = statement.executeQuery(sql);

            while (rs.next()) {
                user = new User();
                user.setId(rs.getInt("id"));
                user.setName(rs.getString("name"));
                user.setEmail(rs.getString("email"));
                user.setPassword(rs.getString("password"));
            }

            statement.close();
            connection.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }

        return user;
    }
}
