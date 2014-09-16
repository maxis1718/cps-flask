{% extends "base.tpl" %}

{% block meta_title %}{{ settings.MENU['news'][lang].decode("utf-8") }}{% endblock %}
{% block title %}{{ settings.MENU['news'][lang].decode("utf-8") }}{% endblock %}

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

                <h3 lang="zh">{{ news.translations[lang].title }}</h3>
            </div>
            <div class="news-description-wrap">
                <p lang="zh">{{ news.translations[lang].description }}</p>

                <p class="news-detail-wrap">
                    <a lang="zh" class="{{ 'hide' if lang != 'zh' else '' }}">(詳全文)</a>
                    <a lang="en" class="{{ 'hide' if lang != 'en' else '' }}">(see more)</a>
                                     
                </p>
            </div>
        </div>
        </div>
    <div class="col-md-1 right"></div>
</div>
{% endfor %}

{% endblock %}
