{% extends "base.tpl" %}

{% block meta_title %}Contact{% endblock %}
{% block title %}Contact{% endblock %}

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
		<div class="row contact-wrap">
			<div class="col-md-7">
				<div class="img-wrap">

					<img src="{{ url_for('static', filename='img/contact-us.jpg') }}" width="100%" />
				</div>
				
			</div>
			<div class="col-md-5">
				<div class="contact-info-wrap">
					
					<i class="fa fa-envelope text {{ 'hide' if lang != 'zh' else '' }}" lang="zh"> 電子郵件</i>
					<i class="fa fa-envelope text {{ 'hide' if lang != 'en' else '' }}" lang="en"> Email</i>
					<div class="email"><a href="mailto:cpsquaretw@gmail.com">cpsquaretw@gmail.com</a></div>
					
					<i class="fa fa-mobile text {{ 'hide' if lang != 'zh' else '' }}" lang="zh"> 手機</i>
					<i class="fa fa-mobile text {{ 'hide' if lang != 'en' else '' }}" lang="en"> Cellphone</i>
					<div class="phone"><a href="skype:+886982621414?call">+886 982 621 414</a></div>
					
				</div>				
			</div>
		</div>

	</div>
	<div class="col-md-1 right"></div>
</div>

{% endblock %}
