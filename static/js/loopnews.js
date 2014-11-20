
// var targets = $('.news-wrap').find('.news-block');

var id = null;
var i = 0;
// var total = targets.length;

function changeToNext() {

    var targets = $('.news-wrap').find('.news-block');
    var total = targets.length;

    var current_id = i;
    i++;
    i = i%total
    var next_id = i;

    var current = targets.eq(current_id);
    var next = targets.eq(next_id);

    // do something
    // console.log('fadeOut',current_id);
    // console.log('fadeIn',next_id);

    current.fadeOut(200, function(){ next.fadeIn(200); });
}


function loopnews () {

    var targets = $('.news-wrap').find('.news-block');
    targets.eq(0).fadeIn(0, function(){
        // select first item
        // $('.index-news-select-item[val=0]').addClass('news-selected');
        setInterval(changeToNext, 5000);
    });
    
}