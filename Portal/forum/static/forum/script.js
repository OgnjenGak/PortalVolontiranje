function addComment ( url ) {
    var id = $( "#id" ).val ( );
    var sadrzaj = $( "#id_sadrzaj" ).val ( );
    var csrfToken = $( "input[name=\"csrfmiddlewaretoken\"]" ).val ( );

    $.ajax ({
        url: url,
        type: "POST",
        data: {
            id: id,
            csrfmiddlewaretoken: csrfToken,
            sadrzaj: sadrzaj
        },
        success: function ( result, status, xhr ) {
            $( "#tbody" ).html ( result );
            $( "#id_sadrzaj" ).val ( "" );
        },
        error: function ( xhr, status, error ) {
            var response =  xhr.responseJSON;

            for ( const key in response ) {
                var selector = "#" + key;
                var errors = response[key];

                $( selector ).html ( errors );
            }
        }
    })
}