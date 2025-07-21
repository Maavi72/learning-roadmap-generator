from django.shortcuts import render
from .models import LearningGoal

def home(request):
    goals = LearningGoal.objects.all()
    return render(request, 'roadmap/home.html', {'goals': goals})

from .models import LearningGoal, Topic
from django.shortcuts import get_object_or_404

def roadmap_detail(request, goal_id):
    goal = get_object_or_404(LearningGoal, id=goal_id)
    topics = Topic.objects.filter(goal=goal).order_by('week')
    return render(request, 'roadmap/roadmap_detail.html', {'goal': goal, 'topics': topics})
