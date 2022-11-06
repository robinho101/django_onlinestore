import {toBasket, offBasket, getAmountOfProduct} from '../../../../static/store/js/pickedProduct.js';

if(document.location.pathname=='/basket/'){
    if(document.querySelector('.basket-empty').textContent.includes('Корзина пуста')) {
    document.querySelector('.second-product_list_wrapper').style.top=-840+'px';
    }else {
    document.querySelector('.second-product_list_wrapper').style.top='';
};
}


function toUserSelectionModel(){
if(document.querySelector('.toUserSelection')) {
    let url = 'http://127.0.0.1:8000/toUserSelectionModel/';
    let toUserSelectionButtons = document.querySelectorAll('.toUserSelection');
    toUserSelectionButtons.forEach((elem)=>{
    elem.addEventListener('click', async (e)=>{
    e.preventDefault();
    if(elem.classList.contains('toUserSelectionGreen')) {
    elem.classList.remove('toUserSelectionGreen')
    elem.textContent='в избранное';
    } else {
    elem.classList.add('toUserSelectionGreen');
    elem.textContent='добавлено';
    }
    let price = elem.getAttribute("data-price");
    let image = elem.getAttribute("data-image");
    image = image.slice(7,);
    let product = elem.getAttribute("data-product");
    let csrf_token = document.querySelector(
        ".form_product_in_basket_to_model"
      )[(name = "csrfmiddlewaretoken")].value;
    let data = {
    'price':price,
    'image':image,
    'product':product,
    "csrfmiddlewaretoken": csrf_token
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
    await fetch(url, fetchData).then((data)=>{
        if(!data.ok){
        throw Error(data.status);
        }
        return data.json()
    }).then((data)=>{
        document.querySelector('.span-amount-of-product_in_user_selection').textContent=data.amount_of_product.number__sum;
        });
    });
    });
}
}



function counter(){
    let item_res = 0;
    document.querySelectorAll('.amount-wrapper').forEach((elem)=>{
    item_res+=Number(elem.value);
    });
    document.querySelector('.your_basket').textContent = 'товаров в вашей корзине - ' + item_res;

    let price_res = 0;
    document.querySelectorAll('.result-in-item-wrapper').forEach((elem)=>{
    price_res+=Number(elem.textContent);
    });
    document.querySelector('.overall_price').textContent = 'общая стоимость - ' + price_res;
    let overall_price = document.querySelector('.overall_price').textContent.replace(/[^0-9]/g,"");
    document.querySelector('.to-pay-btn').setAttribute('href','http://127.0.0.1:8000/buy/'+overall_price);
}

if (document.querySelector('.products-wrapper')) {

document.querySelector('#selectAll').addEventListener('click', (e)=>{
let itemInputCollection = document.querySelectorAll('#item_input');
itemInputCollection.forEach((elem)=>{
if(document.querySelector('#selectAll').checked) {
elem.checked = true;
} else {
elem.checked = false;
}
})
})


window.addEventListener('scroll', (e)=>{
if(document.querySelectorAll('.item-wrapper')[document.querySelectorAll('.item-wrapper').length-1].offsetTop <= window.pageYOffset+55){
document.querySelector('.go-to-pay-wrapper').style.position = 'relative';
 document.querySelector('.go-to-pay-wrapper').style.width = 514 + 'px';
} else if(window.pageYOffset>0) {
    document.querySelector('.go-to-pay-wrapper').style.width = 514 + 'px';
    document.querySelector('.go-to-pay-wrapper').style.position = 'fixed';
    document.querySelector('.go-to-pay-wrapper').style.right = 115 + 'px';
} else {
document.querySelector('.go-to-pay-wrapper').style.right = 0 + 'px';
document.querySelector('.go-to-pay-wrapper').style.position = 'relative';
 document.querySelector('.go-to-pay-wrapper').style.width = 514 + 'px';
}
})

let handler = (e)=>{
    e.preventDefault();
    if(event.target.className == 'amount-wrapper') {
    event.target.offsetParent.previousElementSibling.textContent = Number(event.target.value) * Number(event.target.offsetParent.previousElementSibling.previousElementSibling.previousElementSibling.previousElementSibling.textContent);
    counter();
    } else {
    let item_collections = document.querySelectorAll('.item-wrapper');

    for(let item of item_collections){
        item.querySelector('.result-in-item-wrapper').textContent = Number( item.querySelector('.price-wrapper').textContent)* Number( item.querySelector('.amount-wrapper').value);
        }
    counter();
    }
}
document.addEventListener('DOMContentLoaded', handler);

function afterDOMContentLoaded(){
document.querySelectorAll('.amount-wrapper').forEach((elem)=>{
elem.addEventListener('input', handler)
})
}

document.querySelector('.delete_all_span').addEventListener('click', (e)=>{
    let itemInputCollection = document.querySelectorAll('#item_input');
    itemInputCollection.forEach((elem)=>{
    if(elem.checked) {
    let mainParent = elem.offsetParent.offsetParent;
    mainParent.querySelector('.out_of_basket').click();
    }
    })
    counter()
})

document.querySelector('.to-pay-btn').addEventListener('click', (e)=>{
let order_id = String(Math.floor(Math.random() * 1000000));
document.querySelectorAll('.item-wrapper').forEach(async (elem)=>{
let url = 'http://127.0.0.1:8000/to-purchased-items-model/';
let item = {};
item.order_id = order_id;
item.title = elem.querySelector('.title').textContent;
item.price = elem.querySelector('.price-wrapper').textContent;
item.amount = elem.querySelector('.amount-wrapper').value;
item.image = elem.querySelector('img').getAttribute('src').slice(7,);
item.csrf_token = document.querySelector(".form_product_in_basket_to_model")[(name = "csrfmiddlewaretoken")].value;
let fetchData = {
method: "POST",
credentials: "same-origin",
body: JSON.stringify(item),
headers: new Headers({
  "Content-Type": "application/json; charset=UTF-8",
  "X-CSRFToken": item.csrf_token,
}),
};
await fetch(url, fetchData).then((data)=>{
if(!data.ok){
throw Error(data.status);
} else {
console.log(data.status)
for (let item of document.querySelectorAll('.item-wrapper')) {
    item.querySelector('.out_of_basket').click();
}
}
});
});
});




afterDOMContentLoaded()
}

toUserSelectionModel()

getAmountOfProduct("http://127.0.0.1:8000/product-in-basket-to-model/", ".span-amount-of-product");
getAmountOfProduct("http://127.0.0.1:8000/toUserSelectionModel/", ".span-amount-of-product_in_user_selection");


export {counter, toUserSelectionModel};