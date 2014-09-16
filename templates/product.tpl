{% extends "base.tpl" %}

{% block meta_title %}News{% endblock %}
{% block title %}News{% endblock %}

<!-- extrac css -->
{% block extra_css %}
<link rel="stylesheet" href="{{ url_for('static', filename='css/pages/news.css') }}">
{% endblock %}

<!-- extrac js -->
{% block extra_js %}
{% endblock %}

{% block main %}

<div class="row">
    <div class="col-md-2 left">
        <div class="dropdown">
            <button class="btn btn-default dropdown-toggle" type="button" id="dropdownMenu1" data-toggle="dropdown">
            <span class="" lang="zh">品牌</span>
            <span class="hide" lang="en">Brand</span>
            <span class="caret"></span>
            </button>
            <ul class="dropdown-menu" role="menu" aria-labelledby="dropdownMenu1">
                {% for brand in brand_count %}
                <li role="presentation">
                    <a role="menuitem" tabindex="-1" href="{{ url_for('show_product_by_brand', brandname=brand, lang=lang) }}">{{ brand.name }} ( {{ brand.id }} )</a>
                </li>
                {% endfor %}
            </ul>
        </div>        
    </div>
    <div class="col-md-9 middle">

        
        <div class="row">
            <div class="col-md-12 middle product-wrap" id="product-{{ product['id'] }}">
                <div class="row">
                    <div class="col-md-6">
                        <div class="product-image-wrap">
                            <a href="/{{lang}}/products/{{product.id}}"><img src={{ url_for('static', filename=product['image_url']) }} width="100%" /></a>
                        </div>                
                    </div>
                    <div class="col-md-6">
                        <div class="product-description-wrap">

                            <div class="product-title-wrap">
                                <h3 lang="zh">{{ product.translations[lang].title }}</h3>
                                
                            </div>

                            <div class="product-type-wrap">
                                <p lang="zh">{{ product.productType.translations[lang].name }} 廠牌：{{ product.brand.translations[lang].name }}</p>
                                
                            </div>

                            <div class="product-html-content-wrap">
                                <div lang="zh">{{ product.translations[lang].description }}</div>
                                
                            </div>

                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        
    </div>
    <div class="col-md-1 right"></div>
</div>

{% endblock %}