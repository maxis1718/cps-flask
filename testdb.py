# coding: utf-8
from datetime import datetime
from cps import db

## create the tables and database
print 'create tables and database'
db.create_all()

from cps import User
from cps import News
from cps import ProductType
from cps import Brand
from cps import Product

## create some users
print 'create `admin` and `guest`'
admin = User('admin', 'admin@cps.com')
guest = User('guest', 'guest@cps.com')

## commit
# db.session.add(admin)
# db.session.add(guest)
# db.session.commit()


print "creat news"
news1 = News("images/iPhone6.png", datetime.now() )
news1.translations['zh'].title = u"iPhone 6: 豈止於大"
news1.translations['en'].title = u"iPhone 6: Not only big"
news1.translations['zh'].description = u'Tim Cook 舉起了全新的 iPhone 6 ，我們可以看到新 iPhone 比起上一代明顯更薄！除了螢幕更大以外，兩款新機在性能、相機皆有所提升，但機身厚度卻都變得更加纖薄。大螢幕版本的 iPhone 6 Plus，售價將比 4.7 吋 iPhone 6 貴 $100 美金，也就是大約台幣 3 千元左右，大家在螢幕尺寸和價格差異的考量下，又會選擇哪一部呢？'
news1.translations['en'].description = u'<div>New iPhone</div>'
news1.translations['en'].content = u"""<ul class="speclist">
	<li class="model">Apple iPhone 6 16GB</li>
	<li class="first-line">
	  	<label>作業系統:</label>iOS                    

			<a class="fb-share" title="分享到facebook" name="fb_share" href="https://www.facebook.com/sharer.php?u=http%3A%2F%2Fwww.eprice.com.tw%2Fmobile%2Fintro%2F5098%2Fapple-iphone-6-16gb%2F&amp;t=&amp;src=sp" target="_blank"></a> 
            
			<iframe src="https://www.facebook.com/widgets/like.php?href=http%3A%2F%2Fwww.eprice.com.tw%2Fmobile%2Fintro%2F5098%2Fapple-iphone-6-16gb%2F&amp;layout=button_count&amp;show_faces=false&amp;width=94&amp;action=like&amp;font=arial&amp;colorscheme=light&amp;height=21" scrolling="no" frameborder="0" class="fb-like fb_iframe_widget" allowtransparency="true" fb-xfbml-state="rendered" fb-iframe-plugin-query="app_id=&amp;href=http%3A%2F%2Fwww.eprice.com.tw%2Fmobile%2Fintro%2Fc01-p5098-apple-iphone-6-16gb%2F&amp;locale=zh_TW&amp;sdk=joey"><span style="vertical-align: bottom; width: 450px; height: 25px;"><iframe name="f44c87a58" width="1000px" height="1000px" frameborder="0" allowtransparency="true" scrolling="no" title="fb:like Facebook Social Plugin" src="http://www.facebook.com/plugins/like.php?app_id=&amp;channel=http%3A%2F%2Fstatic.ak.facebook.com%2Fconnect%2Fxd_arbiter%2FZEbdHPQfV3x.js%3Fversion%3D41%23cb%3Df16144c5a%26domain%3Dwww.eprice.com.tw%26origin%3Dhttp%253A%252F%252Fwww.eprice.com.tw%252Ff2d8075ab4%26relation%3Dparent.parent&amp;href=http%3A%2F%2Fwww.eprice.com.tw%2Fmobile%2Fintro%2Fc01-p5098-apple-iphone-6-16gb%2F&amp;locale=zh_TW&amp;sdk=joey" class="" style="border: none; visibility: visible; width: 450px; height: 25px;"></iframe></span></iframe>
            
           	<a class="fb-count" href="javascript:void(0);"><fb:comments-count href="http://www.eprice.com.tw/mobile/intro/5098/" fb-xfbml-state="rendered" class=""><span class="fb_comments_count">3</span></fb:comments-count></a>
            
            <div class="clear"></div>
				</li>
	<li>
	  	<label>通　　訊:</label>GSM 四頻 WCDMA 850 + 900 + 2100<span class="system-lte">4G LTE 700 + 900 + 1800<ul class="lte-isp-list"><li class="cht"><a href="javascript:void(0);" rel="nofollow" title="適用中華電信 4G" class="on"></a></li><li class="fet"><a href="javascript:void(0);" rel="nofollow" title="適用遠傳電信 4G" class="on"></a></li><li class="twm"><a href="javascript:void(0);" rel="nofollow" title="適用台灣大哥大 4G" class="on"></a></li><li class="aptg"><a href="javascript:void(0);" rel="nofollow" title="國碁/亞太電信 4G 尚未開台，目前不適用" class="off"></a></li><li class="vibo"><a href="javascript:void(0);" rel="nofollow" title="適用台灣之星 4G" class="on"></a></li></ul><div class="clear"></div></span>	</li>
	<li>
		<label>尺寸重量:</label>138.1 x 67 x 6.9 mm / 129g	</li>
	<li>
		<label>螢　　幕:</label><span class="normal">1334 x 750 pixels</span>、<span class="normal">4.7 吋 </span>IPS TFT	</li>
	<li>
		<label>主要相機:</label><span class="normal">800 萬像素 </span><span class="normal">CMOS</span>    </li>
    <li>
		<label>前置相機:</label><span class="normal">120 萬像素 </span><span class="normal">CMOS</span>        
    </li>
  	<li>
		<label>記憶插卡:</label>無	</li>
	<li>
		<label>使用時間:</label>通話 840 分鐘 / 待機 250 小時	</li>
	<li>
		<label>電　　池:</label>未知 (固定式)    </li>
   	<li>
		<label>顏　　色:</label>金色、銀色、太空灰	</li>
    <li>
		<span class="twm-ad"><a rel="nofollow" href="http://www.eprice.com.tw/ad/redir.html?id=5525" target="_blank"><label>優　　惠:</label>這買最划算</a></span>					
    </li>
    </ul>"""
