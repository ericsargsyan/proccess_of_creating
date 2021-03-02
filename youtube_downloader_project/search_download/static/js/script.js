/*
$(document).ready(function(){
    $.ajax({
        url: "https://www.googleapis.com/youtube/v3/search",
        data: {
            key: "AIzaSyCaqHzxkAae1dnKY-ZJ7JTzPC4TWlbb4Dg",
            q: name,
            type: "video",
            maxResults: 1,
        },
        success: function(res){
            console.log(res);
            for( let i=0; i<res.items.length; i++) {
                let el = '<div class="result"><iframe width="400" height="300" src="https://www.youtube.com/embed/${res.items[i].id.videoId}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>'
                $('.video').append(el);
                }
            }
    })
})*/
