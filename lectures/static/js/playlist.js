let playlistButtons = document.getElementsByClassName("playlist__item");
let lectureDescription = document.getElementsByClassName("lecture__description")[0];             
let lectureTitle = document.getElementsByClassName("lecture__title")[0];  

window.handleclick_fisrt = function (){
  return axios.get(`/lecture/detail/${slug}/1/`)
    .then(
      function(response){
        let data = response.data.data;
                            
        let lectureTitle_h4 = document.createElement("h4");
        let lectureDescription_p = document.createElement("p");  
        lectureTitle_h4.classList.add("title_0");
        lectureDescription_p.classList.add("description_0");

        let lectureTitle_text = document.createTextNode(`${data.title}`);       
        let lectureDescription_text = document.createTextNode(`${data.description}`);        
        lectureTitle_h4.appendChild(lectureTitle_text);
        lectureDescription_p.appendChild(lectureDescription_text);

        lectureTitle.appendChild(lectureTitle_h4);
        lectureDescription.appendChild(lectureDescription_p);
        if (data.is_clicked) {
          playlistButtons[0].classList.add("playlist__item--clicked");
        }

      return response.data.data;
      }
    )
};

function get_data(value){
  let playlists = document.getElementsByClassName("playlist__item");
  
  return axios.get(`/lecture/detail/${slug}/${value}/clicked/`)
    .then(
      function(response) {
        let data = response.data.data;

        let lectureTitle_h4 = document.createElement("h4");
        let lectureDescription_p = document.createElement("p");
        lectureTitle_h4.classList.add(`title_${value-1}`);
        lectureDescription_p.classList.add(`description_${value-1}`);

        let lectureTitle_text = document.createTextNode(`${data.title}`);
        let lectureDescription_text = document.createTextNode(`${data.description}`);
        lectureTitle_h4.appendChild(lectureTitle_text);
        lectureDescription_p.appendChild(lectureDescription_text);

        is_title = document.getElementsByClassName(`title_${value-1}`)[0];
        is_description = document.getElementsByClassName(`description_${value-1}`)[0];
        if (is_title && is_description) {
        } else {
          lectureTitle.appendChild(lectureTitle_h4);
          lectureDescription.appendChild(lectureDescription_p);
        }

        playlists[value-1].classList.add("playlist__item--clicked");

        for (let step=0; step < playlists.length; step++ ) {
          if (step == value-1) {
            continue;
          } 

          playlistTitle = document.getElementsByClassName(`title_${step}`)[0];
          playlistDescription = document.getElementsByClassName(`description_${step}`)[0];

          if (playlistTitle && playlistDescription) {
            playlistTitle.remove();
            playlistDescription.remove();
          }
          if(playlists[step].classList.contains("playlist__item--clicked")){
            playlists[step].classList.remove("playlist__item--clicked");
          }
        };

        return data;
      }
    )
};
  
function handleclick(value){
  get_data(value)
    .then(function(response){
      let lectureId = response.lectureId;
      let iframe = document.getElementsByTagName("iframe")[0];
      iframe.src = `https://www.youtube.com/embed/${lectureId}?enablejsapi=1&origin=http%3A%2F%2F127.0.0.1%3A8000&widgetid=1` 
    })
}
