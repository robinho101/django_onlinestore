import {toBasket, offBasket, getAmountOfProduct} from '../../../../static/store/js/pickedProduct.js';
//import {toUserSelectionModel} from './basket.js';

getAmountOfProduct("http://127.0.0.1:8000/product-in-basket-to-model/", ".span-amount-of-product");
getAmountOfProduct("http://127.0.0.1:8000/toUserSelectionModel/", ".span-amount-of-product_in_user_selection");

if(document.querySelector('.for_all_div')) {
document.querySelectorAll('.toUserSelection').forEach((elem)=>{
elem.addEventListener('click', (e)=>{
elem.offsetParent.remove();
});
});
}
