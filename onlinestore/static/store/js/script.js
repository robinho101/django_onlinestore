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
      document.querySelector('.left-arw').style['display'] = 'block';
      document.querySelector('.right-arw').style['display'] = 'block';
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

styleChange(".search-dropdown", ".search-select", "opacity", 1);

getAmountOfProduct("http://127.0.0.1:8000/product-in-basket-to-model/", ".span-amount-of-product");
getAmountOfProduct("http://127.0.0.1:8000/toUserSelectionModel/", ".span-amount-of-product_in_user_selection");
//////////



export default styleChange;