package com;

import javax.faces.bean.ManagedBean;
import javax.faces.bean.RequestScoped;

@ManagedBean(name = "user", eager = true)
@RequestScoped
public class OrderBean {
    public String address;
    public String name;
    public String color;
    public String comment;
    public String formDelivery;
    public String paymentMethod;
    public int number;
    public boolean notify;
    public boolean delivery;
    public boolean terms;

    public OrderBean() {
    }

    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    
    public String getPaymentMethod() {
        return paymentMethod;
    }

    public void setPaymentMethod(String paymentMethod) {
        this.paymentMethod = paymentMethod;
    }
    
    public String getFormDelivery() {
        return formDelivery;
    }

    public void setFormDelivery(String formDelivery) {
        this.formDelivery = formDelivery;
    }

    public boolean getTerms() {
        return terms;
    }

    public void setTerms(boolean terms) {
        this.terms = terms;
    }

    public String getAddress() {
        return address;
    }

    public String getName() {
        return name;
    }

    public String getColor() {
        return color;
    }

    public String getNumber() {
        return "" + number;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public void setNumber(String number) {
        this.number = Integer.parseInt(number);
    }

    public boolean getNotify() {
        return notify;
    }

    public void setNotify(boolean notify) {
        this.notify = notify;
    }

    public boolean getDelivery() {
        return delivery;
    }

    public void setDelivery(boolean delivery) {
        this.delivery = delivery;
    }

    public String getValidationResult() {
        return "Użytkownik " + name + " zamówił " + number + " sztuk towaru koloru " + color + " na adres " + address;
    }
}
