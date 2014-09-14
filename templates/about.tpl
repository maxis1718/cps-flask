{% extends "base.tpl" %}

{% block meta_title %}About{% endblock %}
{% block title %}About{% endblock %}

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

		<div class="about-section">
			<p lang="zh" class="text {{ 'hide' if lang != 'zh' else '' }}">CP square，CP即價格性能比，square為平方的意思，讓大家都有取得CP極高的3C產品</p>
			<p lang="en" class="text {{ 'hide' if lang != 'en' else '' }}">"CP" means cost-performance ratio which used to measure the cost of an item against its effectiveness. “Square” in math means the result of multiplying a number by itself. The name of the brand “CP Square” reveals our purpose - we want everyone get high performance gadgets at reasonable price.</p>
		</div>

		<div class="about-section">
			<p lang="zh" class="text {{ 'hide' if lang != 'zh' else '' }}">除了提供最即時透明的國牌，白牌手機報價資訊外，我們更重視您的購物經驗，我們所有的商品保證都是實機現貨面交，邀請您來親身體驗過後，滿意再帶走</p>
			<p lang="en" class="text {{ 'hide' if lang != 'en' else '' }}">CP Square provides up to date information from MIC mobile brands to all kinds of White Box mobile. We also value your shopping experience, that’s why all the goods we sold are 100% in stock and we encourage you to come visit our store and experience by yourself.</p>
		</div>

		<div class="about-section">
			<p lang="zh" class="text {{ 'hide' if lang != 'zh' else '' }}">我們更貼心的提供您一站式購足的服務，現場自由搭配手機周邊配件例如:皮套,電池,保護貼,線材，讓您一次購足免煩惱⋯⋯</p>
			<p lang="en" class="text {{ 'hide' if lang != 'en' else '' }}">In order to serve our honorable customers, we create a one-stop all you can get service. Not only the mobile phones you can find at our store, but also the accessories such as, battery, phone cases, adapters…etc. You got all you need in once with CP Square.</p>
		</div>

		<div class="about-section">
			<p lang="zh" class="text {{ 'hide' if lang != 'zh' else '' }}">台灣地區的銷售多屬於B2C性質，我們的經銷商含蓋了北部與南部各大城市，遍及夜市、雜貨店、地下街、通訊行</p>
			<p lang="en" class="text {{ 'hide' if lang != 'en' else '' }}">Our B2C Business is widely spread in Taiwan. There are many distributors carried our product in major city such as Taipei, Tao Yuan and Kaohsiung. Sales channel includes, mobile phone store, night market, grocery store and underground shopping mall. We accept customized order as well.</p>
		</div>

		<div class="about-section">
			<p lang="zh" class="text {{ 'hide' if lang != 'zh' else '' }}">我們也積極拓展國外B2B業務，國外首座銷售據點設於菲律賓馬尼拉馬卡蒂經濟特區，印尼泗水也將成立第二個銷售中心</p>
			<p lang="en" class="text {{ 'hide' if lang != 'en' else '' }}">Recently, we develop international B2B business in emerging markets. The first sales center locates in Makati City, Philippines.  Another sales center will open in Surabaya, Indonesia soon.</p>
		</div>

		<div class="about-section">
			<p lang="zh" class="text {{ 'hide' if lang != 'zh' else '' }}">CPsquare竭誠歡各方洽詢合作, <a href="{{ url_for('show_contact', lang=lang) }}">聯絡我們 <span class="fa fa-paper-plane-o"></span></a></p>

			<p lang="en" class="text {{ 'hide' if lang != 'en' else '' }}">If you have any inquires or interest in our products, please <a href="{{ url_for('show_contact', lang=lang) }}">contact us.</a> We are looking forward to hear from you.</p>
		</div>
	</article>

	</div>
	<div class="col-md-1 right"></div>
</div>

{% endblock %}
