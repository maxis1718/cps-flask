{% extends "pages/page.tpl" %}

{% load mezzanine_tags staticfiles %}

{% block extra_css %}
<link rel="stylesheet" href="{% static "mezzanine/css/magnific-popup.css" %}">
{% endblock extra_css %}

{% block main %}
{{ block.super }}

{% editable page.gallery.content %}
{{ page.gallery.content|richtext_filters|safe }}
{% endeditable %}

<div class="gallery row">
{% with page.gallery.images.all as images %}
{% for image in images %}
<div class="col-xs-4 col-sm-3">
    <a class="thumbnail" rel="#image-{{ image.id }}" title="{{ image.description }}" href="{{ image.file.url }}">
        <div class="img-title">
            <span>{{ image.description }}</span>
        </div>
        <div class="img-container">
            <img class="img-responsive" src="{{ image.file.url }}">
        </div>
    </a>
</div>
{% endfor %}
{% endwith %}
</div>
{% endblock %}

{% block extra_js %}
{{ block.super }}
<script src="{% static "mezzanine/js/magnific-popup.js" %}"></script>
<script>
$(document).ready(function() {
    $('.gallery').magnificPopup({
        delegate: 'a',
        type: 'image',
        gallery: {
            enabled: true,
        }
    });
});
</script>
{% endblock %}
