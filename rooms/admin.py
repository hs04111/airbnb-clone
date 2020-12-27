from django.contrib import admin
from django.utils.html import mark_safe
from . import models

# Register your models here.


@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    list_display = (
        "name",
        "used_by",
    )

    def used_by(self, obj):
        return obj.rooms.count()


# room admin에서 linine 으로 photo 를 볼 수 있게 하려면 이 클래스를 정의해야 한다

class PhotoInline(admin.TabularInline):
    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    # 위에서 정의한 클래스를 이렇게 넣으면 room admin에서 photo를 볼 수 있다.
    inlines = (PhotoInline,)

    fieldsets = (
        (
            "Spaces", {"fields": ("guests", "beds", "bedrooms", "baths",)}
        ),
        (
            "Basic Info", {"fields": (
                "name", "description", "country", "address", "price")}

        ),
        (
            "Times", {"fields": ("check_in", "check_out", "instant_book")}
        ),
        (
            "More About the Space", {"fields": (
                "amenities", "facilities", "house_rules"),
                "classes": ("collapse",)}
        ),
        (
            "Last Details", {"fields": ("host",)}
        ),

    )

    list_display = ("name",
                    "country",
                    "city",
                    "price",
                    "guests",
                    "beds",
                    "bedrooms",
                    "baths",
                    "check_in",
                    "check_out",
                    "instant_book",
                    "count_amenities",
                    "count_photos",
                    "total_rating",
                    )

    ordering = ('name', 'price', 'bedrooms',)

    list_filter = ("host__superhost",
                   "host__gender",
                   "instant_book",
                   "room_type",
                   "amenities",
                   "facilities",
                   "house_rules", "city", "country", )

    # 데이터가 많이 생기면(ex. user) admin 창에서 검색할 수 있는 기능을 준다.
    raw_id_fields = ("host",)

    search_fields = ("^city", "=host__username")

    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",)

    def count_amenities(self, obj):  # obj는 보통 리스트의 현재 row
        return obj.amenities.count()

    def count_photos(self, obj):
        return obj.photos.count()

    count_photos.short_description = "Photo Count"
    count_amenities.short_description = "count_amenities"  # list의 해당 model 제목


@ admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition """

    list_display = ('__str__', "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px", src="{obj.file.url}" />')
        # mark_safe는 html이나 javascript 등을 장고 사이트에서 안전하게 볼 수 있다는 표시. 없으면 장고 페이지에서 작동하지 않는다.
        # dir(obj.file)을 print해보면 여러가지가 있는데, 그 중에 url도 있어서 위처럼 쓸 수 있는 것.

    get_thumbnail.short_description = "Thumbnail"
