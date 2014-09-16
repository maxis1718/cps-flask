{% extends "base.tpl" %}

{% block meta_title %}{% endblock %}
{% block title %}{% endblock %}

<!-- extrac css -->
{% block extra_css %}
<link rel="stylesheet" href="{{ url_for('static', filename='css/index.css') }}">
{% endblock %}

<!-- extrac js -->
{% block extra_js %}
{% endblock %}

{% block main %}

<div class="row">
	<div class="col-md-1 left"></div>
	<div class="col-md-10 middle large-banner-wrap">
		<div class="large-banner">
			<img src="{{ url_for('static', filename='img/advertise_here.jpg') }}"/>
		</div>
		<div class="nav-control-wrap"></div>
	</div>
	<div class="col-md-1 right"></div>
</div>


<div class="row footer-wraps">
	<div class="col-md-1 col-xs-1"></div>
	<div class="col-md-7 col-xs-7 news-wrap">
		<h2 lang="{{ lang }}">{{ settings.INDEX_NEWS[lang].decode('utf-8') }}</h2>
		<ul>
			{% for news in news_list %}
			<li><a href="/{{lang}}/news/{{ news.id }}">{{ news.translations[lang].title }}</a></li>
			{% endfor %}
		</ul>
	</div>
	<div class="col-md-3 col-xs-3 other-info-wrap">
		<div></div>
	</div>
	<div class="col-md-1 col-xs-1"></div>
</div>

{% endblock %}
