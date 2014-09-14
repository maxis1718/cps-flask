<!doctype html>
<html>

<head>
    <meta http-equiv="Content-type" content="text/html; charset=utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <meta name="keywords" content="{% block meta_keywords %}{% endblock %}">
    <meta name="description" content="{% block meta_description %}{% endblock %}">
    <title>{% block meta_title %}{% endblock %}{% if settings.SITE_TITLE %} | {{ settings.SITE_TITLE }}{% endif %}</title>

    <link rel="shortcut icon" href="{{ url_for('static', filename='img/favicon.ico') }}">

    <link rel="stylesheet" href="{{ url_for('static', filename='css/bootstrap.css') }}">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/font-awesome.css') }}">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/shared.css') }}">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/bootstrap-theme.css') }}">

    {% block extra_css %}
    {% endblock %}

    <script src="{{ url_for('static', filename='js/jquery.min.js') }}"></script>
    <script src="{{ url_for('static', filename='js/bootstrap.js') }}"></script>
    <script src="{{ url_for('static', filename='js/bootstrap-extras.js') }}"></script>
    <script src="{{ url_for('static', filename='js/util.js') }}"></script>


    {% block extra_js %}
    {% endblock %}

    <!--[if lt IE 9]>
    <script src="{{ url_for('static', filename='js/html5shiv.js') }}"></script>
    <script src="{{ url_for('static', filename='js/respond.min.js') }}"></script>
    <![endif]-->

    {% block extra_head %}
    {% endblock %}

</head>

<body>
<div id="navbar-top" class="navbar navbar-fixed-top" role="navigation">
    <div class="container">
        <div class="navbar-header">
            {% if settings.SITE_TITLE %}<a class="navbar-brand site-title" href="/">{{ settings.SITE_TITLE }}</a>{% endif %}
            {% if settings.SITE_TAGLINE %}<p class="navbar-text visible-lg site-tagline">{{ settings.SITE_TAGLINE }}</p>{% endif %}
        </div>

        <div class="navbar-collapse collapse">
            <ul class="nav navbar-nav">
                <li class="" id="news">
                    <a class="{{ 'hide' if lang != 'zh' else '' }}" href="/zh/news/" lang="zh">新聞列表</a>
                    <a class="{{ 'hide' if lang != 'en' else '' }}" href="/en/news/" lang="en">News</a>
                </li>
                <li class="" id="product">
                    <a class="{{ 'hide' if lang != 'zh' else '' }}" href="/zh/products/" lang="zh">產品</a>
                    <a class="{{ 'hide' if lang != 'en' else '' }}"href="/en/products/" lang="en">Products</a>
                </li>
                <li class="" id="about">
                    <a class="{{ 'hide' if lang != 'zh' else '' }}" href="/zh/about/" lang="zh">公司簡介</a>
                    <a class="{{ 'hide' if lang != 'en' else '' }}"href="/en/about/" lang="en">About</a>
                </li>
                <li class="" id="download">
                    <a class="{{ 'hide' if lang != 'zh' else '' }}" href="/zh/download/" lang="zh">軟體下載</a>
                    <a class="{{ 'hide' if lang != 'en' else '' }}" href="/en/download/" lang="en">Download</a>
                </li>
                <li class="" id="contact">
                    <a class="{{ 'hide' if lang != 'zh' else '' }}" href="/zh/contact/" lang="zh">聯絡我們</a>
                    <a class="{{ 'hide' if lang != 'en' else '' }}" href="/en/contact/" lang="en">Contact</a>
                </li>
                <li class="" id="https:--www.facebook.com-CPsquare3C">
                    <a class="{{ 'hide' if lang != 'zh' else '' }}" href="https://www.facebook.com/CPsquare3C" target="_blank" lang="zh">FB粉絲團</a>
                    <a class="{{ 'hide' if lang != 'en' else '' }}" href="https://www.facebook.com/CPsquare3C" target="_blank" lang="en">Facebook</a>
                </li>
            </ul>
            <!-- Language selector -->
            <ul class="nav navbar-nav navbar-right">
                <li class="dropdown">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown">Language<span class="caret"></span></a>
                    <ul class="dropdown-menu" role="menu">
                        <li><a href="/zh/{{ request.path.split(lang+'/')[1] }}">繁體中文</a></li>
                        <li><a href="/en/{{ request.path.split(lang+'/')[1] }}">English</a></li>
                    </ul>
                </li>
            </ul>

        </div>

    </div>
</div>


<!-- main block -->
<div class="container main-block-wrap">
    {% block main %}
    {% endblock %}
</div>

</body>
</html>
