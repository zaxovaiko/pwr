package com.validators;

import com.ProductBean;

import javax.faces.application.FacesMessage;
import javax.faces.bean.ManagedBean;
import javax.faces.bean.SessionScoped;
import javax.faces.component.UIComponent;
import javax.faces.context.FacesContext;
import javax.faces.validator.FacesValidator;
import javax.faces.validator.Validator;
import javax.faces.validator.ValidatorException;

@ManagedBean
@SessionScoped
@FacesValidator("orderValidator")
public class OrderValidator implements Validator {

    @Override
    public void validate(FacesContext fc, UIComponent uic, Object value) throws ValidatorException {
        if (value.equals("")) {
            throw new ValidatorException(new FacesMessage("Item can not be empty"));
        }
    }

    public void validateNumber(FacesContext fc, UIComponent uic, Object value) throws ValidatorException {
        String[] orderedProduct = new ProductBean().orderedProduct;

        try {
            Integer.parseInt((String) value);
        } catch (NumberFormatException e) {
            throw new ValidatorException(new FacesMessage("Only digits allowed"));
        }

        if (Integer.parseInt((String) value) > Integer.parseInt(orderedProduct[4])) {
            throw new ValidatorException(new FacesMessage("There is no as many items to sell"));
        }
    }
}
