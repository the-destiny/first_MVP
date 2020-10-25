let classInfo = document.getElementsByClassName("class__info")[0];
let navInfo = document.getElementsByClassName("class__nav__info")[0];
let navPlaylist = document.getElementsByClassName("class__nav__playlist")[0];

if(!classInfo.classList.contains("class__info__on")){
  classInfo.classList.add("class__info__on");
}

if(!navInfo.classList.contains("class__nav__info__on")){
  navInfo.classList.add("class__nav__info__on");
}

function infoClick(){
  let classInfo = document.getElementsByClassName("class__info")[0];
  let playlist = document.getElementsByClassName("class__playlist")[0];

  if(playlist.classList.contains("class__playlist__on")){
    playlist.classList.remove("class__playlist__on");
  }

  if(!classInfo.classList.contains("class__info__on")){
    classInfo.classList.add("class__info__on");
  }

  if(!navInfo.classList.contains("class__nav__info__on")){
    navInfo.classList.add("class__nav__info__on");
  }

  if(navPlaylist.classList.contains("class__nav__playlist__on")){
    navPlaylist.classList.remove("class__nav__playlist__on");
  }
}

function playlistClick(){
  let classInfo = document.getElementsByClassName("class__info")[0];
  let playlist = document.getElementsByClassName("class__playlist")[0];

  if(classInfo.classList.contains("class__info__on")){
    classInfo.classList.remove("class__info__on");
  }

  if(!playlist.classList.contains("class__playlist__on")){
    playlist.classList.add("class__playlist__on");
  }

  if(!navPlaylist.classList.contains("class__nav__playlist__on")){
    navPlaylist.classList.add("class__nav__playlist__on");
  }

  if(navInfo.classList.contains("class__nav__info__on")){
    navInfo.classList.remove("class__nav__info__on");
  }
}
