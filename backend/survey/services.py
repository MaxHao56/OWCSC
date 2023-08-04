from .models import Responses, Questions
from .exceptions import RadioValueException


def convert_radio_value_to_boolean(radio_value: str) -> bool:
    """converts values from HTML template to bool, if HTML update then update this function"""
    if radio_value == 'yes':
        return True
    elif radio_value == 'no':
        return False
    else:
        raise RadioValueException


def create_response(
        user_id: int,
        question_id: int,
        survey_name: str,
        value: bool):
    """creating or updating Response object with positive or negative answer"""
    obj, created = Responses.objects.update_or_create(
        question_id=question_id,
        user_id=user_id,
        survey_type_id=survey_name)
    obj.response = Responses.Status.POSITIVE if value else Responses.Status.NEGATIVE
    obj.save()
