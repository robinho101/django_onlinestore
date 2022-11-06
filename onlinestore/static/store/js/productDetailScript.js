import styleChange from './script.js';
import {toBasket, offBasket, getAmountOfProduct} from './pickedProduct.js';
import {toUserSelectionModel} from '../../../../static/userEnvironment/js/basket.js';

if (document.querySelector('.left-arw')) {
styleChange(".left-arw", ".other-item-card", "left", 270);
styleChange(".right-arw", ".other-item-card", "right", 270);
}

getAmountOfProduct("http://127.0.0.1:8000/product-in-basket-to-model/", ".span-amount-of-product");
getAmountOfProduct("http://127.0.0.1:8000/toUserSelectionModel/", ".span-amount-of-product_in_user_selection");

function toViewedItemsModel(){
    document.addEventListener('DOMContentLoaded', async (e)=>{
    let url = 'http://127.0.0.1:8000/to-viewed-items-model/';

    let title = document.querySelector('.title').textContent;
    let description = document.querySelector('.title').nextElementSibling.nextElementSibling.textContent;
    let price = document.querySelector('button').getAttribute('data-price');
    let image = document.querySelector('.picture').getAttribute('src');
    image = image.slice(7,);
    let csrf_token = document.querySelector('.form_product_in_basket_to_model')[name="csrfmiddlewaretoken"].value;

    let data = {
        'title':title,
        'description':description,
        'price':price,
        'image':image,
        'csrf_token':csrf_token
    }

    let fetchData = {
      method: "POST",
      credentials: "same-origin",
      body: JSON.stringify(data),
      headers: new Headers({
        "Content-Type": "application/json; charset=UTF-8",
        'X-CSRFToken': csrf_token,
      }),
    };
    await fetch(url,fetchData).then(function(data){
        if(!data.ok) {
            throw Error(data.status);
        }
        return;
    })
    });
}

toViewedItemsModel();