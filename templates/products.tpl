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

{% for product in product_list %}
<div class="row">
    <div class="col-md-1 left"></div>
    <div class="col-md-10 middle product-wrap" id="product-{{ product['id'] }}">
        <div class="row">
            <div class="col-md-5">
                <div class="product-image-wrap">
                    <img src={{ url_for('static', filename=product['image_url']) }} width="100%" />
                </div>                
            </div>
            <div class="col-md-7">
                <div class="product-description-wrap">

                    <div class="product-title-wrap">
                        <h3 lang="zh">{{ product['title_zh'] }} </h3>
                        <h3 class="hide" lang="en">{{ product['title_en'] }}</h3>
                    </div>

                    <div class="product-type-wrap">
                        <p lang="zh">{{ product['type_zh'] }}</p>
                        <p class="hide" lang="en">{{ product['type_en'] }}</p>
                    </div>

                    <div class="product-html-content-wrap">
                        <div lang="zh">{{ product['html_zh'] }}</div>
                        <div class="hide" lang="en">{{ product['html_en'] }}</div>
                    </div>

                    <div class="product-content-wrap hide">
                        <div lang="zh">
                            {% for li in product['content_zh'] %}
                            <li>{{ li }}</li>
                            {% endfor %}
                        </div>
                        <div class="hide" lang="en">
                            {% for li in product['content_en'] %}
                            <li>{{ li }}</li>
                            {% endfor %}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="col-md-1 right"></div>
</div>
{% endfor %}

{% endblock %}