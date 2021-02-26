from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from bugtracker.models import TicketModel
from bugtracker.form import TicketForm
from myuser.models import MyUser
# Create your views here.
@login_required
def home_view(request):
    tickets = TicketModel.objects.all()
    return render(request, 'home.html', {'tickets':tickets})
@login_required
def ticket_view(request, ticket_id):
    ticket = TicketModel.objects.get(id=ticket_id)
    return render(request, 'ticket.html', {'ticket': ticket})
#  HttpResponseRedirect(request.GET.get('next', reverse('home')))
@login_required
def add_ticket_view(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_ticket = TicketModel.objects.create(
            title=data['title'],
            description=data['description'],
            user=request.user
            )
            return redirect('ticket view', ticket_id=new_ticket.id)
    form = TicketForm()
    return render(request, 'form.html', {'form': form})

@login_required
def edit_ticket_view(request, ticket_id):
    ticket = TicketModel.objects.get(id=ticket_id)
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            ticket.title = data['title']
            ticket.description = data['description']
            ticket.save()
            return redirect('ticket view', ticket_id=ticket.id)
    form = TicketForm(initial={
        'title': ticket.title,
        'description': ticket.description
    })
    return render(request, 'form.html', {'form': form})

@login_required
def change_status(request, ticket_id):
    ticket = TicketModel.objects.get(id=ticket_id)
    if ticket.status == 'new':
        ticket.status = 'in_progress'
        ticket.user_assigned = request.user
    elif ticket.status == 'in_progress':
        ticket.status = 'done'
        ticket.completed_by = ticket.user_assigned
        ticket.user_assigned = None
    ticket.save()
    return redirect('ticket view', ticket_id=ticket.id)

@login_required
def invalid_ticket(request, ticket_id):
    ticket = TicketModel.objects.get(id=ticket_id)
    ticket.status = 'invalid'
    ticket.save()
    return redirect('ticket view', ticket_id=ticket.id)

    
@login_required
def user_view(request, user_id):
    my_user = MyUser.objects.get(id=user_id)
    tickets = TicketModel.objects.filter(user=my_user)
    return render(request, 'user.html', {'user':my_user, 'tickets': tickets})