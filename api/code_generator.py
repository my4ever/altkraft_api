import random
import string

from api.models import UsedCode, ValidCode
from altkraft_api.settings import NUMBER_OF_VALID_CODE


def generate_code() -> None:
    """
    Generates 8 digits code.
    Checks if such code exists in UsedCode.
    If code uniq adds code into ValidCode table.
    Other way repeats the loop.
    """
    while len(ValidCode.objects.all()) < NUMBER_OF_VALID_CODE:
        code = ''.join(random.choices(string.digits + string.ascii_letters, k=8))
        while len(UsedCode.objects.filter(code=code)) != 0:
            code = ''.join(random.choices(string.digits + string.ascii_letters, k=8))
        # Adding uniq code into tables ValidCode and UsedCode
        ValidCode.objects.create(code=code)
        UsedCode.objects.create(code=code)
