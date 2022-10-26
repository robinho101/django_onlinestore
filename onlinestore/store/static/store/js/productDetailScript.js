import styleChange from './script.js';
import {toBasket, offBasket, getAmountOfProduct} from './pickedProduct.js';
import {toUserSelectionModel} from '../../../../static/userEnvironment/js/basket.js';

styleChange(".left-arw", ".other-item-card", "left", 270);
styleChange(".right-arw", ".other-item-card", "right", 270);

getAmountOfProduct("http://127.0.0.1:8000/product-in-basket-to-model/", ".span-amount-of-product");
getAmountOfProduct("http://127.0.0.1:8000/toUserSelectionModel/", ".span-amount-of-product_in_user_selection");
