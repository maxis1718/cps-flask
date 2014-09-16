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
			<img src="/static/img/advertise_here.jpg" />
		</div>
		<div class="nav-control-wrap"></div>
	</div>
	<div class="col-md-1 right"></div>
</div>


<div class="row">
	<div class="col-md-1"></div>
	<div class="col-md-7 news-wrap">
		<h2 lang="zh-tw">新聞</h2>
		<h2 class="hide" lang="en">News</h2>
		<div>
		</div>
	</div>
	<div class="col-md-3 other-info-wrap">
		<div></div>
	</div>
	<div class="col-md-1"></div>
</div>

{% endblock %}
