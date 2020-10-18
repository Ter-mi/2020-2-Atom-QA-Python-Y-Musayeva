from selenium.webdriver.common.by import By


class AuthLocators:
    ENTER_BUTTON = (By.CLASS_NAME, 'responseHead-module-button-1BMAy4')
    EMAIL = (By.NAME, 'email')
    PASSWORD = (By.NAME, 'password')


class MainLocators:

    USER_NAME = (By.CLASS_NAME, 'right-module-userNameWrap-34ibLS')
    CAMPAIGN_NAME = (By.XPATH, '//a[@class="campaigns-tbl-cell__campaign-name"]')
    SEARCH_CAMPAIGN = (By.XPATH, '//input[contains(@class,"searchInput")]')
    CAMPAIGN_SUGGESTION = (By.XPATH, '//span[@class="suggester-ts__item__name"]')
    CAMPAIGN_LIST = (By.XPATH, '//a[@href="/campaigns/full"]')
    HEADER_BUTTON_CREATE_CAMPAIGN = (By.XPATH, '//div[@class="dashboard-module-createButtonWrap-UufRCB"]')
    LINK_CREATE_CAMPAIGN = (By.XPATH, '//a[@href="/campaign/new"]')
    TRAFFIC_TYPE = (By.XPATH, '//div[@class="column-list-item _traffic"]')
    LINK_FIELD = (By.XPATH, '//input[@data-gtm-id="ad_url_text"]')
    NAME_FIELD = (By.XPATH, '//div[@class="input input_campaign-name input_with-close"]//input')
    BANNER = (By.ID, 'patterns_4')
    UPLOAD_ELEMENT = (By.XPATH, '//input[@data-test="image_240x400"]')
    SAVE_PIC = (By.XPATH, '//input[@class ="image-cropper__save js-save"]')
    BUTTON_ADD_ADS = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[6]/div/div[4]/div/div[3]/div[1]/div')
    BUTTON_CREATE_CAMPAIGN = (By.XPATH, '//div[@class="footer"]//button[@class="button button_submit"]')

    BUTTON_SEGMENTS = (By.XPATH, '//a[contains(@href, "/segments")]')
    LINK_FIRST_SEGMENT = (By.XPATH, '//a[@href="/segments/segments_list/new/"]')
    BUTTON_CREATE_SEGMENT = (By.CLASS_NAME, 'button__text')
    ADD_SEGMENTS = (By.XPATH, '//span[@data-translated="Add audience segments..."]')
    OPTION_SEGMENT = (By.XPATH, '//div[contains(text(), "Приложения ")]')
    
    FIRST_CHECKBOX = (By.XPATH, '//input[contains(@class, "adding-segments-source__checkbox js-main-source-checkbox")]')
    BUTTON_LIST = (By.XPATH, '//div[@class="adding-segments-source__text-top"]')
    SECOND_CHECKBOX = (By.XPATH, '//input[contains(@class, "segment-settings-view__checkbox js-payer-checkbox-pay")]')
    BUTTON_ADD_SEGMENT = (By.XPATH, '//div[@class="adding-segments-modal__btn-wrap js-add-button"]/button')
    SEGMENT_NAME_FIELD = (By.XPATH, '//div[@class="input input_create-segment-form"]//input')
    BUTTON_CONFIRM_SEGMENT = (By.XPATH, '//div[contains(text(), "Создать сегмент")]')
    SEGMENT_NAME = (By.XPATH, '//a[@class="adv-camp-cell adv-camp-cell_name"]')
    SPAN_ONE_OF_ONE=(By.XPATH, '//span[@class="pagination-module-pages-2t7wfR"]')
    BUTTON_SORT = (By.XPATH, '//div[@data-group-id="created"]/span')
    SEARCH_SEGMENT = (By.XPATH, '//input[contains(@class,"suggester-module-searchInput-1dyLvN")]')
    DELETE_BUTTON = (By.XPATH, '//span[contains(@class,"icon-cross")]')
    CONFIRM_DELETE = (By.XPATH, '//button[@class="button button_confirm-remove button_general"]')
    SEARCH_SUGGESTION = (By.XPATH, '//li[contains(@class,"suggester-module-option-1kQRIM")]')
    EMPTY_SUGGESTION = (By.XPATH, '//li[@class="suggester-ts__item_empty-text suggester-ts__item"]')
    SEGMENT_COUNTER = (By.XPATH, '//a[@href="/segments/segments_list"]//span[@class="left-nav__count js-nav-item-count"]')
    SUGGESTION_ID = (By.XPATH, '//span[contains(@class, "adv-camp-cell adv-camp-cell_name")]')
