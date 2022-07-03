from django.contrib import admin
from .models import Course, Lesson, Faq, FaqData, Quiz, QuizData

# Register your models here.


class LessonAdmin(admin.StackedInline):
    model = Lesson
    extra = 0


class CourseAdmin(admin.ModelAdmin):
    list_display = ("title",)
    inlines = [LessonAdmin, ]


class FaqDataAdmin(admin.StackedInline):
    model = FaqData
    extra = 0


class FaqAdmin(admin.ModelAdmin):
    list_display = ("title", )
    inlines = [FaqDataAdmin, ]


class QuizDataAdmin(admin.StackedInline):
    model = QuizData
    extra = 0


class QuizAdmin(admin.ModelAdmin):
    list_display = ("title", )
    inlines = [QuizDataAdmin, ]


admin.site.register(Course, CourseAdmin)
admin.site.register(Faq, FaqAdmin)
admin.site.register(Quiz, QuizAdmin)

