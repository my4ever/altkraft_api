import random
import string

from api.models import UsedCode, ValidCode
from altkraft_api.settings import NUMBER_OF_VALID_CODE


def checking_codes() -> None:
    """
    Checks for buffered table of valid codes to be filled.
    If code is uniq adds it into UsedCode, ValidCode table.
    Other way repeats the loop.
    """
    # Checking for number of valid codes equals to emout set as NUMBER_OF_VALID_CODE.
    while ValidCode.objects.all().count() < NUMBER_OF_VALID_CODE + 1:
        code = generate_code()
        # Checking for existence of generated code in DB.
        while UsedCode.objects.filter(code=code).count() != 0:
            code = generate_code()
        # Adding uniq code into tables ValidCode and UsedCode.
        ValidCode.objects.create(code=code)
        UsedCode.objects.create(code=code)


def generate_code() -> str:
    """Generates 8 digits code."""
    return ''.join(random.choices(string.digits + string.ascii_letters, k=8))