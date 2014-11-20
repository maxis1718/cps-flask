<!doctype html>
<html>

<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <meta name="title" content="{% block meta_title %}{% endblock %}">
    <meta name="keywords" content="{% block meta_keywords %}{% endblock %}">
    <meta name="description" content="{% block meta_description %}{% endblock %}">
    <title>{% block title %}{% endblock %}
    {% if settings.SITE_TITLE %}
        {% if not is_index %} | {% endif %}
    {{ ' '.join(settings.SITE_TITLE[lang]) }}
    {% endif %}</title>

    <link rel="shortcut icon" href="{{ url_for('static', filename='img/favicon.ico') }}">

    <link rel="stylesheet" href="{{ url_for('static', filename='css/bootstrap-theme.css') }}">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/bootstrap.css') }}">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/font-awesome.css') }}">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/shared.css') }}">

    {% block extra_css %}
    {% endblock %}

    <script src="{{ url_for('static', filename='js/jquery.min.js') }}"></script>
    <script src="{{ url_for('static', filename='js/bootstrap.js') }}"></script>
    <script src="{{ url_for('static', filename='js/bootstrap-extras.js') }}"></script>
    <script src="{{ url_for('static', filename='js/util.js') }}"></script>


    {% block extra_js %}
    {% endblock %}

    <script src="{{ url_for('static', filename='js/main.js') }}"></script>

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
        <div class="navbar-collapse collapse">

            <ul class="nav navbar-nav">
                {% if settings.SITE_TITLE %}
                <li class="navbar-brand">
                    <!-- <a class="site-title">中培貿易<br>CPSquare</a> -->
                    <a class="site-title" href={{ url_for("show_index", lang=lang) }}>
                        {% for title_line in settings.SITE_TITLE[lang] %}
                            <div>{{ title_line }}</div>
                        {% endfor %}
                    </a>
                </li>
                {% endif %}
                {% if settings.SITE_TAGLINE %}
                <li class="navbar-tagline">
                    <a class="site-tagline">{{ settings.SITE_TAGLINE[lang].decode('utf-8') }}</a>
                </li>
                {% endif %}
                {% for menu_name in settings.MENU_ORDER %}
                <li class="" id="news">
                    {% if "//" in settings.MENU[menu_name]['url'].decode('utf-8') %}
                    <a href={{ settings.MENU[menu_name]['url'].decode('utf-8') }} lang={{ lang }} target="_blank">{{ settings.MENU[menu_name][lang].decode('utf-8') }}</a>                    
                    {% else %}
                    <a href={{ url_for('show_'+settings.MENU[menu_name]['url'], lang=lang) }} lang={{ lang }}>{{ settings.MENU[menu_name][lang].decode('utf-8') }}</a>                        
                    {% endif %}
                </li>
                {% endfor %}
            </ul>
            <!-- Language selector -->
            <ul class="nav navbar-nav navbar-right">
                <li class="dropdown">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown">Language<span class="caret"></span></a>
                    <ul class="dropdown-menu" role="menu">
                        {% for LangItem in settings.LANGUAGES %}
                        <li><a href="/{{ LangItem['url'] }}/{{ request.path.split(lang+'/')[1] }}">{{ LangItem['name'].decode('utf-8') }}</a></li>
                        {% endfor %}
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
    <footer>
        <div>2014 cpsquare</div>
    </footer>
</div>


</body>
</html>
