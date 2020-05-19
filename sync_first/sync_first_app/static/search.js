$(document).on('click','#submit-btn',function(e){
    // this will prevent form and reload page on submit.
    e.preventDefault();
    personId = $("#person-id").val();

    $.get( "/api/get_incidents_by_id/" + personId, function ( data ) {
        var incidents = $("#incidents");
        data.forEach(function (incident) {
            console.log(incident);
            var newElement = $('<div class="card bg-light"><div class="card-body text-center"><p class="card-text">תעודת זהות מתלוננ/ת:' +
            incident['main_id'] + '</p><p class="card-text">תעודת זהות בן/בת זוג: ' +
            incident.spouse_id + '</p><p class="card-text">תאריך: ' +
            incident.date + '</p><p class="card-text">תיאור המקרה: ' +
            incident.description + '</p></div></div>')
            incidents.append(newElement);

        })})

});
