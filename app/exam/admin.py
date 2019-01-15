from django.contrib import admin

from . import models as exam_models

admin.site.register(exam_models.Question)
admin.site.register(exam_models.Answer)
admin.site.register(exam_models.Exam)
admin.site.register(exam_models.CompletedExam)