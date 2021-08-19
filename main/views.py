from django.shortcuts import redirect, render, get_object_or_404
from .models import NotePad

# Create your views here.

def notepads(request):
    notes = NotePad.objects.order_by('-date_created')
    
    context = {
        'notes' : notes
    }
    
    if request.method == 'POST':
        data = dict(title = request.POST['title'], description=request.POST['description'], body=request.POST['body'])
        

        NotePad.objects.create(**data)

        return redirect('notelist')
    return render(request, 'notepad_list.html', context)



def note_detail(request, title, day, month, year):
    note = get_object_or_404(NotePad, title=title, date_created__day=day, date_created__month=month, date_created__year=year)
    
    context = {
        'note' : note
    }

    if request.method == 'POST':
           

        data= get_object_or_404(NotePad, title=title, date_created__day=day, date_created__month=month, date_created__year=year)
    
        data.title=request.POST['title']
        data.description=request.POST['description']
        data.body=request.POST['body']
        data.save()

        return redirect('notelist') 

        
        

        
    return render(request, 'notepad.html', context)