news1.translations['zh'].content = u"""<div class="content">
            <label style="color: rgb(255, 102, 51); font-weight: bold;">iPhone 6 正式發佈：螢幕更大、機身更薄、性能更強、對焦更快</label><br>
<label style="color: rgb(51, 51, 51);">Tim Cook 舉起了全新的 iPhone 6 ，我們可以看到新 iPhone 比起上一代明顯更薄！除了螢幕更大以外，兩款新機在性能、相機皆有所提升，但機身厚度卻都變得更加纖薄。大螢幕版本的 iPhone 6 Plus，售價將比 4.7 吋 iPhone 6 貴 $100 美金，也就是大約台幣 3 千元左右，大家在螢幕尺寸和價格差異的考量下，又會選擇哪一部呢？</label><br style="color: rgb(51, 51, 51);">
<br style="color: rgb(51, 51, 51);">
<img src="http://timg.eprice.com.tw/tw/mobile/img/2014-09/10/4912641/epic520_1_4544_8606fa364fad47a28c7ef0706a807ece.JPG" data-original="http://timg.eprice.com.tw/tw/mobile/img/2014-09/10/4912641/epic520_1_4544_8606fa364fad47a28c7ef0706a807ece.JPG" title="Apple iPhone 6 16GB 介紹圖片" alt="Apple iPhone 6 16GB 介紹圖片" border="0" style="max-width: 640px; color: rgb(51, 51, 51); font-size: 15.5555562973022px; display: inline;"><br style="color: rgb(51, 51, 51);">
<label style="color: rgb(51, 51, 51); font-size: 15.5555562973022px;">▲全新 iPhone 正式發表，</label><label style="color: rgb(51, 51, 51);">4.7 吋名為 iPhone 6，5.5 吋大螢幕版本就叫做 iPhone 6 Plus</label><br style="color: rgb(51, 51, 51);">
<br style="color: rgb(51, 51, 51);">
<img src="http://timg.eprice.com.tw/tw/mobile/img/2014-09/10/4912641/mansonfat_1_4544_080865e00511081693543ca3363c20af.png" data-original="http://timg.eprice.com.tw/tw/mobile/img/2014-09/10/4912641/mansonfat_1_4544_080865e00511081693543ca3363c20af.png" title="Apple iPhone 6 16GB 介紹圖片 - 1" alt="Apple iPhone 6 16GB 介紹圖片 - 1" border="0" style="max-width: 640px; color: rgb(51, 51, 51); border-width: 0px; border-style: solid; height: 480px; width: 640px; display: inline;"><br style="color: rgb(51, 51, 51);">
<br style="color: rgb(51, 51, 51);">
<img src="http://timg.eprice.com.tw/tw/mobile/img/2014-09/10/4912641/epic520_1_4544_e3e4e0986144ba194aa733765500c03f.JPG" data-original="http://timg.eprice.com.tw/tw/mobile/img/2014-09/10/4912641/epic520_1_4544_e3e4e0986144ba194aa733765500c03f.JPG" title="Apple iPhone 6 16GB 介紹圖片 - 2" alt="Apple iPhone 6 16GB 介紹圖片 - 2" border="0" style="max-width: 640px; color: rgb(51, 51, 51); display: inline;"><br style="color: rgb(51, 51, 51);">
<label style="color: rgb(51, 51, 51);">▲ 從 4 吋、4.7 吋、到最大的 5.5 吋，iPhone 的「大」夢終於完成，甚至解析度也更加提升了。各位鍾愛誰？</label><br style="color: rgb(51, 51, 51);">
<br style="color: rgb(51, 51, 51);">
<img src="http://timg.eprice.com.tw/tw/mobile/img/2014-09/10/4912641/mansonfat_1_4544_dd516f97c25a3a4a8bc44afbd99a0126.png" data-original="http://timg.eprice.com.tw/tw/mobile/img/2014-09/10/4912641/mansonfat_1_4544_dd516f97c25a3a4a8bc44afbd99a0126.png" title="Apple iPhone 6 16GB 介紹圖片 - 3" alt="Apple iPhone 6 16GB 介紹圖片 - 3" border="0" style="max-width: 640px; color: rgb(51, 51, 51); border-width: 0px; border-style: solid; height: 481px; width: 640px; display: inline;"><br style="color: rgb(51, 51, 51);">
<label style="color: rgb(51, 51, 51);">▲ 因應大螢幕，5.5 吋的 iPhone 6 Plus 將有橫向桌面顯示。</label><br style="color: rgb(51, 51, 51);">
<br style="color: rgb(51, 51, 51);">
<img src="http://timg.eprice.com.tw/tw/mobile/img/2014-09/10/4912641/epic520_1_4544_87aa5c6dff45927dfe0d9a40fc864ee7.JPG" data-original="http://timg.eprice.com.tw/tw/mobile/img/2014-09/10/4912641/epic520_1_4544_87aa5c6dff45927dfe0d9a40fc864ee7.JPG" title="Apple iPhone 6 16GB 介紹圖片 - 4" alt="Apple iPhone 6 16GB 介紹圖片 - 4" border="0" style="max-width: 640px; color: rgb(51, 51, 51); display: inline;"><br style="color: rgb(51, 51, 51);">
<br style="color: rgb(51, 51, 51);">
<label style="color: rgb(51, 51, 51); font-size: 15.5555562973022px;">▲在薄度的部份兩款機型都更加精進，iPhone 6 僅有 6.9mm，大螢幕的&nbsp;iPhone 6 Plus 也只有 7.1mm 。</label><br style="color: rgb(51, 51, 51);">
<br style="color: rgb(51, 51, 51);">
<img src="http://timg.eprice.com.tw/tw/mobile/img/2014-09/10/4912641/epic520_1_4544_b61fe61f2e3074f47390c5febbe11f3f.JPG" data-original="http://timg.eprice.com.tw/tw/mobile/img/2014-09/10/4912641/epic520_1_4544_b61fe61f2e3074f47390c5febbe11f3f.JPG" title="Apple iPhone 6 16GB 介紹圖片 - 5" alt="Apple iPhone 6 16GB 介紹圖片 - 5" border="0" style="max-width: 640px; color: rgb(51, 51, 51); display: inline;"><br style="color: rgb(51, 51, 51);">
<label style="color: rgb(51, 51, 51); font-size: 15.5555562973022px;">▲</label><label style="color: rgb(20, 24, 35); line-height: 20px;">iPhone 6 採用第二代的 64-bit A8 CPU，比前代快上 25% ！至於</label><label style="color: rgb(20, 24, 35); line-height: 20px;">全新的 M8 協同晶片甚至可以辨出跑步還是踩單車的差異，就連</label><label style="color: rgb(20, 24, 35); line-height: 20px;">計算距離和熱量都可以做到。</label><br style="color: rgb(51, 51, 51);">
<br style="color: rgb(51, 51, 51);">
<label style="color: rgb(51, 51, 51);">&nbsp;</label>
<h2 style="line-height: 27px;">
	對焦更快，畫質更好的相機提升！</h2>
<br style="color: rgb(51, 51, 51);">
<img src="http://timg.eprice.com.tw/tw/mobile/img/2014-09/10/4912641/epic520_1_4544_f922a6762d73c2dd37a40ae89d7eaa7a.JPG" data-original="http://timg.eprice.com.tw/tw/mobile/img/2014-09/10/4912641/epic520_1_4544_f922a6762d73c2dd37a40ae89d7eaa7a.JPG" title="Apple iPhone 6 16GB 介紹圖片 - 6" alt="Apple iPhone 6 16GB 介紹圖片 - 6" border="0" style="max-width: 640px; color: rgb(51, 51, 51); display: inline;"><br style="color: rgb(51, 51, 51);">
<br style="color: rgb(51, 51, 51);">
<img src="http://timg.eprice.com.tw/tw/mobile/img/2014-09/10/4912641/epic520_1_4544_33c97fad511c4e6f22c82666ec6daf7b.JPG" data-original="http://timg.eprice.com.tw/tw/mobile/img/2014-09/10/4912641/epic520_1_4544_33c97fad511c4e6f22c82666ec6daf7b.JPG" title="Apple iPhone 6 16GB 介紹圖片 - 7" alt="Apple iPhone 6 16GB 介紹圖片 - 7" border="0" style="max-width: 640px; color: rgb(51, 51, 51); display: inline;"><br style="color: rgb(51, 51, 51);">
<label style="color: rgb(51, 51, 51); font-size: 15.5555562973022px;">​▲</label><label style="color: rgb(20, 24, 35); font-size: 15.5555562973022px; line-height: 20px;">iPhone 6 與&nbsp;iPhone 6&nbsp;Plus&nbsp;搭載的相機依然為 800 萬畫素，但&nbsp;</label><label style="color: rgb(20, 24, 35); line-height: 20px;">iPhone 6&nbsp;</label><label style="color: rgb(20, 24, 35); font-size: 15.5555562973022px; line-height: 20px;">Plus</label><label style="color: rgb(20, 24, 35); line-height: 20px;">&nbsp;是 A</label><label style="color: rgb(20, 24, 35); font-size: 15.5555562973022px; line-height: 20px;">pple&nbsp;</label><label style="color: rgb(20, 24, 35); line-height: 20px;">首款加入光學防震的機種，而</label><label style="font-size: 15.5555562973022px; color: rgb(20, 24, 35); line-height: 20px;">&nbsp;</label><label style="color: rgb(20, 24, 35); line-height: 20px;">iPhone 6 相機則是維持數位防震。此外兩款手機的主</label><label style="color: rgb(20, 24, 35); line-height: 20px;">鏡頭皆為 F2.2 光圈，同時增進對焦速度與降造能力，並且</label><label style="color: rgb(20, 24, 35); line-height: 20px;">可拍攝 4300 萬畫素全景照片及最高 60 fps 的 Full HD 影片拍攝。</label><br style="color: rgb(20, 24, 35); line-height: 20px;">
<br style="color: rgb(51, 51, 51);">
<img src="http://timg.eprice.com.tw/tw/mobile/img/2014-09/10/4912641/epic520_1_4544_ff3b3169d68b56844a720d80a4135ca6.jpg" data-original="http://timg.eprice.com.tw/tw/mobile/img/2014-09/10/4912641/epic520_1_4544_ff3b3169d68b56844a720d80a4135ca6.jpg" title="Apple iPhone 6 16GB 介紹圖片 - 8" alt="Apple iPhone 6 16GB 介紹圖片 - 8" border="0" style="max-width: 640px; color: rgb(51, 51, 51); display: inline;"><br style="color: rgb(51, 51, 51);">
<br style="color: rgb(51, 51, 51);">
<img src="http://timg.eprice.com.tw/tw/mobile/img/2014-09/10/4912641/epic520_1_4544_31620a582c06c700a6bddd643150698f.jpg" data-original="http://timg.eprice.com.tw/tw/mobile/img/2014-09/10/4912641/epic520_1_4544_31620a582c06c700a6bddd643150698f.jpg" title="Apple iPhone 6 16GB 介紹圖片 - 9" alt="Apple iPhone 6 16GB 介紹圖片 - 9" border="0" style="max-width: 640px; color: rgb(51, 51, 51); display: inline;"><br style="color: rgb(51, 51, 51);">
<br style="color: rgb(51, 51, 51);">
<img src="http://timg.eprice.com.tw/tw/mobile/img/2014-09/10/4912641/epic520_1_4544_eb6fee06664de020524fdbb0b5566135.jpg" data-original="http://timg.eprice.com.tw/tw/mobile/img/2014-09/10/4912641/epic520_1_4544_eb6fee06664de020524fdbb0b5566135.jpg" title="Apple iPhone 6 16GB 介紹圖片 - 10" alt="Apple iPhone 6 16GB 介紹圖片 - 10" border="0" style="max-width: 640px; color: rgb(51, 51, 51); display: inline;"><br style="color: rgb(51, 51, 51);">
<label style="color: rgb(51, 51, 51); font-size: 15.5555562973022px;">​▲</label><label style="color: rgb(20, 24, 35); line-height: 20px;">iPhone 6 / 6 Plus 的前鏡頭維持12</label><label style="color: rgb(20, 24, 35); font-size: 15.5555562973022px; line-height: 20px;">20 萬畫素，但</label><label style="color: rgb(20, 24, 35); line-height: 20px;">功能也更進步了，除了加入新感光元件，也有F2.2大光圈，使拍攝亮度更高，可以連續自拍、HDR 功能。<a href="#" data-url="http://www.eprice.com.tw/mobile/talk/4544/4912658/1/" target="_blank">點我看更多相機詳細介紹。</a></label><br style="color: rgb(51, 51, 51);">
<br style="color: rgb(51, 51, 51);">
<label style="color: rgb(51, 51, 51);">&nbsp;</label>
<h2 style="line-height: 27px;">
	iPhone 6 / 6 Plus 預載全新 iOS 8 作業系統</h2>
<label style="color: rgb(51, 51, 51);">&nbsp;</label>
<h2 style="line-height: 27px;">
	&nbsp;</h2>
<h2 style="line-height: 27px;">
	<img src="http://timg.eprice.com.tw/tw/mobile/img/2014-09/10/4912641/epic520_1_4544_a0b437e7dc1f69f989f414b8fe6b5248.JPG" data-original="http://timg.eprice.com.tw/tw/mobile/img/2014-09/10/4912641/epic520_1_4544_a0b437e7dc1f69f989f414b8fe6b5248.JPG" title="Apple iPhone 6 16GB 介紹圖片 - 11" alt="Apple iPhone 6 16GB 介紹圖片 - 11" border="0" style="max-width: 640px; color: rgb(51, 51, 51); display: inline;"></h2>
<br style="color: rgb(51, 51, 51);">
<img src="http://timg.eprice.com.tw/tw/mobile/img/2014-09/10/4912641/epic520_1_4544_dcb1e2bc876f5c9dc03e725ac16d3845.jpg" data-original="http://timg.eprice.com.tw/tw/mobile/img/2014-09/10/4912641/epic520_1_4544_dcb1e2bc876f5c9dc03e725ac16d3845.jpg" title="Apple iPhone 6 16GB 介紹圖片 - 12" alt="Apple iPhone 6 16GB 介紹圖片 - 12" border="0" style="max-width: 640px; color: rgb(51, 51, 51); font-size: 15.5555562973022px; border-width: 0px; border-style: solid; height: 387px; width: 640px; display: inline;"><br style="color: rgb(51, 51, 51);">
<br style="color: rgb(51, 51, 51);">
<img src="http://timg.eprice.com.tw/tw/mobile/img/2014-09/10/4912641/epic520_1_4544_f2282529cf1df7e9a2d4111b1650c141.jpg" data-original="http://timg.eprice.com.tw/tw/mobile/img/2014-09/10/4912641/epic520_1_4544_f2282529cf1df7e9a2d4111b1650c141.jpg" title="Apple iPhone 6 16GB 介紹圖片 - 13" alt="Apple iPhone 6 16GB 介紹圖片 - 13" border="0" style="max-width: 640px; color: rgb(51, 51, 51); border-width: 0px; border-style: solid; height: 348px; width: 640px; display: inline;"><br style="color: rgb(51, 51, 51);">
<label style="color: rgb(51, 51, 51); font-size: 15.5555562973022px;">▲iPhone 6 與 iPhone 6 Plus 將預載全新的 iOS 8 作業系統。好消息是 9 月 17 日起 Apple 會開放&nbsp;iOS 8 升級，甚至連推出許久的 iPad 2 、iPhone 4s 都在升級名單裡面喔！</label><br style="color: rgb(51, 51, 51);">
<br style="color: rgb(51, 51, 51);">
<label style="color: rgb(51, 51, 51);">&nbsp;</label>
<h2 style="line-height: 27px;">
	&nbsp;全新&nbsp;Apple Pay 功能，提供更安全的付款機制&nbsp;</h2>
<img src="http://timg.eprice.com.tw/tw/mobile/img/2014-09/10/4912641/epic520_1_4544_0c979da18d745835c89f32ff9f12dbe1.JPG" data-original="http://timg.eprice.com.tw/tw/mobile/img/2014-09/10/4912641/epic520_1_4544_0c979da18d745835c89f32ff9f12dbe1.JPG" title="Apple iPhone 6 16GB 介紹圖片 - 14" alt="Apple iPhone 6 16GB 介紹圖片 - 14" border="0" style="max-width: 640px; color: rgb(51, 51, 51); display: inline;"><br style="color: rgb(51, 51, 51);">
<br style="color: rgb(51, 51, 51);">
<img src="http://timg.eprice.com.tw/tw/mobile/img/2014-09/10/4912641/epic520_1_4544_2791c99a328501cf02d3ffa71799d714.jpg" data-original="http://timg.eprice.com.tw/tw/mobile/img/2014-09/10/4912641/epic520_1_4544_2791c99a328501cf02d3ffa71799d714.jpg" title="Apple iPhone 6 16GB 介紹圖片 - 15" alt="Apple iPhone 6 16GB 介紹圖片 - 15" border="0" style="max-width: 640px; color: rgb(51, 51, 51); display: inline;"><br style="color: rgb(51, 51, 51);">
<br style="color: rgb(51, 51, 51);">
<img src="http://timg.eprice.com.tw/tw/mobile/img/2014-09/10/4912641/epic520_1_4544_8155b2a8ef0a73d6637ee73e3a517af7.jpg" data-original="http://timg.eprice.com.tw/tw/mobile/img/2014-09/10/4912641/epic520_1_4544_8155b2a8ef0a73d6637ee73e3a517af7.jpg" title="Apple iPhone 6 16GB 介紹圖片 - 16" alt="Apple iPhone 6 16GB 介紹圖片 - 16" border="0" style="max-width: 640px; color: rgb(51, 51, 51); border-width: 0px; border-style: solid; height: 361px; width: 640px; display: inline;"><br style="color: rgb(51, 51, 51);">
<label style="color: rgb(51, 51, 51); font-size: 15.5555562973022px;">▲</label><label style="color: rgb(20, 24, 35); line-height: 20px;">iPhone 6 加入 NFC 感應晶片，同時具有</label><label style="color: rgb(20, 24, 35); line-height: 20px;">標榜</label><label style="font-size: 15.5555562973022px; color: rgb(20, 24, 35); line-height: 20px;">安全性高</label><label style="color: rgb(20, 24, 35); line-height: 20px;">的 Apple Pay 付款功能，</label><label style="color: rgb(20, 24, 35); line-height: 20px;">Apple 表示該功能不會將你的信用卡紀錄洩漏，</label><label style="color: rgb(20, 24, 35); line-height: 20px;">甚至連你用 Apple Pay 付了多少錢的資料 Apple 都不</label><label style="color: rgb(20, 24, 35); font-size: 15.5555562973022px; line-height: 20px;">會</label><label style="color: rgb(20, 24, 35); line-height: 20px;">知道。</label><br style="color: rgb(51, 51, 51);">
<br style="color: rgb(51, 51, 51);">
<label style="color: rgb(51, 51, 51);">&nbsp;</label>
<h2 style="line-height: 27px;">
	台灣 9 月 26 開賣，售價從 22,500 元起跳！</h2>
<br style="color: rgb(51, 51, 51); font-size: 15.5555562973022px;">
<img src="http://timg.eprice.com.tw/tw/mobile/img/2014-09/10/4912641/epic520_1_4544_7a081e946474a3c45c64d1a092dbc076.JPG" data-original="http://timg.eprice.com.tw/tw/mobile/img/2014-09/10/4912641/epic520_1_4544_7a081e946474a3c45c64d1a092dbc076.JPG" title="Apple iPhone 6 16GB 介紹圖片 - 17" alt="Apple iPhone 6 16GB 介紹圖片 - 17" border="0" style="max-width: 640px; color: rgb(51, 51, 51); font-size: 15.5555562973022px; display: inline;"><br style="color: rgb(51, 51, 51); font-size: 15.5555562973022px;">
<br style="color: rgb(51, 51, 51); font-size: 15.5555562973022px;">
<img src="http://timg.eprice.com.tw/tw/mobile/img/2014-09/10/4912641/epic520_1_4544_a413d2a76fe4678e7304cd43d27cd4ad.JPG" data-original="http://timg.eprice.com.tw/tw/mobile/img/2014-09/10/4912641/epic520_1_4544_a413d2a76fe4678e7304cd43d27cd4ad.JPG" title="Apple iPhone 6 16GB 介紹圖片 - 18" alt="Apple iPhone 6 16GB 介紹圖片 - 18" border="0" style="max-width: 640px; color: rgb(51, 51, 51); font-size: 15.5555562973022px; display: inline;"><br style="color: rgb(51, 51, 51); font-size: 15.5555562973022px;">
<label style="color: rgb(51, 51, 51); font-size: 15.5555562973022px;">▲iPhone 6 合約價格登場，199 美元起跳，而 iPhone 6 Plus 合約價則是 299 美元起跳，跟前帶代比起來沒有比較貴。iPhone 6 共有金、銀、黑三色，首波預購 9/12 開始，第一波供貨時間則是 9/19。而台灣這次很快，9 月 26 開賣就會開賣，</label><label style="color: rgb(51, 51, 51); font-size: 15.5555562973022px;">iPhone 6 16GB 售價 22,500 元，iPhone 6 Plus 16GB 售價 25,900 元起，<a href="#" data-url="http://www.eprice.com.tw/mobile/talk/4544/4912653/1/" target="_blank">點我看更多價格資訊</a>。</label><br style="color: rgb(51, 51, 51); font-size: 15.5555562973022px;">
<span class="releasedate">◎ Apple iPhone 6 預計 2014 年 9 月 26 日上市，建議售價 22,500 元。</span>				
            </div>"""

