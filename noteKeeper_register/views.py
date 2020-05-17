from django.shortcuts import render, redirect
from .form import NoteForm 
from .models import noteKeeper

# Create your views here.
def note_list(request):
    context = {'note_list':noteKeeper.objects.all()}
    return render(request, "noteKeeper_register/note_list.html", context) 

def note_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = NoteForm()
        else:
            note = noteKeeper.objects.get(pk=id)
            form = NoteForm(instance=note)
        return render(request, "noteKeeper_register/note_form.html", {'form':form})
    else:
        if id == 0:
            form = NoteForm(request.POST)
        else:
            note = noteKeeper.objects.get(pk=id)
            form = NoteForm(request.POST, instance = note)

        if form.is_valid():
            form.save()

        return redirect('/note/list')

def note_delete(request, id):
    note = noteKeeper.objects.get(pk = id)
    note.delete()
    return redirect('/note/list')

