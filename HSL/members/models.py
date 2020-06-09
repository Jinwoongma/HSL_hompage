from django.db import models

# Create your models here.
class Member(models.Model):
    COURSE_CHOICES = (
        ('Undergraduate', 'Undergraduate'),
        ('Master', 'Master'),
        ('Doctor', 'Doctor'),
        ('Professor', 'Professor')
    )
    name = models.CharField(max_length=100)
    course = models.CharField(
        max_length=20,
        choices=COURSE_CHOICES,
        default='UD',
    )
    photo = models.ImageField(upload_to="members_image", blank=True)
    is_graduate = models.BooleanField()
    work_space = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name
