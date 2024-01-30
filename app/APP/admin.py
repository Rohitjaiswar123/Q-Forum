from django.contrib import admin
from .models import institute , Comment, questions
# Register your models here.
admin.site.register(institute)


admin.site.register(Comment)
admin.site.register(questions)
