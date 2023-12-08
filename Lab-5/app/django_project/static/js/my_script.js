$(document).ready(function() {
    $('#id_genres').change(function() {
        var selectedGenre = $(this).val();
        var apiUrl = 'http://api.filmon.com/api/vod/search?genre=' + selectedGenre;

        console.log('Solicitud AJAX a:', apiUrl);

        $.ajax({
            url: apiUrl,
            type: 'GET',
            success: function(data) {
                console.log('Respuesta de la API:', data);
                updateTable(data.movies);  // Ajusta esto según la estructura real de la respuesta
            },
            error: function(error) {
                console.log('Error en la solicitud AJAX:', error);
            }
        });
    });

    function updateTable(movies) {
        var tbody = $('table tbody');
        tbody.empty();

        $.each(movies, function(index, movie) {
            var row = $('<tr>');
            row.append('<td>' + movie.name + '</td>');
            row.append('<td>' + movie.description + '</td>');
            row.append('<td><img src="' + movie.image.url + '" style="width:100px"/></td>');
            row.append('<td><a href="/movie/' + movie.id + '">Ver detalles</a></td>');
            tbody.append(row);
        });
    }
});

