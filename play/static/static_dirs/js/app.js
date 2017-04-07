$(function () {
    $('ul.tab-nav li a.button').click(function () {
        var href = $(this).attr('href');

        $('li a.active.button', $(this).parent().parent()).removeClass('active');
        $(this).addClass('active');

        $('.tab-pane.active', $(href).parent()).removeClass('active');
        $(href).addClass('active');

        return false;
    });
});

$(function () {
    $('div.side_btn').click(function () {
        var href = 'div' + $(this).attr('id');
        console.log(href);
        $('div.side_btn').removeClass('active');
        $(this).addClass('active');

        $('.tab-pane.active').removeClass('active');
        $("#" + href).addClass('active');


        return false;
    });
});

$(function () {
    $('#search').keyup(function () {
        if ($("#search").val() == "") {
            console.log("hi")
            $("#search-result").hide();
            return;
        }else $("#search-result").show();
        $.ajax({
            type: "POST",
            url: "/search/",
            data: {
                'search_text': $("#search").val(),
                'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
            },
            success: searchSuccess,
            dataType: 'html'

        })
    })
});

function searchSuccess(data, textStatus, jqXHR) {
    $('#searchList').html(data);
}

$(document).ready(function () {
 $("#search-result").hide();
});