from .models import Person, Incident
from django.db.models.query import QuerySet

MINIMAL_NUMBER_OF_INCIDENTS = 2


def is_at_risk(person):
    """
    This function determines whether a person might be at risk or not.
    If you change the criterion for what qualifies as a risk, you must change this function.
    :return: True / False
    """
    if len(person.incidents_reported_by.all()) >= MINIMAL_NUMBER_OF_INCIDENTS:
        return True
    else:
        return False


def is_a_threat(person):
    """
    This function determines whether a person might be a threat or not.
    If you change the criterion for what qualifies as a threat, you must change this function.
    :return: True / False
    """
    if len(person.incidents_reported_about.all()) >= MINIMAL_NUMBER_OF_INCIDENTS:
        return True
    else:
        return False


def get_at_high_risk():
    all_people = Person.objects.all()
    at_risk = []
    for person in all_people:
        if is_at_risk(person):
            at_risk.append({"person": person.identification,
                            "number_of_incidents": len(person.incidents_reported_by.all())})

    return at_risk


def get_might_be_a_threat():
    all_people = Person.objects.all()
    a_threat = []
    for person in all_people:
        if is_a_threat(person):
            a_threat.append({"person": person.identification,
                             "number_of_incidents": len(person.incidents_reported_about.all())})

    return a_threat


def get_monitored_people():
    return Person.objects.filter(status="pending")


def get_events_for_people(people):
    """
    Get all the events associated with given people.
    """
    events = QuerySet(model=Incident)
    for person in people:
        events = events | person.incidents_reported_about.all() | person.incidents_reported_by.all()

    return events
