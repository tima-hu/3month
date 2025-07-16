from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title': 'Geek',
        'image': 'https://jymysh.kg/media/orders/photos/Frame_38.webp',
        'description': 'Geek is a platform for learning programming and IT skills.'
    }
    return render(request, 'index.html', context=context)
 