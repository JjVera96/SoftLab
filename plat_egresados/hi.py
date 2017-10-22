from app.models import User
from django.contrib.auth.models import Group
User.objects.all()
Group.objects.all()
yo = User.objects.get(identification='1087559573')
yo = User.objects.get(username='1087559573')
tu = User.objects.get(identification='1087556034')
tu = User.objects.get(username='1087556034')
yo.groups.all()
tu.groups.all()