news2 = News("images/samsung_note4.png", datetime.now() )
news2.translations['zh'].title = u"Galaxy Note 5: 豈止於大"
news2.translations['en'].title = u"iPhone 6: Not only big"
news2.translations['zh'].description = u'<div>新手機上市</div>'
news2.translations['en'].description = u'<div>New iPhone</div>'
news2.translations['en'].content = u'<div>Latest iphone</div>'
news2.translations['zh'].content = u'<div>不只外型變大，更在各方面都顯著提升</div>'


db.session.add(news1)
db.session.add(news2)
db.session.commit()

brand1 = Brand()
brand1.translations['zh'].name = u"Inf0cus"
brand1.translations['en'].name = u"InF0cus"
brand2 = Brand()
brand2.translations['zh'].name = u"索尼"
brand2.translations['en'].name = u"Sony"
db.session.add( brand1 )
db.session.add( brand2 )
db.session.commit()

product_type1 = ProductType()
product_type1.translations['zh'].name = u"一般手機"
product_type1.translations['en'].name = u"Phone"
product_type2 = ProductType()
product_type2.translations['zh'].name = u"配件"
product_type2.translations['en'].name = u"Accesory"
db.session.add( product_type1 )
db.session.add( product_type2 )
db.session.commit()

product1 = Product( image_url="images/phone1.jpg", publish_time=datetime.now(), product_type_id=1 , brand_id=1 , related_product_id=0)
product1.translations['zh'].title = u"MB10"
product1.translations['en'].title = u"MB10"
product1.translations['zh'].description = u'iPhone 6 採用第二代的 64-bit A8 CPU，比前代快上 25% ！至於全新的 M8 協同晶片甚至可以辨出跑步還是踩單車的差異，就連計算距離和熱量都可以做到。'
product1.translations['en'].description = u'<div>New Phone</div>'
product1.translations['en'].content = u"""<p style="color: #F58800; padding-bottom: 6px;">■English <br>
■Support WCDMA/CDMA<br>
	  </br<></p>"""
