from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseForbidden
from .forms import CreatePollForm
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import Poll

def home(request):
    polls=Poll.objects.all()
    context={'polls':polls}
    return render(request,'poll/home.html',context)

# def create(request):
#     if request.method=='POST':
#         form=CreatePollForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form=CreatePollForm()
#     context={'form':form}
#     return render(request,'poll/create.html',context)



@login_required
def create(request):
    if request.method=='POST':
        form=CreatePollForm(request.POST)
        if form.is_valid():
            poll = form.save(commit=False) # don't save the form yet
            poll.user = request.user # set the user_id field to the current user's ID
            poll.save() # now save the poll object to the database
            return redirect('home')
    else:
        form=CreatePollForm()
    context={'form':form}
    return render(request,'poll/create.html',context)



    
def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    if request.method == "POST":
        selected_option = request.POST.get('poll', None)
        if selected_option == 'option1':
            poll.op1c += 1
            poll.save()
        elif selected_option == 'option2':
            poll.op2c += 1
            poll.save()
        elif selected_option == 'option3':
            poll.op3c += 1
            poll.save()
        else:
            return HttpResponse(400, 'Invalid form')
        return redirect('results', poll.id)
    context = {
        'poll': poll,
    }
    return render(request, 'poll/vote.html', context)


def results(request,poll_id):
    poll=Poll.objects.get(pk=poll_id)
    context={'poll':poll}
    return render(request,'poll/results.html',context)


@require_POST
def delete_poll(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    if request.method == 'POST':
        poll.delete()
        return redirect('home')
    return render(request, 'poll/confirm_delete.html', {'poll': poll})

def confirm_delete_poll(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'confirm_delete.html', {'poll': poll})

