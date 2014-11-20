{% extends "base.tpl" %}

{% block meta_title %}{% endblock %}
{% block title %}{% endblock %}

<!-- extrac css -->
{% block extra_css %}
<link rel="stylesheet" href="{{ url_for('static', filename='css/index.css') }}">
{% endblock %}

<!-- extrac js -->
{% block extra_js %}
<script src="{{ url_for('static', filename='js/loopnews.js') }}"></script>
{% endblock %}

{% block main %}

<div class="row">
	<div class="col-md-1 left"></div>
	<div class="col-md-10 middle large-banner-wrap">
		<div class="large-banner">
			<img src="{{ url_for('static', filename='images/home.jpg') }}"/>
		</div>
		<div class="nav-control-wrap"></div>
	</div>
	<div class="col-md-1 right"></div>
</div>


<div class="row footer-wraps">
	<div class="col-md-1 col-xs-1"></div>
	<div class="col-md-10 col-xs-7 news-wrap">
		<h2 lang="{{ lang }}">{{ settings.INDEX_NEWS[lang].decode('utf-8') }}</h2>
		{% for i, news in news_list %}
        <div class="row news-block news-block-{{i}}" style="display: none;">
            <div class="col-md-5 col-xs-5 index-news-img-wrap">
                <img class="index-news-img" src="{{ url_for('static', filename=news.image_url) }}" width="95%">
            </div>
            <div class="col-md-7 col-xs-7 index-news-text-wrap">
                <div class="index-news-title">
                    <a href="/{{lang}}/news/{{ news.id }}">{{ news.translations[lang].title }}</a>
                </div>
                <div class="index-news-description">
                    <div>{{ news.translations[lang].description }} </div>
                </div>
            </div>
        </div>
		{% endfor %}
        <div>
<!--         {% for i, news in news_list %}
            <span class="index-news-select-item" val="{{ i }}">{{ i }}</span>
        {% endfor %}   -->          
        </div>
	</div>
<!-- 	<div class="col-md-3 col-xs-3 other-info-wrap">
		<div></div>
	</div> -->
	<div class="col-md-1 col-xs-1"></div>
</div>

{% endblock %}
