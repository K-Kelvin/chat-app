from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipient")
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ('-date', )
    
    def __str__(self):
        return f'{self.message}'

    def get_all_messages(id_1, id_2):
        ''' Gets all messages between users with id_1 and id_2 '''
        messages = []
        # get messages from sender to recipient
        sender_messages = Message.objects.filter(sender_id=id_1, recipient_id=id_2).order_by('-date')
        for x in range(len(sender_messages)):
            sender_messages[x].is_read = True
            messages.append(sender_messages[x])

        # get messages from recipient to sender
        recipient_messages = Message.objects.filter(sender_id=id_2, recipient_id=id_1).order_by('-date')
        for x in range(len(recipient_messages)):
            recipient_messages[x].is_read = True
            messages.append(recipient_messages[x])

        messages.sort(key=lambda x: x.date, reverse=False)
        return messages

    def sent(self, request):
        if self.sender.id == request.user.id:
            return True
        return False
