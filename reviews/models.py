from django.db import models
from core import models as core_models


class Review(core_models.TimeStampedModel):

    """ Review Model Definition """

    review = models.TextField()
    accuracy = models.IntegerField()
    cleanliness = models.IntegerField()
    communication = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()
    user = models.ForeignKey(
        "users.User", related_name="reviews", on_delete=models.CASCADE)
    room = models.ForeignKey(
        "rooms.Room", related_name="reviews", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.review} - {self.room}'

    def rating_average(self):  # 모델에 이렇게 함수를 만들어야 admin 뿐만 아니라 모든 사이트에서 사용할 수 있다
        avg = (self.accuracy +
               self.cleanliness +
               self.communication +
               self.location +
               self.check_in +
               self.value)/6

        return round(avg, 2)

    rating_average.short_description = "Avg."
