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

    def sent(self, request):
        if self.sender.id == request.user.id:
            return True
        return False

    @staticmethod
    def add_new(sender_uname, recipient_uname, message):
        ''' Save messages to the database once provided sender and receipient usernames '''
        sender = User.objects.get(username=sender_uname)
        recipient = User.objects.get(username=recipient_uname)
        message = Message.objects.create(sender=sender, recipient=recipient, message=message)
        return message

    @staticmethod
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


class RoomMember(models.Model):
    room = models.ForeignKey("Room", on_delete=models.CASCADE, related_name="room")
    member = models.ForeignKey(User, on_delete=models.CASCADE, related_name="member")

    def __str__(self):
        return f'<Room<{self.room_id}>: User<{self.member}>/>'

    @staticmethod
    def has_member(member):
        found = RoomMember.objects.filter(member=member)
        if len(found) > 0:
            return True
        return False

    @staticmethod
    def has_member_and_room(member, room):
        found = RoomMember.objects.filter(member=member, room=room)
        if len(found) > 0:
            return True
        return False


class Room(models.Model):
    title = models.CharField(max_length=86)
    description = models.CharField(max_length=324)
    is_group = models.BooleanField(default=False)
    hash = models.CharField(max_length=64, null=True)

    def __str__(self):
        return f'<Room: {self.pk}>'

    def add_member(self, user):
        ''' Handle adding a member to a room '''
        if self.is_group:
            # check if limit is reached
            # add member if not
            # RoomMember.objects.create(room=self, member=user)
            pass
        else:
            if len(self.roommember_set) < 2:
                RoomMember.objects.create(room=self, member=user)
                return True
            return False

    def has_member(self, member):
        ''' Check if a member exists in a room '''
        return RoomMember.has_member_and_room(member, self)

    @staticmethod
    def get_or_create(username1, username2):
        ''' Get a room id having both user1 and user2, if it exists, otherwise create it '''
        lst = [username1, username2]
        lst.sort()
        hash = "-".join(lst)
        try:
            room = Room.objects.get(hash=hash)
        except Room.DoesNotExist:
            room = Room.objects.create(hash=hash)

        user1 = User.objects.get(username=username1)
        user2 = User.objects.get(username=username2)

        RoomMember.objects.get_or_create(room=room, member=user1)
        RoomMember.objects.get_or_create(room=room, member=user2)
        return room.pk
