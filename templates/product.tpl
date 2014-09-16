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
  
    </div>
    <div class="col-md-9 middle">

        
        <div class="row">
            <div class="col-md-12 middle product-wrap" id="product-{{ product['id'] }}">
                <div class="row">
                    <div class="col-md-12">
                        <div class="product-image-wrap">
                            <img src={{ url_for('static', filename=product['image_url']) }} width="100%" />
                        </div>                
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-6">
                        <div class="product-description-wrap">

                            <div class="product-title-wrap">
                                <h3 lang="{{lang}}">{{ product.translations[lang].title }}</h3>
                                
                            </div>

                            <div class="product-type-wrap">
                                <p lang="{{lang}}">{{ product.productType.translations[lang].name }} 廠牌：{{ product.brand.translations[lang].name }}</p>
                                
                            </div>

                            <div class="product-html-content-wrap">
                                <div lang="{{lang}}">{{ product.translations[lang].description }}</div>
                                
                            </div>

                            <hr>
                            {% if related_product %}
                                <h3>相關產品</h3>
                                <div class="product-title-wrap">
                                    <h3 lang="{{lang}}">{{ related_product.translations[lang].title }}</h3>
                                </div>

                            {% endif %}

                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        
    </div>
    <div class="col-md-1 right"></div>
</div>

{% endblock %}