from django.shortcuts import render, redirect
from home.models import Task
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Home view for task submission
def home(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        private = request.POST.get("private") == 'on'
        
        # Create and save the task linked to the logged-in user
        task = Task(title=title, description=description, private=private, user=request.user)
        task.save()
        messages.success(request, "Your task has been submitted successfully!")
        return redirect('tasks')
    
    return render(request, "index.html")

# View for displaying tasks
@login_required  # Ensures only logged-in users can access this view
def tasks(request):
    # Fetch tasks created by the logged-in user
    tasks = Task.objects.filter(user=request.user)
    return render(request, "tasks.html", {'tasks': tasks})
