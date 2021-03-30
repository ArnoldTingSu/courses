from django.db import models


# Create your models here.
class CourseManager(models.Manager):
    def validate_course(self, postData):
        errors = {}
        if len(postData["course_name"]) < 5:
            errors["course_name"] = "Course must be at least 5 characters long!"
        if len(postData["description"]) < 15:
            errors["description"] = "Description must be at least 15 characters long!"
        return errors

class Course(models.Model):
    name=models.CharField(max_length=225)
    desc=models.TextField()
    add_date=models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects = CourseManager()
