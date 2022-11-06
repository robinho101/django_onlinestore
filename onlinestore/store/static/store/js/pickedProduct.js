import {counter, toUserSelectionModel} from '../../../../static/userEnvironment/js/basket.js';

if(document.location.pathname.includes('/picked-product/')){
document.querySelector('.form-select').addEventListener('change', async(e)=>{
let sort_by = document.querySelectorAll('.sort_by_price')[e.target.value-1].textContent;
if(sort_by.includes('по убыванию')){
sort_by = '-';
}else {
sort_by = '';
}
let url = document.location.href
let csrf_token = document.querySelector('.form_product_in_basket_to_model')[name="csrfmiddlewaretoken"].value;
let data = {
'sort_by':sort_by,
'csrf_token':csrf_token
}
let fetchData = {
  method: "POST",
  credentials: "same-origin",
  body: JSON.stringify(data),
  headers: new Headers({
    "Content-Type": "application/json; charset=UTF-8",
    "X-CSRFToken": csrf_token,
  }),
};

await fetch (url, fetchData).then((data)=>{
if (!data.ok) {
          throw Error(data.status);
        }else {
        console.log(data.status)
        }
})
location.href=document.location.href;
});
}

function getAmountOfProduct(urlAdrs, classSelector) {
  document.addEventListener("DOMContentLoaded", async (e) => {
    let url = urlAdrs;
    try{
    let user = document.querySelector(".user").textContent;

    let csrf_token = document.querySelector('.form_product_in_basket_to_model')[name="csrfmiddlewaretoken"].value;
    let data = {
      "user": user,
      "csrfmiddlewaretoken":csrf_token
    };
    let fetchData = {
      method: "POST",
      credentials: "same-origin",
      body: JSON.stringify(data),
      headers: new Headers({
        "Content-Type": "application/json; charset=UTF-8",
        "X-CSRFToken": csrf_token,
      }),
    };
    await fetch(url, fetchData)
      .then(function (data) {
        if (!data.ok) {
          throw Error(data.status);
        }
        return data.json();
      })
      .then((data) => {
      if(data.products_in_user_selection) {
        data.products_in_user_selection.forEach((elem)=>{
          for (let item of document.querySelectorAll('.title')) {
          if (elem.includes(item.textContent)) {
            item.offsetParent.offsetParent.querySelector('.toUserSelection').classList.add('toUserSelectionGreen');
            item.offsetParent.offsetParent.querySelector('.toUserSelection').textContent= 'добавлено';
          }
          if (elem.includes(item.textContent) && item.offsetParent.querySelector('.toUserSelection')) {
            item.offsetParent.querySelector('.toUserSelection').classList.add('toUserSelectionGreen')
            item.offsetParent.querySelector('.toUserSelection').textContent= 'добавлено';
          }
          }
        })
        }

        if(data.products_in_basket) {
            data.products_in_basket.forEach((elem)=>{
        for(let item of document.querySelectorAll('.title')) {
            if(elem.includes(item.textContent) && item.offsetParent.offsetParent.querySelector('.in_basket')) {
            item.offsetParent.offsetParent.querySelector('.in_basket').style.display ='none';
            item.offsetParent.offsetParent.querySelector('.in_basket').nextElementSibling.style.display ='block';
            }
        }
        })
        }
        if (classSelector) {
          document.querySelector(classSelector).textContent =
          data.amount_of_product.number__sum;
}
      });
    } catch(err){
        console.log(err);
    }
  });
}


////////

function toBasket(){
let url = "http://127.0.0.1:8000/product-in-basket-to-model/";
document.querySelectorAll(".in_basket").forEach((elem) => {
  elem.addEventListener("click", async (e) => {
    e.preventDefault();
    elem.nextElementSibling.nextElementSibling.style.display = "block";
    elem.textContent = "";
    try {
    let user = document.querySelector(".user").textContent;
    let amount = elem.offsetParent.previousElementSibling.value
    let product = elem.getAttribute("data-product");
    let price_per_item = elem.getAttribute("data-price");
    let image = elem.getAttribute("data-image");
    image = image.slice(7,);
    let csrf_token = document.querySelector('.form_product_in_basket_to_model')[name="csrfmiddlewaretoken"].value;

    let data = {
      "user": user,
      "product": product,
      "amount":amount,
      "price_per_item": price_per_item,
      "image": image,
      "csrfmiddlewaretoken":csrf_token
    };
    let fetchData = {
      method: "POST",
      credentials: "same-origin",
      body: JSON.stringify(data),
      headers: new Headers({
        "Content-Type": "application/json; charset=UTF-8",
        'X-CSRFToken': csrf_token,
      }),
    };
    await fetch(url, fetchData).then(function (data) {
      if(!data.ok){
        throw Error(data.status);
      }
      return data.json();
    }).then(data=>{
        document.querySelector('.span-amount-of-product').textContent=data.amount_of_product.number__sum;
    });
    elem.style.display = 'none';
    elem.textContent = "в корзину";
    elem.nextElementSibling.nextElementSibling.style.display = "none";
    elem.nextElementSibling.style.display = 'block';
    } catch(err) {
        console.log(err);
    }
  });
});
}

///////

function offBasket() {
  let url =
    "http://127.0.0.1:8000/deletion-the-products-from-model-and-basket/";

  document.querySelectorAll(".out_of_basket").forEach((elem) => {
    elem.addEventListener("click", async (e) => {
      e.preventDefault();

      if(elem.nextElementSibling){
      elem.nextElementSibling.style.display = "block";
      elem.textContent = "";
      }

      try {
      let user = document.querySelector(".user").textContent;
      let product = elem.getAttribute("data-product");
      let csrf_token = document.querySelector(
        ".form_product_in_basket_to_model"
      )[(name = "csrfmiddlewaretoken")].value;
      let data = {
        "user": user,
        "product": product,
        "csrfmiddlewaretoken": csrf_token,
      };
      let fetchData = {
        method: "POST",
        credentials: "same-origin",
        body: JSON.stringify(data),
        headers: new Headers({
          "Content-Type": "application/json; charset=UTF-8",
          "X-CSRFToken": csrf_token,
        }),
      };
      await fetch(url, fetchData).then(function (data) {
      if(!data.ok){
        throw Error(data.status);
      }
      return data.json();
    }).then(data=>{
        document.querySelector('.span-amount-of-product').textContent=data.amount_of_product.number__sum;
        if(document.querySelector('.amountOfProduct')){
        document.querySelector('.amountOfProduct').textContent=data.amount_of_product.number__sum;
        }
    });
    if(elem.offsetParent.offsetParent.className == 'item-wrapper'){
    elem.offsetParent.offsetParent.remove();
    counter();
    }

    if(elem.nextElementSibling){
      elem.style.display = "none";
      elem.textContent = "удалить";
      elem.nextElementSibling.style.display = "none";
      elem.previousElementSibling.style.display = "block";
      }
    } catch(err) {
        console.log(err);
    }
    });
  });
}

getAmountOfProduct("http://127.0.0.1:8000/product-in-basket-to-model/", ".span-amount-of-product");
getAmountOfProduct("http://127.0.0.1:8000/toUserSelectionModel/", ".span-amount-of-product_in_user_selection");
toBasket()
offBasket()

export {toBasket, offBasket, getAmountOfProduct};