var trigger_modal = document.getElementsByClassName("trigger-modal");
var trigger_close = document.getElementsByClassName("trigger-modal__form__close");

if(lecture_count>=3){ //우선은 3개 이상으로 해둠
    $(window).on('load', function() {
        trigger_close[0].addEventListener("click", closeclick, false);
        function closeclick(e){
            trigger_modal[0].style.display= "none";
        }
    });
}else{
    trigger_modal[0].style.display="none"
};
