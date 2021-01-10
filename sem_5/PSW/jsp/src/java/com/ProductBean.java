/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com;

import java.util.ArrayList;
import javax.faces.bean.ManagedBean;
import javax.faces.bean.RequestScoped;

/**
 * @author volodymyr
 */
@ManagedBean(name = "products", eager = true)
@RequestScoped
public class ProductBean {
    public ArrayList<String[]> recentProducts = new ArrayList<>();
    public String[] orderedProduct = new String[]{"4", "Huawei X65", "One advanced diverted domestic sex repeated bringing you old. Possible procured her trifling laughter thoughts property she met way. Companions shy had solicitude favourable own. Which could saw guest man now heard but. Lasted my coming uneasy marked so should. Gravity letters it amongst herself dearest an windows by. Wooded ladies she basket season age her uneasy saw. Discourse unwilling am no described dejection incommode no listening of. Before nature his parish boy.", "https://via.placeholder.com/250x400"};

    public ProductBean() {
        recentProducts.add(new String[]{"1", "Mi Bend 3", "https://via.placeholder.com/250x550"});
        recentProducts.add(new String[]{"2", "Lenovo 320s", "https://via.placeholder.com/250x550"});
        recentProducts.add(new String[]{"3", "Samsung M51", "https://via.placeholder.com/250x550"});
        recentProducts.add(new String[]{"4", "Huawei X65", "https://via.placeholder.com/250x550"});
    }

    public ArrayList<String[]> getRecentProducts() {
        return recentProducts;
    }

    public String[] getOrderedProduct() {
        return orderedProduct;
    }

    public double getRandomProductPrice() {
        return Math.round(Math.random() * 100000) / 100.0;
    }
}
