from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from core.models import Post, Report
from django.contrib import messages


@login_required(login_url='login')
def ReportPost(request):
    username = request.user.username
    post_id = request.GET.get('post_id')

    post = Post.objects.get(id=post_id)

    is_reported = Report.objects.filter(post_id=post_id, username=username).first()

    if is_reported == None:
        new_report = Report.objects.create(post_id=post_id, username=username)
        new_report.save()
        post.is_reported = True
        post.no_of_reports += 1
        post.save()
        return redirect('home')
    else:
        # is_reported.delete() # report is undeletable for now.
        messages.info(request, 'Already reported')
        return redirect('home')
