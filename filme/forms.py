from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms


class FormHomepage(forms.Form):
    email = forms.EmailField(
        label=False,
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Seu e-mail",
                "class": "w-full md:w-7/12 px-4 py-3 rounded-md text-black text-base focus:outline-none focus:ring-2 focus:ring-red-600"
            }
        )
    )



class CriarContaForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Modernização: deixar inputs mais bonitos com Tailwind
        for campo in self.fields.values():
            campo.widget.attrs.update({
                "class": "bg-white/10 border border-white/20 text-white rounded-md px-3 py-2 w-full focus:outline-none focus:ring-2 focus:ring-red-500 placeholder-gray-300"
            })