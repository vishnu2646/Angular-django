from django.db import models

# Create your models here.
class Team(models.Model):
    teamId = models.AutoField(primary_key=True)
    teamName = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.teamName

class Employee(models.Model):
    employeeId = models.AutoField(primary_key=True)
    employeeName = models.CharField(max_length=255)
    dateofJoined = models.DateField()
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team')
    image = models.ImageField('images/')

    def __str__(self) -> str:
        return self.employeeName

    def __unicode__(self):
        return self.employeeName

    @property
    def team_name(self):
        return self.team.teamName