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
