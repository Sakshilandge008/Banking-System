from django.shortcuts import render, redirect
from .models import User

def add_user(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        balance = request.POST.get('balance')

        # 🔥 Create user properly
        user = User.objects.create(
            full_name=full_name,
            email=email,
            current_balance=balance
        )
        user.set_password(password)   # encrypt password
        user.save()

        return redirect('home')

    return render(request, 'add_user.html')
