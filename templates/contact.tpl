{% extends "base.tpl" %}


{% block meta_title %}{{ settings.MENU['contact'][lang].decode("utf-8") }}{% endblock %}
{% block title %}{{ settings.MENU['contact'][lang].decode("utf-8") }}{% endblock %}

<!-- extrac css -->
{% block extra_css %}
<link rel="stylesheet" href="{{ url_for('static', filename='css/pages/contact.css') }}">
{% endblock %}

<!-- extrac js -->
{% block extra_js %}
{% endblock %}

{% block main %}

<div class="row">
	<div class="col-md-1 left"></div>
	<div class="col-md-10 middle">
		<h2>{{ settings.MENU['contact'][lang].decode('utf-8') }}</h2>
		<div class="row contact-wrap">
			<div class="col-md-7">
				<div class="map-wrap">
				<!-- <div class="img-wrap"> -->
					<iframe src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d3614.3472203594233!2d121.54321879999998!3d25.056218!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abe6c92ba3f1%3A0xbca3e0c901b18aa6!2zMTA05Y-w5YyX5biC5Lit5bGx5Y2A6IiI5a6J6KGXOTHomZ8!5e0!3m2!1szh-TW!2stw!4v1416324233336" width="100%" height="480" frameborder="0" style="border:0"></iframe>
					<!-- <img src="{{ url_for('static', filename='img/contact-us.jpg') }}" width="100%" /> -->
				</div>
			</div>
			<div class="col-md-5">
				<div class="contact-info-wrap">
					{% for item in settings.CONTACT %}
					<i class="{{ item['before'] }} text" lang="{{ lang }}"> {{ item['title'][lang].decode("utf-8") }}</i>
					{% if item['url'] %}
					<div class="{{ item['type'] }}"><a href={{ item['url'] }}>{{ item['content'] }}</a></div>
					{% else %}
					<div class="{{ item['type'] }}">{{ item['content'] }}</div>
					{% endif %}
					{% endfor %}
				</div>				
			</div>
		</div>
	</div>
	<div class="col-md-1 right"></div>
</div>
{% endblock %}
