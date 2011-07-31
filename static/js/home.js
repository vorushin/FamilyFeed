$(document).ready(function() {
    $(".home .action_btns a.green_grad").click(function () {
		$(".home .timeline-band-input").fadeOut(200);	
		$(".home .action_btns").animate({top:725},200);	
		$(".home .action_btns a.green_grad").text('× Close a Demo');
    });
});