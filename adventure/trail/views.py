from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, TemplateView, ListView, DetailView
from .models import Trail
from django.db.models import Q


class HomeView(View):
    def get(self, request):
        trails = Trail.objects.all()
        return render(request, 'home.html', {'trails': trails})


class UserCreateView(CreateView):
     model = User
     fields = ['username','email','password']
     success_url = reverse_lazy('home')




# class AddTrailView(LoginRequiredMixin, View):
#     def get(self,request):
#         form = AddTrailForm()
#         return render(request,'add_trail.html',{'form': form})
#
#     def post(self,request):
#         form = AddTrailForm(request.POST)
#         if form.is_valid():
#             Trail.objects.create(
#                 name = form.cleaned_data['name'],
#                 type_tour = form.cleaned_data['type_tour'],
#                 difficulty = form.cleaned_data['difficulty'],
#                 distance = form.cleaned_data['distance'],
#                 time_tour = form.cleaned_data['time_tour'],
#                 description = form.cleaned_data['description'],
#                 creator = request.user
#             )
#         return render(request,'add_trail.html', {'forms': form})


class AddTrailView(CreateView):
    model = Trail
    template_name = 'trail_form.html'
    fields = ['name', 'type_tour', 'difficulty', 'distance', 'time_tour', 'description', 'photo']

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super(AddTrailView, self).form_valid(form)

    def get_success_url(self):
        return reverse('trail-view', args=(self.object.id,))


class HomePageView(TemplateView):
    template_name = "home.html"


class SearchTrailView(ListView):
    model = Trail
    template_name = "search_trail.html"

    def get_queryset(self):
        trail_type = self.request.GET.get('trail', '')
        trail_name = self.request.GET.get('trail_name', '')
        trail_difficulty = self.request.GET.get('trail_difficulty', '')
        trail_time = self.request.GET.get('trail_time', '')

        query_by_trail = Q(type_tour=trail_type)
        query_by_name = (Q(name__icontains=trail_name) | Q(description__icontains=trail_name))
        query_by_difficulty = Q(difficulty=trail_difficulty)
        query_by_time = Q(time_tour=trail_time)

        final_query = query_by_trail
        if trail_name:
            final_query = final_query & query_by_name
        if trail_difficulty:
            final_query = final_query & query_by_difficulty
        if trail_time:
            final_query = final_query & query_by_time

        object_list = Trail.objects.filter(final_query)
        return object_list


class TrailView(DetailView):
    model = Trail
    template_name = "trail_view.html"


class ContactView(TemplateView):
    template_name = 'contact.html'

class UsersView(TemplateView):
    model = User
    template_name = 'users.html'

    def get_users(self,request):
        users = User.objects.all()
        return render(request, 'users.html', {'users': users})
