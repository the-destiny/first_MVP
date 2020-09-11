var trigger_modal = document.getElementsByClassName("trigger_modal");
var trigger_close = document.getElementsByClassName("close");

$(window).on('load', function() {
    //trigger_modal[0].style.display= "block";
    trigger_close[0].addEventListener("click", closeclick, false);

    function closeclick(e){
        trigger_modal[0].style.display= "none";
    }
});
