import {getAmountOfProduct} from './pickedProduct.js';


window.addEventListener('scroll', (e)=>{
    if(window.pageYOffset>0){
        document.querySelector('header').style.position = 'fixed';
    }   else {
    document.querySelector('header').style.position = '';
    }
});


function styleChange(selector1, selector2, styleName, styleValue) {
  document.querySelector(selector1).addEventListener("click", (e) => {

    let stName = styleName,
      stValue = styleValue;


    if (stName == "left") {
      document.querySelector('.left-arw').style.display = 'block';
      document.querySelector('.right-arw').style.display = 'block';
      let current = document.querySelector(selector2).style[stName].replace(/\D/g,'');
      let res = -Number(current) - stValue;
      document.querySelectorAll(selector2).forEach((elem, index)=>{
      if(document.querySelectorAll('.other-item-card')[document.querySelectorAll('.other-item-card').length-1].offsetLeft == 1082) {
        document.querySelector('.left-arw').style['display'] = 'None';
        return;
      } else {
        elem.style['right'] ='';
        elem.style[stName] =String(res)+'px';
        if(document.querySelectorAll('.other-item-card')[document.querySelectorAll('.other-item-card').length-1].offsetLeft == 1082) {
        document.querySelector('.left-arw').style['display'] = 'None';
        return;
      }
      }
      })
      return;
    } else if (stName == "right") {
      document.querySelector('.left-arw').style['display'] = 'block';
      document.querySelector('.right-arw').style['display'] = 'block';
      let current = document.querySelector(selector2).style[stName].replace(/\D/g,'');
      let res = Number(current) + stValue;
            document.querySelectorAll(selector2).forEach((elem, index)=>{
      if(document.querySelectorAll('.other-item-card')[0].offsetLeft == 2) {
        document.querySelector('.right-arw').style['display'] = 'None';
        return;
      } else {
        elem.style['left'] ='';
        elem.style[stName] =-String(res)+'px';
      if(document.querySelectorAll('.other-item-card')[1].offsetLeft == 2) {
        document.querySelector('.right-arw').style['display'] = 'None';
        return;
      }
      }
      })
      return;
    } else if (document.querySelector(selector2).style[stName] == stValue) {
      document.querySelector(selector2).style[stName] = "";
    } else {
      document.querySelector(selector2).style[stName] = stValue;
    }
  });
}

document.querySelector('.search-submit-block').addEventListener('click', async (e)=>{
    let text;
    if (document.querySelector('#item-search-input').value) {
        text = document.querySelector('#item-search-input').value
    } else {
        return;
    }
    let url = 'http://127.0.0.1:8000/search-result/';
    let selectedCategoryId;
    let csrf_token = document.querySelector('.form_product_in_basket_to_model')[name="csrfmiddlewaretoken"].value;
    document.querySelectorAll('option').forEach((elem)=>{
    if(elem.selected) {
        if(elem.previousSibling.data.replace(/\D+/g,"")){
           selectedCategoryId = Number(elem.previousSibling.data.replace(/\D+/g,""));
        } else {
            selectedCategoryId='';
        }
    }
    });

    let data = {
    'selectedCategoryId':selectedCategoryId,
    'text':text,
    "csrfmiddlewaretoken":csrf_token
    }
    let fetchData = {
      method: "POST",
      credentials: "same-origin",
      body: JSON.stringify(data),
      headers: new Headers({
        "Content-Type": "application/json; charset=UTF-8",
        "X-CSRFToken": csrf_token,
      }),
    }
    await fetch(url, fetchData).then((data)=>{
        if (!data.ok) {
          throw Error(data.status);
        }
    })
    location.href='http://127.0.0.1:8000/search-result/';
});

styleChange(".search-dropdown", ".search-select", "opacity", 1);

getAmountOfProduct("http://127.0.0.1:8000/product-in-basket-to-model/", ".span-amount-of-product");
getAmountOfProduct("http://127.0.0.1:8000/toUserSelectionModel/", ".span-amount-of-product_in_user_selection");
//////////



export default styleChange;