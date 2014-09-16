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
				<div class="img-wrap">
					<img src="{{ url_for('static', filename='img/contact-us.jpg') }}" width="100%" />
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
