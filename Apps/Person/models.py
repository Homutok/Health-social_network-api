from datetime import datetime

from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models
from django_countries.fields import CountryField
from Achievement.models import Achievement


class Person(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE, related_name='public_user_info')
    date_of_birth = models.DateField(null=True, blank=True)  # Дата рождения
    summary = models.CharField(max_length=1000, db_index=True, null=True, blank=True)  # Информация о пользователе
    photo = models.ForeignKey('PersonPhoto', on_delete=models.SET_NULL, null=True, default=30,
                              related_name='photo_for_user')
    MALE = 'male'
    FEMALE = 'female'
    OTHER = 'other'
    GENDER_CHOICE = (
        (MALE, 'Мужчина'),
        (FEMALE, 'Женщина'),
        (OTHER, 'Другие'),
    )
    person_gender = models.CharField(max_length=50, null=True, choices=GENDER_CHOICE, blank=True, default='other',
                                     help_text='Половая '
                                               'принадлежность')
    country = CountryField(null=True, blank=True)  # Страна проживания
    person_height = models.IntegerField(null=True, blank=True)
    place_of_study = models.CharField(max_length=1000, db_index=True, null=True,
                                      blank=True)  # Информация о пользователе
    release_date = models.DateField(null=True, blank=True)  # Информация о пользователе

    def create_profile(self, user):
        new_person = Person(user=user, country='RU')
        new_person.save()

    class Meta:
        ordering = ['user']

    def __str__(self):
        return str(self.user.username)


class PersonHealth(models.Model):
    persons_data = models.ForeignKey(User, on_delete=models.PROTECT, null=True, related_name='health_for_user')
    date_of_check = models.DateField(null=True, blank=True)
    person_weight = models.IntegerField(null=True, blank=True)
    person_dream = models.IntegerField(null=True, blank=True)
    person_pulse = models.IntegerField(null=True, blank=True)
    person_steps_per_day = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['date_of_check']

    def __str__(self):
        return '[' + str(self.persons_data.id) + ']' + str(self.persons_data) + '-' + str(self.id) + '_' + str(
            self.date_of_check)


class PersonPhoto(models.Model):
    person_photo = models.FileField(upload_to='article/profile_photo',
                                    # height_field=None,
                                    validators=[FileExtensionValidator(['svg'])],
                                    null=True)  # Фотография пользователя

    def __str__(self):
        return self.person_photo.name


class PersonAchievement(models.Model):
    persons_data = models.ForeignKey(User, on_delete=models.CASCADE, related_name='achievement_for_user')
    achievement_data = models.ForeignKey(Achievement, on_delete=models.CASCADE, related_name='achievements')

    def __str__(self):
        return str(self.persons_data) + '---' + str(self.achievement_data)
