{% extends "base.tpl" %}

{% block meta_title %}新聞{% endblock %}
{% block title %}新聞{% endblock %}

<!-- extrac css -->
{% block extra_css %}
<link rel="stylesheet" href="{{ url_for('static', filename='css/pages/article.css') }}">
{% endblock %}

<!-- extrac js -->
{% block extra_js %}
{% endblock %}

{% block main %}

{% for news in news_list %}
<div class="row">
	<p> news </p>

</div>
{% endfor %}

{% endblock %}
