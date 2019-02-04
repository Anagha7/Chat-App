from django.db import models

# Create your models here.

class Message(models.Model):
    ch1 = (('send','s'),
        ('receive','r'))
    ch2 = (('send','s')('receive',r)('delivered',d))
    chat_id = models.IntegerField('Chat_ID', primary_key=True)
    time = models.DateTimeField('Date', blank=False)
    message = models.CharField('Messages',max_length=1000)
    attachments = models.FileField('Attachments',upload_to='attachments/')
    sor = models.CharField('Send/Receive',choices=ch1)
    g_id = models.ForeignKey(Group,verbose_name="Group_ID")
    u_id = models.ForeignKey(User,verbose_name='User_ID')
    status =models.CharField('Status',choices=ch2)