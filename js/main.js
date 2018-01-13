$.get('/data/index.json',function(data, status){
    for (var i in data){
        movie = data[i];
        var li = $('<li></li>');
        li.addClass('list-group-item');
        var a = $('<a></a>');
        a.css('float','right');
        a.html('查看');
        li.append(a);
        var span = $('<span></span>');
        span.html(movie['movie']);
        li.append(span);
        console.log(li);
        $('#movie_list').append(li);
    }
})