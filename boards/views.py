from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import NewTopicForm, NewPostForm
from .models import Board, Post, Topic


# Create your views here.
def Home(request):
    boards = Board.objects.all()
    context = {'boards': boards}
    return render(request, 'boards/home.html', context)


def About(request):
    boards = Board.objects.all()
    context = {'boards': boards}
    return HttpResponse("About Page")


def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    context = {'board': board}
    return render(request, 'boards/board_topics.html', context)


def topic_posts(request, board_pk, topic_pk):
    topic = get_object_or_404(Topic, board__pk=board_pk, pk=topic_pk)
    topic.views +=1
    topic.save()
    context = {'topic': topic}
    return render(request, 'boards/topic_posts.html', context)


@login_required
def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.created_by = request.user
            topic.save()

            Post.objects.create(
                message=form.cleaned_data.get('message'),
                created_by=request.user,
                topic=topic
            )
            return redirect('boards:board_topics', pk=pk)
    else:
        form = NewTopicForm()
    context = {'board': board, 'form': form}
    return render(request, 'boards/new_topic.html', context)


@login_required
def new_post(request, board_pk, topic_pk):
    topic = get_object_or_404(Topic, board__pk=board_pk, pk=topic_pk)
    if request.method == "POST":
        form = NewPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()
            return redirect('boards:topic_posts', board_pk=board_pk, topic_pk=topic_pk)
    else:
        form = NewPostForm()
    context = {'form': form, 'topic': topic}
    return render(request, 'boards/new_post.html', context)









