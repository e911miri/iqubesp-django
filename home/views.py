from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "home/index.djhtml", {
        'main': "The Journey of an IT GURU Statts with one skill",
        "block1": "Learning in sdp is having your mentor right next to you - Kola",
        "block2": "At SDP, learning has never been more fun - Wande",
        "block3": "I often ask myself why it is so cheap, 3months - 5k? it's just awesome - Orimolade M."
    })