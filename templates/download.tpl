{% extends "base.tpl" %}

{% block meta_title %}{{ settings.MENU['download'][lang].decode("utf-8") }}{% endblock %}
{% block title %}{{ settings.MENU['download'][lang].decode("utf-8") }}{% endblock %}

<!-- extrac css -->
{% block extra_css %}
<link rel="stylesheet" href="{{ url_for('static', filename='css/pages/download.css') }}">
{% endblock %}

<!-- extrac js -->
{% block extra_js %}
<script src="{{ url_for('static', filename='css/pages/download.js') }}"></script>
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

{% endblock %}
