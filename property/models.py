from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):
    new_building = models.BooleanField('Новостройка', default=None, db_index=True)
    created_at = models.DateTimeField(
        'Когда создано объявление',
        default=timezone.now,
        db_index=True)

    description = models.TextField('Текст объявления', blank=True)
    price = models.IntegerField('Цена квартиры', db_index=True)

    town = models.CharField(
        'Город, где находится квартира',
        max_length=50,
        db_index=True)
    town_district = models.CharField(
        'Район города, где находится квартира',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное')
    address = models.TextField(
        'Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4')
    floor = models.CharField(
        'Этаж',
        max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж')

    rooms_number = models.IntegerField(
        'Количество комнат в квартире',
        db_index=True)
    living_area = models.IntegerField(
        'количество жилых кв.метров',
        null=True,
        blank=True,
        db_index=True)

    has_balcony = models.NullBooleanField('Наличие балкона', db_index=True)
    active = models.BooleanField("Активно-ли объявление", db_index=True)
    construction_year = models.IntegerField(
        "Год постройки здания",
        null=True,
        blank=True,
        db_index=True)

    who_liked = models.ManyToManyField(
        User,
        related_name="liked_posts",
        verbose_name="Кто лайкнул"
    )

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'


class Complain(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        related_name="complain"
    )
    flat = models.ForeignKey(
        Flat,
        on_delete=models.CASCADE,
        verbose_name="Квартира",
        related_name="complain"
    )
    complain = models.TextField("Жалоба")

    def __str__(self):
        return f'{self.user}{self.flat}'


class Owner(models.Model):
    owner = models.CharField(
        verbose_name="ФИО владельца",
        max_length=200,
        db_index=True)
    owners_phonenumber = models.CharField(
        "Номер владельца",
        max_length=20,
        db_index=True)
    owner_pure_phone = PhoneNumberField(
        null=True,
        blank=True,
        verbose_name="Нормализованный номер владельца",
        db_index=True
    )
    flat_property = models.ManyToManyField(
        "Flat",
        related_name="owners",
        verbose_name='Квартиры в собственности'
    )

    def __str__(self):
        return f'{self.owner}'
