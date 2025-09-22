from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class BasicModelTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Marvel', description='Marvel Team')
        self.assertEqual(str(team), 'Marvel')

    def test_user_creation(self):
        team = Team.objects.create(name='DC', description='DC Team')
        user = User.objects.create(name='Clark Kent', email='clark@dc.com', team=team)
        self.assertEqual(str(user), 'Clark Kent')

    def test_activity_creation(self):
        team = Team.objects.create(name='Marvel', description='Marvel Team')
        user = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=team)
        activity = Activity.objects.create(user=user, type='Run', duration=30, date='2025-09-22')
        self.assertEqual(str(activity), 'Tony Stark - Run (2025-09-22)')

    def test_workout_creation(self):
        team = Team.objects.create(name='Marvel', description='Marvel Team')
        workout = Workout.objects.create(name='Cardio', description='Cardio workout')
        workout.suggested_for.add(team)
        self.assertEqual(str(workout), 'Cardio')

    def test_leaderboard_creation(self):
        team = Team.objects.create(name='DC', description='DC Team')
        leaderboard = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(str(leaderboard), 'DC Team - 100 pts')
