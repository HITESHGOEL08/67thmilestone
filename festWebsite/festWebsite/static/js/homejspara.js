const $container = $('svg');
const $dragon_dark = $('#dragon-dark');
const $dragon_light = $('#dragon-light');
const $dragon_front = $('#dragon-front');
const $dragon_eye = $('#dragon-eye');
const $hair = $('#hair');
const $body = $('#body');
const $dress = $('#dress');
const $dress_back = $('#dress-back');
const $legs_shadow = $('#legs-shadow');
let container_w = $container.width();
let container_h = $container.height();

$(window).resize(() => {
  container_w = $container.width();
  container_h = $container.height();
});	

$(window).on('mousemove deviceorientation', event => {
  const isMobile = window.matchMedia('(max-width: 767px)').matches;
  const pos_x = isMobile ? Math.round(event.originalEvent.gamma * 50) : event.pageX;
  const pos_y = isMobile ?  Math.round(event.originalEvent.beta * 50) : event.pageY;
  let left = container_w / 2 - pos_x;
  let top  = container_h / 2 - pos_y;
  
  $('#deviceOrientation').text('gamma: ' + event.originalEvent.gamma + ' beta: ' + event.originalEvent.beta);

  function translateTween(args) {
    TweenLite.to(
      args.el,
      1, 
      { 
        css: { 
          transform: 'translateX(' + left / args.posLeft + 'px) translateY('  + top / args.posTop + 'px)'
        }, 
        ease:Expo.easeOut, 
        overwrite: 'all' 
      });
  }

  var parallaxPropsArray = [
    { el: $hair, posLeft: 100, posTop: 100},
    { el: $body, posLeft: 150, posTop: 80},
    { el: $dress, posLeft: 125, posTop: 100},
    { el: $dress_back, posLeft: 185, posTop: 120},
    { el: $legs_shadow, posLeft: -185, posTop: 400},
    { el: $dragon_eye, posLeft: 230, posTop: 200},
    { el: $dragon_dark, posLeft: 150, posTop: 300},
    { el: $dragon_light, posLeft: 200, posTop: 200},
    { el: $dragon_front, posLeft: 125, posTop: 300}
  ];

  for (i=0; i<parallaxPropsArray.length; i++) {
    translateTween(parallaxPropsArray[i]);
  }
});

$(document).mousemove(e => {
  $('.custom-cursor').position({
    my: 'left center',
    of: e,
    collision: 'none'
  });
});

// illustration by http://jerryliustudio.tumblr.com/