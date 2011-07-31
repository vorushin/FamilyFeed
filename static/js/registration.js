$(document).ready(function() {
    $("form a.btn").click(function () {
		$("form").submit();
    });

    $("form").submit(function() {
        if ($("input[name=open_password]").is(":visible")) {
            $("input[name=password]").val($("input[name=open_password]").val());
        }
    });

    $("input[name=showpass]").change(function() {
        if ($(this).is(":checked")) {
            $("input[name=open_password]").val($("input[name=password]").val());
            $("input[name=password]").hide();
            $("input[name=open_password]").show().focus();
        }
        else {
            $("input[name=password]").val($("input[name=open_password]").val());
            $("input[name=open_password]").hide();
            $("input[name=password]").show().focus();
        }
    });
});