handleclick_fisrt().then(data=>{
  var lectureId = data.lectureId;
  var tag = document.createElement('script');

  tag.src = "https://www.youtube.com/iframe_api";
  var firstScriptTag = document.getElementsByTagName('script')[0];
  firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

  var player;
  window.onYouTubeIframeAPIReady = function() {
    player = new YT.Player('player', {
        height: '524',
        videoId: lectureId,
        suggestedQuality: 'hd1080',
    });
  }
})
