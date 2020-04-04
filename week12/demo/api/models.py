from django.db import models
from .validators import validate_extension, validate_file_size


class Course(models.Model):
    name = models.CharField(max_length=50)
    syllabus = models.FileField(upload_to='course_files',
                                validators=[validate_extension],
                                null=True, blank=True)
    logo = models.ImageField(upload_to='course_files',
                             validators=[validate_file_size],
                             null=True, blank=True)

    def __str__(self):
        return f'{self.name}'