product1.translations['zh'].content = u"""<p style="color: #F58800; padding-bottom: 6px;">■金屬外型呈現超凡質感<br>
■支援雙模式WCDMA/CDMA<br>
■4G支援FDD-LTE，並支援SV-LTE<br>
■高通S801 MSM8974AC 四核心2.5GHz<br>
■16GB (ROM) / 2GB (RAM)<br>
■13M相機 + iCatch獨立影像處理器等高檔規格<br>
■最極致的工藝，厚度6.99mm<br>
■5.5”FHD大螢幕，更清晰美麗的視覺饗宴<br>
■前後Gorilla 3最新強化玻璃<br< p=""> 
	  </br<></p>"""

product2 = Product( image_url="images/phone2.jpg", publish_time=datetime.now(), product_type_id=1 , brand_id=1, related_product_id=0 )
product2.translations['zh'].title = u"iPhone 7"
product2.translations['en'].title = u"iPhone 7"
product2.translations['zh'].description = u'iPhone 6 採用第二代的 64-bit A8 CPU，比前代快上 25% ！至於全新的 M8 協同晶片甚至可以辨出跑步還是踩單車的差異，就連計算距離和熱量都可以做到。'
product2.translations['en'].description = u'<div>New iPhone</div>'
product2.translations['en'].content = u"""<p style="color: #F58800; padding-bottom: 6px;">■金屬外型呈現超凡質感<br>
■支援雙模式WCDMA/CDMA<br>
■4G支援FDD-LTE，並支援SV-LTE<br>
■高通S801 MSM8974AC 四核心2.5GHz<br>
■16GB (ROM) / 2GB (RAM)<br>
■13M相機 + iCatch獨立影像處理器等高檔規格<br>
■最極致的工藝，厚度6.99mm<br>
■5.5”FHD大螢幕，更清晰美麗的視覺饗宴<br>
■前後Gorilla 3最新強化玻璃</br></p>"""
product2.translations['zh'].content = u"""<p style="color: #F58800; padding-bottom: 6px;">■金屬外型呈現超凡質感<br>
■支援雙模式WCDMA/CDMA<br>
■4G支援FDD-LTE，並支援SV-LTE<br>
■高通S801 MSM8974AC 四核心2.5GHz<br>
■16GB (ROM) / 2GB (RAM)<br>
■13M相機 + iCatch獨立影像處理器等高檔規格<br>
■最極致的工藝，厚度6.99mm<br>
■5.5”FHD大螢幕，更清晰美麗的視覺饗宴<br>
■前後Gorilla 3最新強化玻璃<br></p>"""


