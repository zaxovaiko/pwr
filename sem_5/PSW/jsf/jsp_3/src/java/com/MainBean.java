/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com;

import javax.faces.bean.ManagedBean;
import javax.faces.bean.RequestScoped;

/**
 *
 * @author volodymyr
 */
@ManagedBean(name="main")
@RequestScoped
public class MainBean {
    public String rabat = "-20%";
    
    public String getRabat() {
        return rabat;
    }
}
