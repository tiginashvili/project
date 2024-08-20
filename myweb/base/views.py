from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Note, User, Type
from .forms import MyUserCreationForm, NoteForm, UserForm

def home(request):
    notes = Note.objects.filter(creator=request.user.id)
    context = {"notes": notes}
    return render(request, 'base/home.html', context)

def login_page(request):
    page = "login"
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, "User doesn't exist!")
            return render(request, "base/login_register.html", {"page": page})

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username or Password is incorrect!")

    return render(request, "base/login_register.html", {"page": page})

def logout_user(request):
    logout(request)
    return redirect('home')

def register_page(request):
    form = MyUserCreationForm()
    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "An error occurred during registration")

    return render(request, 'base/login_register.html', {'form': form})

def add_note(request):
    types = Type.objects.all()
    form = NoteForm()
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            messages.error(request, "Error occurred while adding the note!")

    return render(request, 'base/add_note.html', {'form': form, 'types': types})

def delete_note(request, id):
    note = Note.objects.get(id=id)
    if request.method == "POST":
        note.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': note})

@login_required(login_url='login')
def update_user(request):
    user = request.user
    form = UserForm(instance=user)
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, "base/update-user.html", {'form': form})

def python(request):
    return render(request, 'base/python.html')

def cpp(request):
    return render(request, 'base/cpp.html')

