from django.contrib import admin

from .models import ResearchPaper, Car, CarPhoto

class CarPhotoInline(admin.StackedInline):
    model = CarPhoto
    extra = 0

class CarAdmin(admin.ModelAdmin):
    inlines = [CarPhotoInline]

    def save_model(self, request, obj, form, change):
        obj.save()

        for i, afile in enumerate(request.FILES.getlist('photos_multiple')):
            print(afile)
            obj.image.save(f'img-{i}', afile)

admin.site.register(Car, CarAdmin)
admin.site.register(ResearchPaper)
