from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.
from django.urls import reverse

from Accounts.models import Profile
from Chats.forms import GetTxt, SearchForm
from Chats.models import Text


@login_required(login_url='Account:login')
def add_friend(request, num):
    person = Profile.objects.get(pk=num)
    profile_id = request.user.profile.id
    profile = Profile.objects.get(pk=profile_id)
    profile.following.add(person)
    person.follower.add(profile)
    return HttpResponseRedirect(reverse('Chats:test'))


@login_required(login_url='Account:login')
def remove_friend(request, num):
    person = Profile.objects.get(pk=num)
    profile_id = request.user.profile.id
    profile = Profile.objects.get(pk=profile_id)
    profile.following.remove(person)
    person.follower.remove(profile)
    return HttpResponseRedirect(reverse('Chats:test'))


@login_required(login_url='Account:login')
def text_box_view(request, num):
    person = Profile.objects.get(pk=num)
    profile = request.user.profile
    if request.method == 'POST':
        form = GetTxt(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            Text.objects.create(from_user=profile, text=text, to=person)

    else:
        form = GetTxt()
    texts = Text.objects.filter(from_user__in=[person, profile], to__in=[person, profile]).order_by('-time')
    context = {
        'person': person,
        'profile': profile,
        'form': form,
        'texts': texts,
    }
    return render(request, 'Chats/chatw3.html', context)


def test_view(request):
    try:
        profile = request.user.profile
        my_id = request.user.profile.id
        data = profile.following.values_list('username_id', flat=True)
        friends = Profile.objects.filter(username_id__in=data)
        # people = Profile.objects.exclude(user=profile.user)
        users = Profile.objects.exclude(pk=my_id)
    except:
        profile = ''
        users = Profile.objects.all()
        friends = ''

    paginator = Paginator(users, 4)
    num_page = request.GET.get('page')
    try:
        paginator.page(num_page)
    except PageNotAnInteger:
        paginator.page(1)
    except EmptyPage:
        paginator.page(paginator.num_pages)
    find = SearchForm(request.GET)
    if find.is_valid():
        name_searched = find.cleaned_data['name']
        users = users.filter(username_id__contains=name_searched)
        min_age, max_age = find.get_age()
        if max_age is not None:
            users = users.filter(age__lte=max_age)
        if min_age is not None:
            users = users.filter(age__gte=min_age)

    context = {'profile': profile,
               'friends': friends,
               'users': users,
               'find': find,
               }
    return render(request, 'Chats/pro_test2.html', context)


@login_required(login_url='Account:login')
def friend_box(request):
    senders = []
    id_list = []
    profile = request.user.profile
    data = profile.following.values_list('username_id', flat=True)
    friends = Profile.objects.filter(username_id__in=data)
    texts = Text.objects.filter(Q(from_user=profile) | Q(to=profile)).order_by('-time')
    for i in texts:
        if i.from_user == profile:
            if i.to.username_id not in senders:
                senders.append(i.to.username_id)
                id_list.append(i.id)
        else:
            if i.from_user.username_id not in senders:
                senders.append(i.from_user.username_id)
                id_list.append(i.id)
    last_text = Text.objects.filter(id__in=id_list).order_by('time')
    context = {
        'profile': profile,
        'friends': friends,
        'texts': texts,
        'last': last_text
    }
    return render(request, 'Chats/box.html', context)
