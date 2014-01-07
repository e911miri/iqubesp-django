from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    context = {
       'main': "The Journey of an IT GURU Statts with one skill",
        "block1": "Learning in sdp is having your mentor right next to you - Kola",
        "block2": "At SDP, learning has never been more fun - Wande",
        "block3": "I often ask myself why it is so cheap, 3months - 5k? it's just awesome - Orimolade M."
    }
    template_path = "home/index.djhtml"
    return render(request, template_path, context)

def login_view(request):
    if request.POST:        
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to a success page.
            else:
                return render(request, "auth/login.djhtml", {})
        else:
            # Return an 'invalid login' error message.
            return None
    else:
        return render(request, "auth/login.djhtml", {})
    
    
def logout_view(request):
    logout(request)