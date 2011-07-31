$(document).ready(function() {
    var demoVisible = false;
    $(".home .action_btns a.green_grad").click(function () {
        if (!demoVisible) {
            showDemo();
        } else {
            hideDemo();
        }
        demoVisible = !demoVisible;
    });
});

function showDemo() {
    $(".home .timeline-band-input").fadeOut(200);	
    $(".home .action_btns").animate({top:725},200);	
    $(".home .action_btns a.green_grad").text('× Close a Demo');
}

function hideDemo() {
    $(".home .timeline-band-input").fadeIn(200);   
    $(".home .action_btns").animate({top:500},200); 
    $(".home .action_btns a.green_grad").text('See a Demo');
}
