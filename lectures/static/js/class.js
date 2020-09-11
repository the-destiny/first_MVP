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
  let playlist = document.getElementsByClassName("playlist")[0];
  let classInfo_off = document.getElementsByClassName("class")[0];

  if(playlist.classList.contains("playlist__on")){
    playlist.classList.remove("playlist__on");
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

  if(classInfo_off.classList.contains("class__off")){
    classInfo_off.classList.remove("class__off");
  }
}

function playlistClick(){
  let classInfo = document.getElementsByClassName("class__info")[0];
  let playlist = document.getElementsByClassName("playlist")[0];
  let classInfo_off = document.getElementsByClassName("class")[0];

  if(classInfo.classList.contains("class__info__on")){
    classInfo.classList.remove("class__info__on");
  }

  if(!playlist.classList.contains("playlist__on")){
    playlist.classList.add("playlist__on");
  }

  if(!navPlaylist.classList.contains("class__nav__playlist__on")){
    navPlaylist.classList.add("class__nav__playlist__on");
  }

  if(navInfo.classList.contains("class__nav__info__on")){
    navInfo.classList.remove("class__nav__info__on");
  }

  if(!classInfo_off.classList.contains("class__off")){
    classInfo_off.classList.add("class__off");
  }
}
