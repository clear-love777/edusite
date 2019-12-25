from django.db import models
from user.models import User

# Create your models here.


# 课程类
class Course(models.Model):
    course_name = models.CharField(max_length=16,verbose_name="课程名")
    course_tercher = models.IntegerField(verbose_name="课程老师ID")
    # 课程时间 "3-5" 周三 第五节课
    course_time = models.CharField(max_length=16,verbose_name="课程时间")
    course_student_amount = models.IntegerField("最多可选学生数",default=50)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    updated_time = models.DateTimeField('更新时间', auto_now=True)
    course_desc = models.TextField("课程描述",default="")
    user = models.ManyToManyField(User)

class Score(models.Model):
    score = models.IntegerField("考试分数",default=0)
    # 分数对应课程
    course = models.OneToOneField(Course)
    # 分数对应学生
    user = models.OneToOneField(User)

