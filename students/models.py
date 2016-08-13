from django.db import models

# Create your models here.

class Student(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
      (MALE, 'Male'),
      (FEMALE, 'Female')
    )
    name = models.CharField(max_length = 100)
    birthday = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    #class Meta:
    #    abstract = True


class GradeSchoolStudent(Student):
    KINDERGARTEN = 'Y0'
    FIRST = 'Y1'
    SECOND = 'Y2'
    THIRD = 'Y3'
    FOURTH = 'Y4'
    FIFTH = 'Y5'
    SIXTH = 'Y6'
    SEVENTH = 'Y7'
    EIGHTH = 'Y8'
    NINETH = 'Y9'
    TENTH = '10'
    ELEVENTH = '11'
    TWELVETH = '12'
    YEAR_IN_SCHOOL_CHOICES = (
        (KINDERGARTEN, 'Kindergarten'),
        (FIRST, '1st Grade'),
        (SECOND, '2nd Grade'),
        (THIRD, '3rd Grade'),
        (FOURTH, '4th Grade'),
        (FIFTH, '5th Grade'),
        (SIXTH, '6th Grade'),
        (SEVENTH, '7th Grade'),
        (EIGHTH, '8th Grade'),
        (NINETH, '9th Grade'),
        (TENTH, '10th Grade'),
        (ELEVENTH, '11th Grade'),
        (TWELVETH, '12th Grade'),
    )
    year_in_school = models.CharField(max_length=2,
                                      choices=YEAR_IN_SCHOOL_CHOICES)


class CollegeStudent(Student):
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    YEAR_IN_SCHOOL_CHOICES = (
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    )
    year_in_school = models.CharField(max_length=2,
                                      choices=YEAR_IN_SCHOOL_CHOICES)