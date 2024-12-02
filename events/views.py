from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Event, Ticket
from .forms import EventForm, TicketPurchaseForm

class EventListView(ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'
    ordering = ['date']
    paginate_by = 10

class EventDetailView(DetailView):
    model = Event
    template_name = 'events/event_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['ticket_form'] = TicketPurchaseForm()
        return context

class EventCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_staff

class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_form.html'

    def test_func(self):
        return self.request.user.is_staff

class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    template_name = 'events/event_confirm_delete.html'
    success_url = '/'

    def test_func(self):
        return self.request.user.is_staff

@login_required
def purchase_ticket(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = TicketPurchaseForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            if event.available_tickets >= quantity:
                for _ in range(quantity):
                    Ticket.objects.create(event=event, user=request.user)
                messages.success(request, f'Successfully purchased {quantity} ticket(s)!')
                return redirect('event-detail', pk=pk)
            else:
                messages.error(request, 'Not enough tickets available.')
    return redirect('event-detail', pk=pk)

@login_required
def my_tickets(request):
    tickets = Ticket.objects.filter(user=request.user, is_cancelled=False)
    return render(request, 'events/my_tickets.html', {'tickets': tickets})

@login_required
def cancel_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id, user=request.user)
    if not ticket.is_cancelled:
        ticket.is_cancelled = True
        ticket.save()
        messages.success(request, 'Ticket cancelled successfully.')
    return redirect('my-tickets')