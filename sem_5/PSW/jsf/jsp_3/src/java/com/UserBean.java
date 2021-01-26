package com;

import com.dao.UserDAO;

import javax.faces.bean.ManagedBean;
import javax.faces.bean.SessionScoped;
import javax.faces.context.ExternalContext;
import javax.faces.context.FacesContext;
import java.io.IOException;

@ManagedBean(name = "loggedUser", eager = true)
@SessionScoped
public class UserBean {
    public User user;
    public String email;
    public String password;
    public String messageError;
    public boolean isLoggedIn = false;

    public String getEmail() {
        return email;
    }

    public void login() {
        UserDAO userDAO = new UserDAO();
        User user = userDAO.getUserByEmail(email);

        if (user != null && user.getPassword().equals(password)) {
            isLoggedIn = true;
            this.user = user;
        } else {
            messageError = "Invalid data.";
        }
    }

    public void checkAlreadyLoggedIn() throws IOException {
        if (isLoggedIn) {
            ExternalContext ec = FacesContext.getCurrentInstance().getExternalContext();
            ec.redirect(ec.getRequestContextPath() + "/index.xhtml");
        }
    }

    public void checkIsGuest() throws IOException {
        if (!isLoggedIn) {
            ExternalContext ec = FacesContext.getCurrentInstance().getExternalContext();
            ec.redirect(ec.getRequestContextPath() + "/index.xhtml");
        }
    }

    public String getMessageError() {
        return messageError;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public UserBean() {
    }

    public void logout() {
        user = null;
        isLoggedIn = false;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

    public boolean getIsLoggedIn() {
        return isLoggedIn;
    }

    public void setIsLoggedIn(boolean isLoggedIn) {
        this.isLoggedIn = isLoggedIn;
    }
}
