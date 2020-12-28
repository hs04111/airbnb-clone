from django.db import models
from django.urls import reverse
from django_countries.fields import CountryField
from core import models as core_models
# from users import models as user_models #Room model에 사용하기 위해 import했으나, 밑에서 'users.User'로 스트링으로 적으면 장고는 알아서 잘 찾는다.


class AbstractItem(core_models.TimeStampedModel):
    """ Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):

    """ RoomType Model Definition"""
    class Meta:
        verbose_name = "Room Type"


class Amenity(AbstractItem):
    """ Amenity Model Definition"""
    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):
    """ Facility Model Definition"""
    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):
    """ HouseRule Model Definition"""
    class Meta:
        verbose_name = "House Rule"


class Photo(core_models.TimeStampedModel):
    """ Photo Model Definition """
    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="room_photos")
    room = models.ForeignKey(
        "Room", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Room(core_models.TimeStampedModel):

    """ Room Model Definition"""

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(
        'users.User', related_name="rooms", on_delete=models.CASCADE)
    room_type = models.ForeignKey(
        'RoomType', related_name="rooms", on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField(
        'Amenity', related_name="rooms", blank=True)
    facilities = models.ManyToManyField(
        'Facility', related_name="rooms", blank=True)
    house_rules = models.ManyToManyField(
        'HouseRule', related_name="rooms", blank=True)

    def __str__(self):
        return self.name

    # model에 무엇인가 저장될 때 이를 중간에서 가로채서 무언가를 한 후 다시 저장으로 보내는 메소드.
    # 중간에 처리를 한 후 super()를 사용하여 기존의 save() 메소드를 불러와야 한다.

    def save(self, *args, **kwargs):
        self.city = str.capitalize(self.city)
        super().save(*args, **kwargs)

    # admin에서 바로 사이트로 가게 해주는 메소드. view함수의 name과 url의 변수를 reverse에 넣어 return한다.
    def get_absolute_url(self):
        return reverse('rooms:detail', kwargs={'pk': self.pk})

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        for review in all_reviews:
            all_ratings += review.rating_average()
        if len(all_reviews) != 0:
            return round(all_ratings / len(all_reviews), 2)
        else:
            return 0