product3 = Product( image_url="images/acc1.jpg", publish_time=datetime.now(), product_type_id=2 , brand_id=2, related_product_id=2 )
product3.translations['zh'].title = u"JBL J46BT耳道式藍芽耳機"
product3.translations['en'].title = u"JBL J46BT Bluetooth"
product3.translations['zh'].description = u'線控標準三按鈕設計 ，可隨時調整音量、接聽電話或播音樂 '
product3.translations['en'].description = u'線控標準三按鈕設計 ，可隨時調整音量、接聽電話或播音樂 '
product3.translations['en'].content = u"""<p style="color: #F58800; padding-bottom: 6px;">■防汗平板線材設計 可防糾結 <br>
■最新4.0藍牙無線傳輸 <br>
■強而有力的6 mm 單體<br>
■線控標準三按鈕設計&nbsp;，可隨時調整音量、接聽電話或播音樂 <br>
■輕量化設計 輕鬆配戴或攜帶 <br>
■內附內含大、中、小各一的耳套，提供舒適配戴 <br>
</p>"""
product3.translations['zh'].content = u"""<p style="color: #F58800; padding-bottom: 6px;">■防汗平板線材設計 可防糾結 <br>
■最新4.0藍牙無線傳輸 <br>
■強而有力的6 mm 單體<br>
■線控標準三按鈕設計&nbsp;，可隨時調整音量、接聽電話或播音樂 <br>
■輕量化設計 輕鬆配戴或攜帶 <br>
■內附內含大、中、小各一的耳套，提供舒適配戴 <br>
</p>"""


db.session.add( product1 )
db.session.add( product2 )
db.session.add( product3 )
db.session.commit()
print '-'*20,'Done','-'*20


pp = Product.query.filter_by(id=2).first()
print pp.translations['zh'].title
print pp.brand.translations['zh'].name
print pp.productType.translations['zh'].name






