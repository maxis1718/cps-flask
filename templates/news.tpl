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

{% for news in news_list %}
<div class="row">
    <div class="col-md-1 left"></div>
    <div class="col-md-10 middle news-wrap" id="news-{{ news['id'] }}">
        <div class="news-image-wrap">
            
            <img src={{ url_for('static', filename=news['image_url']) }} />
        </div>
        <div class="news-content-wrap">
            <div class="news-title-wrap">
                <h3 lang="zh">{{ news['title_zh'] }}</h3>
                <h3 class="hide" lang="en">{{ news['title_en'] }}</h3>
            </div>
            <div class="news-description-wrap">
                <p lang="zh">{{ news['description_zh'] }}</p>
                <p class="hide" lang="en">{{ news['description_en'] }}</p>
                <p class="news-detail-wrap">
                    <a lang="zh">(詳全文)</a>
                    <a class="hide" lang="en">(see more)</a>                    
                </p>
            </div>
        </div>
        </div>
    <div class="col-md-1 right"></div>
</div>
{% endfor %}

{% endblock %}
