handleclick_fisrt().then(data=>{
  let lectureId = data.lectureId;
  let tag = document.createElement('script');
  tag.src = "https://www.youtube.com/iframe_api";
  let firstScriptTag = document.getElementsByTagName('script')[0];
  firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
    
  let player;
  window.onYouTubeIframeAPIReady = function() {
    player = new YT.Player('player', {
      height: '524',
      videoId: lectureId,
      suggestedQuality: 'hd1080',
    });
  }
})
