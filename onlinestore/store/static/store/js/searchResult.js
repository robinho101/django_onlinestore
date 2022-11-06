import {toBasket, offBasket} from './pickedProduct.js';


function searchResult(url){
if(document.querySelector('.form-select')){
document.querySelector('.form-select').addEventListener('change', async(e)=>{
let sort_by = document.querySelectorAll('.sort_by_price')[e.target.value-1].textContent;
if(sort_by.includes('по убыванию')){
sort_by = '-';
}else {
sort_by = '';
}

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
location.href=url;
});
}
}

searchResult('http://127.0.0.1:8000/search-result/')

export {searchResult};