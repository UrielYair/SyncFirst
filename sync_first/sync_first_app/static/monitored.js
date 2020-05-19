function markAsViewed(incidentID) {
  $.post( "/api/mark_event_as_viewed", { event_id: incidentID })
  .done(function( data ) {
    alert( "האירוע נמחק בהצלחה" );
    document.getElementById("inc-" + incidentID).remove();
  });
}