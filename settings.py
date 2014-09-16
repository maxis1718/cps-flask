# -*- coding: utf-8 -*-

#########################
#     SITE SETTINGS     #
#########################
SITE_TITLE = {
    'zh':'CPSquare',
    'en':'CPSquare'
}
SITE_TAGLINE = {
    'zh':'3c財經發射站',
    'en':'3c財經發射站',
}



#########################
#       LANGUAGES       #
#########################

## default site language
LANG = LANGULAGE = "zh" 

## support languages
LANGUAGES = [
    {
        "url": "en",
        "name": "English"
    },
    {
        "url": "zh",
        "name": "繁體中文"
    }
]

#########################
#     SITE CONTENTS     #
#########################

INDEX_NEWS = {
    "en": "News",
    "zh": "最新消息"
}

MENU_ORDER = [
    "news", 
    "products",
    "about",
    "download",
    "contact",
    "facebook",
]

MENU = {
    "news": {
        "en": "News",
        "zh": "新聞列表",
        "url": "news"
    },
    "products": {
        "en": "Products",
        "zh": "產品",
        "url": "products"
    },
    "about": {
        "en": "About",
        "zh": "公司簡介",
        "url": "about"
    },
    "download": {
        "en": "Download",
        "zh": "軟體下載",
        "url": "download"
    },
    "contact": {
        "en": "Contact",
        "zh": "聯絡我們",
        "url": "contact"
    },
    "facebook": {
        "en": "Facebook",
        "zh": "FB粉絲團",
        "url": "https://www.facebook.com/CPsquare3C"
    },
}

## 
SEE_MORE = {
    'en': '(see more)',
    'zh': '(詳全文)'
}

CONTACT = [
    {
        "title": {
            "en": "Email",
            "zh": "電子郵件",
            "before": "fa fa-mobile" ## font-awesome icon
        },
        "type": "email",
        "content": "cpsquaretw@gmail.com",
        "url": "mailto:cpsquaretw@gmail.com",
        "before": "fa fa-envelope" ## font-awesome icon
    },
    {
        "title": {
            "en": "Cellphone",
            "zh": "手機"
        },
        "type": "phone",
        "content": "+886-982-621-414",
        "url": "skype:+886982621414?call"
    }
]

## Support Font-Awesome icons
# http://fortawesome.github.io/Font-Awesome/icons

ABOUT = {
    "en": [
        '''"CP" means cost-performance ratio which used to measure the cost of an item against its effectiveness. “Square” in math means the result of multiplying a number by itself. The name of the brand “CP Square” reveals our purpose - we want everyone get high performance gadgets at reasonable price.''',
        '''CP Square provides up to date information from MIC mobile brands to all kinds of White Box mobile. We also value your shopping experience, that’s why all the goods we sold are 100% in stock and we encourage you to come visit our store and experience by yourself.''',
        '''In order to serve our honorable customers, we create a one-stop all you can get service. Not only the mobile phones you can find at our store, but also the accessories such as, battery, phone cases, adapters…etc. You got all you need in once with CP Square.''',
        '''Our B2C Business is widely spread in Taiwan. There are many distributors carried our product in major city such as Taipei, Tao Yuan and Kaohsiung. Sales channel includes, mobile phone store, night market, grocery store and underground shopping mall. We accept customized order as well.''',
        '''Recently, we develop international B2B business in emerging markets. The first sales center locates in Makati City, Philippines.  Another sales center will open in Surabaya, Indonesia soon.''',
        '''If you have any inquires or interest in our products, please <a href="/en/contact/">contact us</a>. We are looking forward to hear from you.'''
    ],
    "zh": [
        '''CP square，CP即價格性能比，square為平方的意思，讓大家都有取得CP極高的3C產品''',
        '''除了提供最即時透明的國牌，白牌手機報價資訊外，我們更重視您的購物經驗，我們所有的商品保證都是實機現貨面交，邀請您來親身體驗過後，滿意再帶走''',
        '''我們更貼心的提供您一站式購足的服務，現場自由搭配手機周邊配件例如:皮套,電池,保護貼,線材，讓您一次購足免煩惱!''',
        '''台灣地區的銷售多屬於B2C性質，我們的經銷商含蓋了北部與南部各大城市，遍及夜市、雜貨店、地下街、通訊行''',
        '''我們也積極拓展國外B2B業務，國外首座銷售據點設於菲律賓馬尼拉馬卡蒂經濟特區，印尼泗水也將成立第二個銷售中心''',
        '''CPsquare竭誠歡各方洽詢合作, <a href="/zh/contact/">聯絡我們 <span class="fa fa-paper-plane-o"> </a> ''',
    ]
}
