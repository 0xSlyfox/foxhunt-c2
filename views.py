from django.shortcuts import render, redirect
from .models import Log, Note
from .forms import NoteForm, EventForm
from django.http import HttpRequest

def get_client_ip(request: HttpRequest) -> str:
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def log_list(request):
    logs = Log.objects.all().order_by('-timestamp')
    return render(request, 'log_list.html', {'logs': logs})

def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.host_ip = get_client_ip(request)
            note.save()
            return redirect('log_list')
    else:
        form = NoteForm(initial={'host_ip': get_client_ip(request)})
    return render(request, 'note_form.html', {'form': form})

def add_edit_event(request, note_id, sequence_number=None):
    note = Note.objects.get(pk=note_id)

    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.note = note
            if sequence_number is not None:
                event.sequence_number = sequence_number
            event.save()
            return redirect('log_list')
    else:
        if sequence_number is not None:
            event = Event.objects.get(note=note, sequence_number=sequence_number)
            form = EventForm(instance=event)
        else:
            form = EventForm()
    
    return render(request, 'event_form.html', {'form': form, 'note_id': note_id, 'sequence_number': sequence_number})

