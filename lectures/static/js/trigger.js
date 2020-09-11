var trigger_modal = document.getElementsByClassName("trigger_modal");
var trigger_close = document.getElementsByClassName("close");

if(lecture_history>=3){
    $(window).on('load', function() {
        trigger_close[0].addEventListener("click", closeclick, false);
        function closeclick(e){
            trigger_modal[0].style.display= "none";
        }
    });
}else{
    trigger_modal[0].style.display="none"
};
