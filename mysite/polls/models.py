import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    #下のfieldはFieldクラスのインスタンス
    question_text = models.CharField(max_length=200)# CharField は文字のフィールド
    #CharField max_length を指定する必要
    pub_date = models.DateTimeField('date published')#DateTimeField は日時フィー ルド
    #Question モデルを編集してこれを修正
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    
class Choice(models.Model):
    #それぞれの Choice が一つの Question に関連付けられることを Django に伝えます。
    question = models.ForeignKey(Question, on_delete =models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    