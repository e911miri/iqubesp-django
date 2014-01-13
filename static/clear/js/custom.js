// MAIN CONFIGS -> Replace with your data
var twitter_username = 'Envato', 
    google_map_address = 'Mountain View, CA 94043';





// Main navigation 
$(function () {
    $('#flexnav').flexNav();
});


// Self Hosted video plugin
$('audio,video').mediaelementplayer();


// Responsive videos
$(document).ready(function () {
    $("body").fitVids();
});


// Bootstrap accordion
$('.accordion').on('show', function (e) {
    $(e.target).prev('.accordion-heading').find('.accordion-toggle').addClass('active');
});

$('.accordion').on('hide', function (e) {
    $(e.target).prev('.accordion-heading').find('.accordion-toggle').removeClass('active');
});

$("#accordion-toggle .collapse").collapse();

// Bootstrap tooltips
$('[data-toggle="tooltip"]').tooltip();


// Gridrotator (Home page image grid script)
$(function () {
    $('#ri-grid').gridrotator({
        rows: 4,
        columns: 8,
        animType: 'random',
        animSpeed: 1200,
        interval: 1200,
        step: 'random',
        preventClick: false,
        maxStep: 2,
        w1024: {
            rows: 4,
            columns: 6
        },
        w768: {
            rows: 3,
            columns: 3
        },
        w480: {
            rows: 4,
            columns: 4
        },
        w320: {
            rows: 5,
            columns: 4
        },
        w240: {
            rows: 6,
            columns: 4
        }
    });

});

// Gridrotator without animation (for sliders layout)
$(function () {
    $('#ri-grid-no-animation').gridrotator({
        rows: 4,
        columns: 8,
        slideshow: false,
        w1024: {
            rows: 4,
            columns: 6
        },
        w768: {
            rows: 3,
            columns: 3
        },
        w480: {
            rows: 4,
            columns: 4
        },
        w320: {
            rows: 5,
            columns: 4
        },
        w240: {
            rows: 6,
            columns: 4
        }
    });

});


// Lighbox gallery
$('#popup-gallery').each(function () {
    $(this).magnificPopup({
        delegate: 'a.popup-gallery-image',
        type: 'image',
        gallery: {
            enabled: true
        }
    });
});

// Lighbox image
$('.popup-image').magnificPopup({
    type: 'image'
});

// Lighbox text
$('.popup-text').magnificPopup({
    removalDelay: 500,
    closeBtnInside: true,
    callbacks: {
        beforeOpen: function () {
            this.st.mainClass = this.st.el.attr('data-effect');
        }
    },
    midClick: true
});

// Lightbox iframe
$('.popup-iframe').magnificPopup({
    dispableOn: 700,
    type: 'iframe',
    removalDelay: 160,
    mainClass: 'mfp-fade',
    preloader: false
});


// Mixitup filter (isotope alternative)
$(function () {
    $('#mixitup-grid').mixitup();
});


// Content slider
$(function () {
    $('#wilto-slider-wrap').wiltoSlider();
});
// Uncomment this to allow mutiple content sliders on one page (can slow perfomance)
// $(function () {
//     $('.wilto-slider-wrap').wiltoSlider();
// });


// Twitter list (on sidebar area)
$(function ($) {
    $("#twitter").tweet({
        username: twitter_username, 
        count: 3
    });
});

// Twitter ticker (page footer)
$(function ($) {
    $("#twitter-ticker").tweet({
        username: twitter_username, 
        page: 1,
        count: 20
    });
});
$(document).ready(function () {
    var ul = $('#twitter-ticker').find(".tweet-list");
    var ticker = function () {
        setTimeout(function () {
            ul.find('li:first').animate({
                marginTop: '-4.7em'
            }, 850, function () {
                $(this).detach().appendTo(ul).removeAttr('style');
            });
            ticker();
        }, 5000);
    };
    ticker();
});


// Google maps
$(function () {
    $('#gmap').gmap3({
        marker: {
            address: google_map_address 
        },
        map: {
            options: {
                zoom: 14
            }
        }
    });
});


// Nivo slider
$(window).load(function () {
    $('#nivo-slider').nivoSlider({
        effect: 'fade',
        prevText: '',
        nextText: ''
    });
});
// Uncomment this to allow mutiple nivo sliders on one page (can slow perfomance)
// $(window).load(function () {
//     $('.nivo-slider').nivoSlider({
//         prevText: '',
//         nextText: ''
//     });
// });


// Elastic slider
$(function () {
    $('#ei-slider').eislideshow({
        easing: 'easeOutExpo',
        titleeasing: 'easeOutExpo',
        autoplay: true,
        slideshow_interval: 3000
    });
});
// Uncomment this to allow mutiple elastic sliders on one page (can slow perfomance)
// $(function () {
//     $('.ei-slider').eislideshow({
//         easing: 'easeOutExpo',
//         titleeasing: 'easeOutExpo',
//         autoplay: true,
//         slideshow_interval: 3000
//     });
// });

// Hide elements before load
$('.show-onload').show();