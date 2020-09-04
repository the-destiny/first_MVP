var buttons = document.getElementsByClassName("playlist__item");
var description = document.getElementsByClassName("description")[0];             
var title = document.getElementsByClassName("title")[0];  

function handleclick_fisrt(){
    axios.get(`/lecture/detail/${slug}/1/`)
        .then(function(response){
            var data = response.data.data;
            console.log(data);
                            
            var title_h4 = document.createElement("h4");
            title_h4.classList.add("title_0");
            var description_p = document.createElement("p");  
            description_p.classList.add("description_0");

            var title_text = document.createTextNode(`${data.title}`);       
            var description_text = document.createTextNode(`${data.description}`);        

            title_h4.appendChild(title_text);
            description_p.appendChild(description_text);

            title.appendChild(title_h4);
            description.appendChild(description_p);

            if (data.is_clicked){
                buttons[0].classList.add("playlist__item--clicked");
            }
        })
};

handleclick_fisrt();


function handleclick(value){
            
    var lectures = document.getElementsByClassName("playlist__item");

    axios.get(`/lecture/detail/${slug}/${value}/clicked/`)
        .then(function(response){
            var data = response.data.data;
            console.log(data);
                    
            lectures[value-1].classList.add("playlist__item--clicked");

            var title_h4 = document.createElement("h4"); 
            title_h4.classList.add(`title_${value-1}`);
            var description_p = document.createElement("p");
            description_p.classList.add(`description_${value-1}`);

            var title_text = document.createTextNode(`${data.title}`);    
            var description_text = document.createTextNode(`${data.description}`);    
            title_h4.appendChild(title_text);
            description_p.appendChild(description_text);

            is_title = document.getElementsByClassName(`title_${value-1}`)[0];
            is_description = document.getElementsByClassName(`description_${value-1}`)[0];

            if( is_title && is_description ){
            }else{
                title.appendChild(title_h4);
                description.appendChild(description_p);
            }

            var step=0;

            for (step; step < 5; step++ ){
                if (step == value-1){
                    continue;
                } 

                title_step = document.getElementsByClassName(`title_${step}`)[0];
                description_step = document.getElementsByClassName(`description_${step}`)[0];

                if( title_step && description_step ){
                    title_step.remove();
                    description_step.remove();
                }

                if(lectures[step].classList.contains("playlist__item--clicked")){
                    lectures[step].classList.remove("playlist__item--clicked");
                }
                
            };

            var clicked_lectureId = data.lectureId;
            console.log(clicked_lectureId);

        })
    }
