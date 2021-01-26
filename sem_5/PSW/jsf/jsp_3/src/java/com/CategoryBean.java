/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com;

import javax.faces.bean.ManagedBean;
import javax.faces.bean.RequestScoped;
import javax.faces.bean.SessionScoped;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

/**
 *
 * @author volodymyr
 */
@ManagedBean(name="categories", eager = true)
@SessionScoped
@RequestScoped
public class CategoryBean {
    public boolean isFiltering = false;
    public String[] categories = {"phone", "gadget", "laptop"};
    public String category = "";

    public CategoryBean() {
    }

    public String[] getCategories() {
        return categories;
    }

    public List<Product> getShowFilteredProducts() {
        List<Product> allProducts = new ProductBean().getProducts();
        return allProducts.stream().filter(p -> p.getCategory().equals(category)).collect(Collectors.toList());
    }

    public void setFiltering() {
        setIsFiltering(true);
        setCategory(category);
    }

    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }

    public void setIsFiltering(boolean filtering) {
        isFiltering = filtering;
    }

    public boolean getIsFiltering() {
        return isFiltering;
    }
}
