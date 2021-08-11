// demo day change

console.log("script running!")

function dayChange() {
  $("#your-bar").css("width", "100%").html("<span>YOU</span><span>7 Day</span>");
}

// select routines change input 
$(".list-group-item").on("focus", function() {
  $("#routine-input").val(
    $(this).html()).css("color", "slategrey");
})