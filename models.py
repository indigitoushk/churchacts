from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _


class Person(models.Model):
    TYPES_CHOICES = (
        ('PAST', _('Pastor')),
        ('STAF', _('Church Staff')),
    )
    SEX_CHOICES = (
        ('F', _('Female')),
        ('M', _('Male')),
    )
    MARITAL_STATUS_CHOICES = (
        ('DI', _('Divorced')),
        ('MA', _('Married')),
        ('SI', _('Single')),
        ('WI', _('Widowed')),
    )
    user = models.ForeignKey(User, related_name='person_user', \
                             verbose_name=_('User'), \
                             on_delete=models.SET_NULL, \
                             null=True, blank=True)
    type = models.CharField(verbose_name=_('Type of Person'), max_length=4, \
                            choices=TYPES_CHOICES, null=True, blank=True)
    attendance = models.IntegerField(verbose_name=_('Number of Attendance'), \
                                     default=0)
    alt_name = models.CharField(verbose_name=_('Alternative Name'), \
                                max_length=100, null=True, blank=True)
    sex = models.CharField(verbose_name=_('Sex'), max_length=3, \
                           choices=SEX_CHOICES, null=True, blank=True)
    dob = models.DateField(verbose_name=_('Date of Birth'), \
                           null=True, blank=True)
    marital_status = models.CharField(verbose_name=_('Marital Status'), max_length=2, \
                               choices=MARITAL_STATUS_CHOICES, null=True, blank=True)
    phone = models.CharField(verbose_name=_('Phone Number'), max_length=20, \
                             null=True, blank=True)
    date_accept_christ = models.DateField(verbose_name=_('Date of Accepting Christ'), \
                                          null=True, blank=True)

    def __unicode__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def list_pastors(self):
        return PastoralCare.objects.filter(member=self)

    def list_ministries(self):
        return Ministry.objects.filter(member=self)


class PastoralCare(models.Model):
    pastor = models.ForeignKey(Person, related_name='pastor', \
                               verbose_name=_('Pastor'), \
                               on_delete=models.SET_NULL, \
                               null=True, blank=True)
    member = models.ForeignKey(Person, related_name='member', \
                               verbose_name=_('Member'), \
                               on_delete=models.SET_NULL, \
                               null=True, blank=True)


class Ministry(models.Model):
    member = models.ForeignKey(Person, related_name='ministry_member', \
                               verbose_name=_('Member'), \
                               on_delete=models.SET_NULL, \
                               null=True, blank=True)
    description = models.CharField(verbose_name=_('Description'), max_length=100)
    remark = models.TextField(verbose_name=_('Remark'), \
                              null=True, blank=True)
    start_time = models.DateTimeField(verbose_name=_('Start Time'), \
                                      null=True, blank=True)
    end_time = models.DateTimeField(verbose_name=_('End Time'), \
                                    null=True, blank=True)


class Meeting(models.Model):
    TYPES_CHOICES = (
        ('ME', 'Meeting'),
        ('GP', 'Group'),
        ('FE', 'Fellowship'),
    )
    type = models.CharField(verbose_name=_('Type of Meeting'), max_length=4, \
                            choices=TYPES_CHOICES, null=True, blank=True)
    start_time = models.DateTimeField(verbose_name=_('Start Time'), \
                                      null=True, blank=True)
    end_time = models.DateTimeField(verbose_name=_('End Time'), \
                                    null=True, blank=True)
    remark = models.TextField(verbose_name=_('Remark'), \
                              null=True, blank=True)
    action = models.TextField(verbose_name=_('Action'), \
                              null=True, blank=True)

    def list_participants(self):
        return MeetingParticipant.objects.filter(meeting=self)


class MeetingParticipant(models.Model):
    ROLE_CHOICES = (
        ('PA', 'Pastor'),
        ('GE', 'General'),
    )
    meeting = models.ForeignKey(Meeting, related_name='meeting', \
                                verbose_name=_('Meeting'), \
                                on_delete=models.SET_NULL, \
                                null=True, blank=True)
    person = models.ForeignKey(Person, related_name='person', \
                               verbose_name=_('Member'), \
                               on_delete=models.SET_NULL, \
                               null=True, blank=True)
    role = models.CharField(verbose_name=_('Role'), max_length=4, \
                            choices=ROLE_CHOICES, null=True, blank=True)
    cost = models.FloatField(verbose_name=_('Cost'), default=0)
    remark = models.TextField(verbose_name=_('Remark'), \
                              null=True, blank=True)
    action = models.TextField(verbose_name=_('Action'), \
                              null=True, blank=True)