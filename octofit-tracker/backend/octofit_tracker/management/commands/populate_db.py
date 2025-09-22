from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write('Deleting old data...')
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        self.stdout.write('Creating teams...')
        marvel = Team.objects.create(name='Marvel', description='Marvel Super Heroes')
        dc = Team.objects.create(name='DC', description='DC Super Heroes')

        self.stdout.write('Creating users...')
        users = [
            User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel),
            User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel),
            User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc),
            User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc),
        ]

        self.stdout.write('Creating activities...')
        Activity.objects.create(user=users[0], type='Run', duration=30, date=timezone.now().date())
        Activity.objects.create(user=users[1], type='Swim', duration=45, date=timezone.now().date())
        Activity.objects.create(user=users[2], type='Bike', duration=60, date=timezone.now().date())
        Activity.objects.create(user=users[3], type='Yoga', duration=20, date=timezone.now().date())

        self.stdout.write('Creating workouts...')
        w1 = Workout.objects.create(name='Cardio', description='Cardio workout')
        w2 = Workout.objects.create(name='Strength', description='Strength workout')
        w1.suggested_for.add(marvel, dc)
        w2.suggested_for.add(dc)

        self.stdout.write('Creating leaderboard...')
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        self.stdout.write(self.style.SUCCESS('Database populated with test data!'))
