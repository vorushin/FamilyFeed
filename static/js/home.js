$(document).ready(function() {
    $(".home .action_btns a.green_grad").click(function () {
        showDemo();
    });
});

function showDemo() {
    $(".home .timeline-band-input").fadeOut(200);	
    $(".home .action_btns").animate({top:725},200);	
    $(".home .action_btns a.green_grad").text('× Close a Demo');
    $(".home .action_btns a.green_grad").click(function() {
        hideDemo();
    });
}

function hideDemo() {
    console.log("***** hideDemo");
    $(".home .timeline-band-input").fadeIn(200);   
    $(".home .action_btns").animate({top:500},200); 
    $(".home .action_btns a.green_grad").text('See a Demo');
    $(".home .action_btns a.green_grad").click(function() {
        showDemo();
    });
}
