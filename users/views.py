from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from users.forms import LoginForm, RegisterForm


class IndexView(TemplateView):
    template_name = 'users/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = LoginForm()
        context['form_cad'] = RegisterForm()
        return context


class LoginView(TemplateView):
    template_name = 'users/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = LoginForm()
        context['form_cad'] = RegisterForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            if User.objects.filter(username=username).exists():
                user = authenticate(username=username, password=password)

                if user is not None:
                    login(request, user)
                    return redirect(reverse('user', kwargs={'pk': user.pk}))
                else:
                    messages.error(request, 'Senha incorreta.')
                    context = {'form': form}
                    return render(request, 'users/login.html', context)
            messages.error(request, 'Usuário não localizado. Você pode se cadastrar ou fazer o login com um email registrado.')
            context = {'form': form}
        else:
            messages.error(request, 'Email ou senha inválidos.')
            context = {'form': form, 'no_user': True}

        return render(request, 'users/login.html', context)


class UserView(LoginRequiredMixin, TemplateView):
    template_name = 'users/user.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hidden_password'] = '*' * len(self.request.user.password)
        context['form'] = LoginForm()
        context['form_cad'] = RegisterForm()
        return context


class UserRegisterView(TemplateView):
    template_name = 'users/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = LoginForm()
        context['form_cad'] = RegisterForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email já cadastrado, Faça o login ou tente outro email.')
                context = {'form_cad': form, 'form': LoginForm()}
                return render(request, 'users/error_register.html', context)
            
            user = form.save(commit=False)

            full_name = form.cleaned_data['name']
            name_parts = full_name.split(' ', 1) 
            first_name = name_parts[0]
            last_name = name_parts[1] if len(name_parts) > 1 else ''

            user.username = email
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            login(request, user)
            return redirect('user', pk=user.pk)
        else:
            context = {'form_cad': form, 'form': LoginForm()}
            return render(request, 'users/error_register.html', context)


class UserChangeView(LoginRequiredMixin, TemplateView):
    template_name = 'users/change.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = LoginForm()
        form.fields['username'].label = 'Novo Email (deixe em branco se não deseja alterar)'
        form.fields['username'].required = False
        form.fields['password'].label = 'Nova Senha (deixe em branco se não deseja alterar)'
        form.fields['password'].required = False
        context['form'] = form
        context['form_cad'] = RegisterForm()
        return context

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        form.fields['username'].required = False
        form.fields['password'].required = False

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = User.objects.filter(username=request.user.username).first()
            if username:
                user.email = username
                user.username = username
                user.save()

            if password:
                user.set_password(password)
                user.save()

                updated_user = authenticate(request, username=user.username, password=password)
                if updated_user is not None:
                    login(request, updated_user)

        context = {'form_cad': RegisterForm(), 'form': form}
        return render(request, 'users/change.html', context)


def custom_logout(request):
    logout(request)
    return redirect('index')
