/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com;

import com.dao.ProductDAO;

import java.io.IOException;
import java.util.List;
import javax.faces.bean.ManagedBean;
import javax.faces.bean.RequestScoped;
import javax.faces.context.ExternalContext;
import javax.faces.context.FacesContext;

/**
 * @author volodymyr
 */
@ManagedBean(name = "products", eager = true)
@RequestScoped
public class ProductBean {
    public ProductDAO productDAO = new ProductDAO();
    public List<Product> products;
    public String[] orderedProduct = new String[]{"4", "Huawei X65", "One advanced diverted domestic sex repeated bringing you old. Possible procured her trifling laughter thoughts property she met way. Companions shy had solicitude favourable own. Which could saw guest man now heard but. Lasted my coming uneasy marked so should. Gravity letters it amongst herself dearest an windows by. Wooded ladies she basket season age her uneasy saw. Discourse unwilling am no described dejection incommode no listening of. Before nature his parish boy.", "https://via.placeholder.com/250x400", "4"};

    public String title;
    public String description;
    public float price;
    public String category;
    public String image;

    public void addProduct() throws IOException {
        productDAO.addProduct(title, description, category, price, image);
        ExternalContext ec = FacesContext.getCurrentInstance().getExternalContext();
        ec.redirect(ec.getRequestContextPath() + "/crud.xhtml");
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public String getPrice() {
        return price + "";
    }

    public void setPrice(String price) {
        this.price = (float) Double.parseDouble(price);
    }

    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }

    public String getImage() {
        return image;
    }

    public void setImage(String image) {
        this.image = image;
    }

    public ProductBean() {
        this.products = productDAO.getAllProducts();
    }

    public List<Product> getProducts() {
        return products;
    }

    public void deleteProduct(int id) throws IOException {
        productDAO.deleteProduct(id);
        ExternalContext ec = FacesContext.getCurrentInstance().getExternalContext();
        ec.redirect(ec.getRequestContextPath() + "/crud.xhtml");
    }

    public List<Product> getAll() {
        return products;
    }

    public List<Product> getRecentProducts() {
        return products;
    }

    public String[] getOrderedProduct() {
        return orderedProduct;
    }
}
