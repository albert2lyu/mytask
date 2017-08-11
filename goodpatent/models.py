# coding = utf-8
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils import timezone

class GoodPatent(models.Model):
    theExaminer = models.ForeignKey(User)

    appNO = models.CharField(u'申请号', max_length = 13, default = u'无')
    appIPC = models.CharField(u'分类号', max_length = 15, default = u'无')
    appName = models.CharField(u'发明名称', max_length=100, default = u'无')

    recReason = models.TextField(u'推荐理由', max_length = 500, default = u'无')
    techProblem = models.TextField(u'技术问题', max_length = 500, default = u'无')
    techNovelty = models.TextField(u'技术方案', max_length = 500, default = u'无')
    techAdvantange = models.TextField(u'技术效果', max_length = 500, default = u'无')
    claims = models.TextField(u'权利要求', max_length = 1000, default = u'无')
    concept = models.TextField(u'发明构思', max_length = 300, default = u'无')
    techLevel = models.TextField(u'技术水平', max_length = 300, default = u'无')
    techHeight = models.TextField(u'创新高度', max_length = 300, default = u'无')
    market = models.TextField(u'市场运用效果和社会影响', max_length = 300, default = u'无')

    class Meta : 
        verbose_name = u'有价值专利'
        verbose_name_plural = u'有价值专利'
