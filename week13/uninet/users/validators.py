from django.core.exceptions import ValidationError

MAX_FILE_SIZE = 1024000


def validate_file_size(value):
    print(value)
