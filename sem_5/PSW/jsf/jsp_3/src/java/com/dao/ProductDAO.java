package com.dao;

import com.Product;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class ProductDAO {
    private final static String DB_URL = "jdbc:mysql://localhost:3306/products";
    private final static String DB_USER = "root";
    private final static String DB_PASS = "";

    public List<Product> getAllProducts() {
        String sql = "SELECT * FROM products";
        List<Product> list = new ArrayList<>();

        try {
            Connection connection = DriverManager.getConnection(DB_URL, DB_USER, DB_PASS);
            Statement statement = connection.createStatement();

            ResultSet rs = statement.executeQuery(sql);

            while (rs.next()) {
                Product product = new Product();
                product.setId(rs.getInt("id"));
                product.setTitle(rs.getString("title"));
                product.setDescription(rs.getString("description"));
                product.setCategory(rs.getString("category"));
                product.setPrice(rs.getFloat("price"));
                product.setImages(rs.getString("images"));
                list.add(product);
            }

            statement.close();
            connection.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }

        return list;
    }

    public void addProduct(String title, String description, String category, float price, String image) {
        String sql = "INSERT INTO products (id, title, description, category, price, images) VALUES (NULL, ?, ?, ?, ?, ?)";

        try {
            Connection connection = DriverManager.getConnection(DB_URL, DB_USER, DB_PASS);
            PreparedStatement ps = connection.prepareStatement(sql);

            ps.setString(1, title);
            ps.setString(2, description);
            ps.setString(3, category);
            ps.setFloat(4, price);
            ps.setString(5, image);

            ps.executeUpdate();
            connection.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void deleteProduct(int id) {
        String sql = "DELETE FROM products WHERE id = ?";

        try {
            Connection connection = DriverManager.getConnection(DB_URL, DB_USER, DB_PASS);
            PreparedStatement ps = connection.prepareStatement(sql);
            ps.setInt(1, id);
            ps.executeUpdate();
            connection.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
