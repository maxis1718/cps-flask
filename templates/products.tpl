{% extends "base.tpl" %}

{% block meta_title %}{{ settings.MENU['products'][lang].decode("utf-8") }}{% endblock %}
{% block title %}{{ settings.MENU['products'][lang].decode("utf-8") }}{% endblock %}

<!-- extrac css -->
{% block extra_css %}
<link rel="stylesheet" href="{{ url_for('static', filename='css/pages/products.css') }}">
{% endblock %}

<!-- extrac js -->
{% block extra_js %}
{% endblock %}

{% block main %}

<div class="row products-container">
    <div class="col-md-2 col-xs-2 left vertical-col">
        <ul class="brand-wrap">
            {% for brand in brands %}
            <li brandid={{ brand.id }} class={{ "brand-seleted" if bid == brand.id else ""}}>
                <a href="{{ url_for('show_product_by_brand', brand_id=brand.id, lang=lang) }}">{{ brand.name }} <span class="brand-count"> ( {{ counts[brand.id] }} )</span></a>
            </li>
            {% endfor %}
        </ul>    
    </div>
    <div class="col-md-9 col-xs-9 middle vertical-col">

        {% for product in product_list %}
        <div class="row">
            <div class="col-md-12 middle product-wrap" id="product-{{ product['id'] }}">
                <div class="row">
                    <div class="col-md-7">
                        <div class="product-image-wrap">
                            <a href="/{{lang}}/products/{{product.id}}"><img src={{ url_for('static', filename=product['image_url']) }} width="100%" /></a>
                        </div>                
                    </div>
                    <div class="col-md-5">
                        <div class="product-description-wrap">

                            <div class="product-title-wrap">
                                <h3 lang="{{ lang }}"><a href="/{{lang}}/products/{{product.id}}">{{ product.translations[lang].title }}</a></h3>
                                
                            </div>

                            <div class="product-type-wrap">
                                <p lang="{{ lang }}">
                                    <span>{{ product.productType.translations[lang].name }}</span>
                                    <span>|</span>
                                    <span>{{ "廠牌：" if lang == "zh" else "Brand: "}}<label>{{ product.brand.translations[lang].name }}</label></span>
                                </p>
                            </div>

                            <div class="product-html-content-wrap">
                                <div lang="{{ lang }}">{{ product.translations[lang].description }}</div>
                                
                            </div>

                        </div>
                    </div>
                </div>
            </div>
        </div>

        {% endfor %}
        
    </div>
    <div class="col-md-1 right vertical-col"></div>
</div>

{% endblock %}