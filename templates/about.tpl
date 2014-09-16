{% extends "base.tpl" %}

{% block meta_title %}{{ settings.MENU['about'][lang].decode("utf-8") }}{% endblock %}
{% block title %}{{ settings.MENU['about'][lang].decode("utf-8") }}{% endblock %}

<!-- extrac css -->
{% block extra_css %}
<link rel="stylesheet" href="{{ url_for('static', filename='css/pages/about.css') }}">
{% endblock %}

<!-- extrac js -->
{% block extra_js %}
{% endblock %}

{% block main %}

<div class="row">
	<div class="col-md-1 left"></div>
	<div class="col-md-10 middle">

	<article class="about-sections-wrap">
		{% for section in settings.ABOUT[lang] %}
		<div class="about-section">
			<p lang="zh" class="text">{{ section.decode('utf-8') }}</p>
		{% endfor %}
	</article>

	</div>
	<div class="col-md-1 right"></div>
</div>

{% endblock %}
