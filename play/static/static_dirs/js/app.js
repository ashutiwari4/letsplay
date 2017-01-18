$(document).ready(function () {

})


function loadData(url,page_no) {
    var page_count = 10;
    $.ajax({
        url: "api/song_links/?format=json", success: function (result) {
            console.log(result)
            for (var i = 0; i < page_count; i++) {
                $("#song_id").append("ashu");
            }
        }
    });
}