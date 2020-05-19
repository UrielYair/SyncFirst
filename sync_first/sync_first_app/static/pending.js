function changePersonStatus(personID, status, message) {
  $.post("/api/change_person_status", { person_id: personID, status: status })
  .done(function( data ) {
    alert(message);
    document.getElementById("per-" + personID).remove();
  });
}

function markAsMonitored(personID) {
  changePersonStatus(personID, "monitored", "הועבר לטיפול בהצלחה" );
}
function markAsRefuse(personID) {
  changePersonStatus(personID, "refuse", "סומן כסירוב" );
}
function markAsIrrelevant(personID) {
  changePersonStatus(personID, "irrelevant", "סומן כלא רלוונטי" );
}