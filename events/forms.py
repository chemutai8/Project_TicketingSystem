from django import forms
from .models import Event, Ticket

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'venue', 'capacity', 'price']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class TicketPurchaseForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, max_value=10, initial=1)

    def __init__(self, *args, **kwargs):
        self.event = kwargs.pop('event', None)
        super().__init__(*args, **kwargs)

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        if quantity < 1:
            raise forms.ValidationError("Quantity must be at least 1")
        return quantity

    def calculate_total_price(self):
        if self.event:
            return self.cleaned_data['quantity'] * self.event.price
        return 0
