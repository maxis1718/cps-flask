{% extends "base.tpl" %}

{% block meta_title %}{{ news.translations[lang].title }}{% endblock %}
{% block title %}{{ news.translations[lang].title }}{% endblock %}

<!-- extrac css -->
{% block extra_css %}
<link rel="stylesheet" href="{{ url_for('static', filename='css/pages/article.css') }}">
{% endblock %}

<!-- extrac js -->
{% block extra_js %}
{% endblock %}

{% block main %}

<div class="row">
    <div class="col-md-1 left"></div>
    <div class="col-md-10 middle news-wrap" id="news-{{ news['id'] }}">
        <div class="news-image-wrap">
            
            <img src={{ url_for('static', filename=news['image_url']) }} width="100%" />
        </div>
        <div class="news-content-wrap">
            <div class="news-title-wrap">

                <h3 lang="{{ lang }}">{{ news.translations[lang].title }}</h3>
            </div>
            <div class="news-description-wrap">
                <p lang="{{ lang }}">{{ news.translations[lang].description }}</p>
				<p lang="{{ lang }}">{{ news.translations[lang].content }}</p>
                
            </div>
        </div>
        </div>
    <div class="col-md-1 right"></div>
</div>

{% endblock %}
