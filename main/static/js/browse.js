$(document).ready(function(){
	$(".artist_name").click(function(e) {
		$.get("get_albums",{"artist_name" : e.target.id}, function(data) {
			$("#albums_list").empty();
			for (var i=0; i<data.count; i++)
			{
				$("#albums_list").append('<li class="album_listing"><span>'+data.results[i].albumName+
				'</span><br><img src="' + data.results[i].artworkUrl100 + '" alt="' + data.results[i].albumName +
				'" height="100" width="100"></li>')
			}
		});
	});
});