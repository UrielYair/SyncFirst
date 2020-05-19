function markAsMonitored(personID) {
  $.post( "/api/mark_person_as_monitored", { person_id: personID })
  .done(function( data ) {
    alert( "הועבר לטיפול בהצלחה" );
    document.getElementById("per-" + personID).remove();
  });
}