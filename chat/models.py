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


class RoomMember(models.Model):
    room = models.ForeignKey("Room", on_delete=models.CASCADE, related_name="room")
    member = models.ForeignKey(User, on_delete=models.CASCADE, related_name="member")

    def __str__(self):
        return f'<Room<{self.room_id}>: User<{self.member}>/>'


class Room(models.Model):
    title = models.CharField(max_length=86)
    description = models.CharField(max_length=324)
    is_group = models.BooleanField(default=False)

    def __str__(self):
        return '<Room: {self.pk}>'

    def add_member(self, user):
        ''' Handle adding a member to a room '''
        if self.is_group:
            # check if limit is reached
            # add member if not
            # RoomMember.objects.create(room=self, member=user)
            pass
        else:
            # if (self.room_member_set.count() < 2)
                # member = RoomMember.objects.create(room=self, member=user)
                # self.room_member_set.add(member=user)
            pass

    def has_member(self, member):
        ''' Check if a member exists in a room '''
        # if member in self.room_member_set
        # return True
        # otherwise
        return False

    def get_inbox_id(self, member1, member2):
        ''' Check if both members are in a room which is not a group '''
        # if both member 1 and member2 are in a room which is not a group
        # return the room id
        # otherwise return false
        # add the members to room 
        # return the room id
        pass
