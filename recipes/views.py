from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Recipe
from .forms import RecipeCreatForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import DeleteView,DetailView,UpdateView

# Create your views here.




def index(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes':recipes,
        'name':"Rina"
    }
    return render(request,'home.html',context)


def entree_page(request):
    return render(request,'Entrees.html',
                  {'entrees':Recipe.objects.filter(category='entrees')})


def desserts_page(request):
    return render(request,'desserts.html',
                  {'desserts':Recipe.objects.filter(category='desserts')})


def appetizers(request):
    
    return render(request,'appetizers.html',
                  {'appetizers':Recipe.objects.filter(category='appetizers')})

@login_required
def add_recipe(request):
    form =  RecipeCreatForm()

    if request.method =='POST':
        form= RecipeCreatForm(request.POST,request.FILES)

        if form.is_valid():
            form_obj = form.save(commit=False)

            form_obj.created_by = request.user

            form_obj.save()

            return redirect(reverse('home'))


    context ={
        'form':form
    }
    return render(request,'add_recipe.html',context)


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "detail.html"
    context_object_name = 'recipe'



class RecipeUpdateView(UpdateView):
    model = Recipe
    template_name = "update.html"
    success_url = '/'
    fields = ['name','detail']


class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = "delete.html"
    success_url = '/'


