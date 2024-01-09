from django.shortcuts import render
from core.models import Profile, User
from django.contrib import messages
import instaloader


def getPostsFromInsta(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)

    insta = instaloader.Instaloader()

    if request.method == "POST":
        insta_username = request.POST['searching_value']
        # insta.download_profile(insta_username, profile_pic=False, download_stories=False, post_filter=lambda post: post.typename == 'GraphImage')

        cors_prefix = 'https://cors-anywhere.herokuapp.com/'

        try:
            insta_profile = instaloader.Profile.from_username(insta.context, insta_username)
            insta_profile_posts = insta_profile.get_posts()
            context = {
                'user_profile': user_profile,
                'insta_profile_posts': insta_profile_posts,
                'cors_prefix': cors_prefix,
            }

            return render(request, 'getpostsfrominsta.html', context)

        except instaloader.exceptions.ProfileNotExistsException:
            messages.info(request, "Profile does not exist on Instagram")
            return render(request, 'getpostsfrominsta.html', {'user_profile': user_profile})
        except instaloader.exceptions.ProfileHasNoPicsException:
            messages.info(request, "Profile does not have any post")
            return render(request, 'getpostsfrominsta.html', {'user_profile': user_profile})
        # TODO add exception for private accounts

    return render(request, 'getpostsfrominsta.html', {'user_profile': user_profile})
