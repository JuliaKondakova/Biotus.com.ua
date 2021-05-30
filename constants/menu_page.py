"""Store locators and useful constants"""
#  Menu locators
MENU_BUTTON_XPATH = "//div[@class='button-menu']"
CATEGORY_BUTTON_XPATH = '//li[@class="level0 nav-4 category-item level-top parent"]'
SUBCATEGORY_BUTTON_XPATH = '//span[@class="item_portal_category" and contains(text(),"Омега 3 6 9")]'
ITEM_XPATH = '//a[@class="product-item-link" and contains(text(),"Рыбий жир, Омега 3 6 9 (EFA, Omega 3-6-9), ' \
             'Solgar, 1300 мг, 120 капсул")]'

#  Add to cart locators
ADD_TO_CART_BUTTON_XPATH = '//button[@id="product-addtocart-button"]'

ADDED_TO_CART_TEXT = 'Рыбий жир, Омега 3 6 9 (EFA, Omega 3-6-9), Solgar, 1300 мг, 120 капсул'
ADDED_TO_CART_XPATH = f'//a[contains(text(),"{ADDED_TO_CART_TEXT}")]'

# Add to wishlist locators
ADD_TO_WISHLIST_XPATH = '//a[@href="https://biotus.com.ua/wishlist/"]'
# '//a[@class="link-wishlist" and @data-action="add-to-wishlist"]'
WISHLIST_BUTTON_XPATH = '//*[contains(text(),"Мои списки желаний")]'
ADDED_TO_WISHLIST_XPATH = f'//a[@class="product-image" and @title="{ADDED_TO_CART_TEXT}"]'
