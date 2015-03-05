# -*- coding: utf-8 -*-

from django.db import models
import time, datetime


class Message(models.Model):

    type = models.IntegerField(default=0)  # 1前摄像头图  2后摄像头图  3声音  4 PGS信息
    file_path = models.CharField(max_length=4000)
    log_time = models.BigIntegerField(default=0)

    latitude = models.FloatField(default=0)  # 维度
    longitude = models.FloatField(default=0)  # 经度
    altitude = models.FloatField(default=0)  # 海拔高度
    address = models.CharField(default='',max_length=1000)  # 地址
    name = models.CharField(default='',max_length=200)  # 名称

    def __str__(self):
        return "目标正在经度 %s, 纬度 %s, 海拔 %s 米处活动。" % (self.longitude, self.latitude, self.altitude)


