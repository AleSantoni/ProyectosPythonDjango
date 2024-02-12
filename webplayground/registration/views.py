from .form import UserCreationformWithEmail, ProfileForm, EmailForm
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django import forms
from .models import Profile




class SignUpView(CreateView):
    form_class =  UserCreationformWithEmail
    template_name = 'registration/signup.html'
    
    def get_success_url(self):
        return reverse_lazy('login') + '?register'
    # metodo para recuperar el formulario
    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form()
        # modificar en tiempo real
        form.fields['username'].widget=forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Nombre de usuario'})
        form.fields['email'].widget=forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder':'Dirección email'})
        form.fields['password1'].widget=forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Contraseña'})
        form.fields['password2'].widget=forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Repetir contraseña'})
        return form
    
    
@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
        form_class=ProfileForm
        
        success_url=reverse_lazy('profile')
        template_name='registration/profile_form.html'
        
        def get_object(self):
            # recuperar el objeto que se va a editar
            try:
                return Profile.objects.get(user=self.request.user)
            except Profile.DoesNotExist:
                return Profile.objects.create(user=self.request.user)
            
@method_decorator(login_required, name='dispatch')
class EmailUpdate(UpdateView):
    form_class = EmailForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_email_form.html'

    def get_object(self):
        # recuperar el objeto que se va editar
        return self.request.user

    def get_form(self, form_class=None):
        form = super(EmailUpdate, self).get_form()
        # Modificar en tiempo real
        form.fields['email'].widget = forms.EmailInput(
            attrs={'class':'form-control mb-2', 'placeholder':'Email'})
        return form