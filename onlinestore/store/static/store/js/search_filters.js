document.querySelector('.background-image-wrapper').style.minHeight = document.querySelector('.filter_wrapper').offsetHeight + 200 + 'px';

function inputTypeRangeAndInputTypeTextSetValue(selector) {
  document.querySelector(selector).value = Math.round(event.target.value);
}
document.querySelector(".price_filter_min").addEventListener("change", ()=> inputTypeRangeAndInputTypeTextSetValue(".input-min-price"));
document.querySelector(".price_filter_max").addEventListener("change", ()=> inputTypeRangeAndInputTypeTextSetValue(".input-max-price"));
document.querySelector(".input-min-price").addEventListener("change", ()=> inputTypeRangeAndInputTypeTextSetValue(".price_filter_min"));
document.querySelector(".input-max-price").addEventListener("change", ()=> inputTypeRangeAndInputTypeTextSetValue(".price_filter_max"));

///////////

function minMaxValue(minSelector, maxSelector, minSelector2) {
    if (Math.round(document.querySelector(minSelector).value) > Math.round(document.querySelector(maxSelector).value)) {
        document.querySelector(minSelector).value = Math.round(document.querySelector(maxSelector).value - 1000);
        document.querySelector(minSelector2).value = Math.round(document.querySelector(maxSelector).value - 1000);
    }
}
document.querySelector('.price_filter_min').addEventListener('change', ()=>minMaxValue('.price_filter_min', '.price_filter_max', '.input-min-price'));
document.querySelector('.price_filter_max').addEventListener('change', ()=>minMaxValue('.price_filter_min', '.price_filter_max', '.input-min-price'));
document.querySelector('.input-min-price').addEventListener('change', ()=>minMaxValue('.input-min-price', '.input-max-price', '.price_filter_min'));
document.querySelector('.input-max-price').addEventListener('change', ()=>minMaxValue('.input-min-price', '.input-max-price', '.price_filter_min'));

//////////



document.querySelector('.accept_filters').addEventListener('click',async (e)=>{
if(location.href.includes('/picked-product/')) {
let priceMin = Number(document.querySelector('.input-min-price').value);
let priceMax = Number(document.querySelector('.input-max-price').value);
let csrf_token = document.querySelector('.form_product_in_basket_to_model')[name="csrfmiddlewaretoken"].value;
let url = document.location.href
let data = {
    'search_filter': true,
    'csrf_token': csrf_token,
    'priceMin': priceMin,
    'priceMax': priceMax,
    'other_filters': {
    }
};
document.querySelectorAll('.filter-input').forEach((elem)=>{
    if(elem.checked) {
    let elemObj = elem.dataset;
    let nameProp = elemObj.name;
    if(data['other_filters'][nameProp]) {
            data['other_filters'][nameProp].push(elemObj.value);
    } else {
            data['other_filters'][nameProp] = [elemObj.value];
        }
    }
});
console.log(data);
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
location.reload();
}
});






