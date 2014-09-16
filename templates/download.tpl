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
        <h2>{{ settings.MENU['download'][lang].decode('utf-8') }}</h2>
		<ul class="download-item-wrap">
            {% for item in softwares %}
            <li class="download-item">
                <a href={{ url_for('static', filename="softwares/"+item['filename'].decode('utf-8') ) }}>{{ item['title_'+lang].decode('utf-8') }}</a>
            </li>
            {% endfor %}
        </ul>
	</div>
</div>

{% endblock %}
