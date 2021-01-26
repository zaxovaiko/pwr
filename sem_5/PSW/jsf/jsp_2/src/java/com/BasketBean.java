package com;

import java.io.Serializable;
import java.util.*;
import javax.faces.bean.ManagedBean;
import javax.faces.bean.SessionScoped;
import javax.faces.context.FacesContext;

@ManagedBean(name = "selectionsBean")
@SessionScoped
public class BasketBean implements Serializable {
    private static final HashMap<String, String> productsMap = new HashMap<>();

    private final HashMap<String, String[]> selections = new HashMap<>();
    private final HashMap<String, Double> prices = new HashMap<>();
    private String selection;

    public String formDelivery;
    public String paymentMethod;

    public BasketBean() {
        FacesContext.getCurrentInstance().getExternalContext().setSessionMaxInactiveInterval(1200);

        productsMap.put("1", "Mi Bend 3");
        productsMap.put("2", "Lenovo 320s");
        productsMap.put("3", "Samsung M51");
        productsMap.put("4", "Huawei X65");

        prices.put("1", 54.0);
        prices.put("2", 123.50);
        prices.put("3", 870.90);
        prices.put("4", 500.0);
    }

    public double getOrderItems() {
        double totalSum = 0;

        HashMap<String, Double> deliv = new HashMap<>();
        deliv.put("courier", 10.0);
        deliv.put("postoffice", 6.0);
        deliv.put("pickup", 2.0);

        totalSum += deliv.get(formDelivery);

        for (Map.Entry<String, String[]> item : selections.entrySet()) {
            String key = item.getKey();
            String[] value = item.getValue();
            int numberOfItems = Integer.parseInt(value[1]);
            totalSum += prices.get(key) * numberOfItems;

        }

        selections.clear();
        return totalSum;
    }

    public String getFormDelivery() {
        return formDelivery;
    }

    public void setFormDelivery(String formDelivery) {
        this.formDelivery = formDelivery;
    }

    public String getPaymentMethod() {
        return paymentMethod;
    }

    public void setPaymentMethod(String paymentMethod) {
        this.paymentMethod = paymentMethod;
    }

    public int getNumberOfSelections() {
        System.out.println();
        int number = 0;
        Object[] items = selections.values().stream().map(e -> e[1]).toArray();
        for (Object item : items) {
            number += Integer.parseInt((String) item);
        }
        return number;
    }

    public String getSelection() {
        return selection;
    }

    public void setSelection(String id) {
        selection = productsMap.get(id);
        if (selections.containsKey(id)) {
            String[] temp = selections.get(id);
            Integer items = Integer.parseInt(temp[1]) + 1;
            selections.put(id, new String[]{selection, items + ""});
            return;
        }
        selections.put(id, new String[]{selection, "1"});
    }

    public Object[] getSelections() {
        return selections.values().toArray();
    }
} 