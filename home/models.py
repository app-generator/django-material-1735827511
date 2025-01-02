# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Player(models.Model):

    #__Player_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    teamid = models.ForeignKey(team, on_delete=models.CASCADE)

    #__Player_FIELDS__END

    class Meta:
        verbose_name        = _("Player")
        verbose_name_plural = _("Player")


class Team(models.Model):

    #__Team_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)

    #__Team_FIELDS__END

    class Meta:
        verbose_name        = _("Team")
        verbose_name_plural = _("Team")


class Boards(models.Model):

    #__Boards_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)

    #__Boards_FIELDS__END

    class Meta:
        verbose_name        = _("Boards")
        verbose_name_plural = _("Boards")


class Tournament(models.Model):

    #__Tournament_FIELDS__
    startdate = models.DateTimeField(blank=True, null=True, default=timezone.now)
    enddate = models.DateTimeField(blank=True, null=True, default=timezone.now)
    numberofrounds = models.IntegerField(null=True, blank=True)
    tournamenttypeid = models.ForeignKey(tournament_type, on_delete=models.CASCADE)

    #__Tournament_FIELDS__END

    class Meta:
        verbose_name        = _("Tournament")
        verbose_name_plural = _("Tournament")


class Tournament_Type(models.Model):

    #__Tournament_Type_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    legsorsets = models.TextField(max_length=255, null=True, blank=True)
    bestofnumber = models.IntegerField(null=True, blank=True)
    points = models.IntegerField(null=True, blank=True)

    #__Tournament_Type_FIELDS__END

    class Meta:
        verbose_name        = _("Tournament_Type")
        verbose_name_plural = _("Tournament_Type")


class Game(models.Model):

    #__Game_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    tournamentid = models.ForeignKey(tournament, on_delete=models.CASCADE)
    boardid = models.ForeignKey(boards, on_delete=models.CASCADE)
    matchdate = models.DateTimeField(blank=True, null=True, default=timezone.now)
    hometeamid = models.ForeignKey(team, on_delete=models.CASCADE)
    awayteamid = models.ForeignKey(team, on_delete=models.CASCADE)
    callerid = models.ForeignKey(player, on_delete=models.CASCADE)
    roundnumber = models.IntegerField(null=True, blank=True)
    playoffid = models.ForeignKey(playoff, on_delete=models.CASCADE)

    #__Game_FIELDS__END

    class Meta:
        verbose_name        = _("Game")
        verbose_name_plural = _("Game")


class Result(models.Model):

    #__Result_FIELDS__
    gameid = models.ForeignKey(game, on_delete=models.CASCADE)
    homeset = models.IntegerField(null=True, blank=True)
    awayset = models.IntegerField(null=True, blank=True)
    homelegs = models.IntegerField(null=True, blank=True)
    awaylegs = models.IntegerField(null=True, blank=True)

    #__Result_FIELDS__END

    class Meta:
        verbose_name        = _("Result")
        verbose_name_plural = _("Result")


class Game_Statistics(models.Model):

    #__Game_Statistics_FIELDS__
    gameid = models.ForeignKey(game, on_delete=models.CASCADE)
    resultid = models.ForeignKey(result, on_delete=models.CASCADE)
    teamid = models.ForeignKey(team, on_delete=models.CASCADE)
    playerid = models.ForeignKey(player, on_delete=models.CASCADE)
    setswon = models.IntegerField(null=True, blank=True)
    setslost = models.IntegerField(null=True, blank=True)
    legswon = models.IntegerField(null=True, blank=True)
    legslost = models.IntegerField(null=True, blank=True)
    average = models.IntegerField(null=True, blank=True)
    highestcheckout = models.IntegerField(null=True, blank=True)
    checkout = models.IntegerField(null=True, blank=True)
    status = models.TextField(max_length=255, null=True, blank=True)

    #__Game_Statistics_FIELDS__END

    class Meta:
        verbose_name        = _("Game_Statistics")
        verbose_name_plural = _("Game_Statistics")


class Playoff(models.Model):

    #__Playoff_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    tournamentid = models.ForeignKey(tournament, on_delete=models.CASCADE)

    #__Playoff_FIELDS__END

    class Meta:
        verbose_name        = _("Playoff")
        verbose_name_plural = _("Playoff")



#__MODELS__END
