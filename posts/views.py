
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse , HttpResponseRedirect , Http404
from posts.models import Post
from django.contrib import messages

from comments.forms import  CommentForm

from django.contrib.contenttypes.models import ContentType

from comments.models import  Comment

from .forms import  PostForm


#function based views ..

def posts_create(request): # create

    # to validate that the post is done by only superuser
    if  not request.user.is_staff or  not request.user.is_superuser:
        raise Http404

    print("login page running ...")

    form = PostForm(request.POST or None , request.FILES or None)
    if form.is_valid():
        instance = form.save(commit = False)
        instance.save()
        print(form.cleaned_data.get("title"))
        print(form.cleaned_data.get("content"))
        # here display the success message ...
        #messages.success(request , "Post Sucessfully Created !!!")
        # now redirect the page after adding the new post ...
        return HttpResponseRedirect("/posts/list/")

    context={
        "form": form,
        "data" :"hello"
    }
    return render(request , "post_create.html" , context)

def posts_detail(request , id): # retreive

    print("requesting details:")
    #instance = Post.objects.get(id=5)
    instance = get_object_or_404(Post , id=id)



    initial_data = {
        "content_type" : ContentType.objects.get_for_model(Post),
        "object_id" : instance.id
    }
    comment_form = CommentForm(request.POST or None , initial = initial_data)
    if comment_form.is_valid():
        c_type = comment_form.cleaned_data.get("content_type")
        #print(c_type)
        content_type = ContentType.objects.get(model = c_type)
        #print(content_type)
        obj_id = comment_form.cleaned_data.get("object_id")
        content_data = comment_form.cleaned_data.get("content")

        # here save the comment that has been created ...
        new_comment , created = Comment.objects.get_or_create(
                            user = request.user,
                            content_type = content_type,
                            object_id = obj_id,
                            content = content_data
                        )

    

    content_type = ContentType.objects.get_for_model(Post)
    obj_id = instance.id

    comments = Comment.objects.filter(content_type = content_type , object_id = obj_id)
    context={
        "title" : instance.title,
        "instance" : instance,
        "comments" : comments,
        "comment_form" : comment_form,
    }
    return  render(request , "post_details.html" ,context)

def posts_list(request): # list posts

    print("requesting list:")
    querySet_list = Post.objects.all().order_by("-timestamp")
    paginator = Paginator(querySet_list, 10)
    page = request.GET.get('page')
    querySet = paginator.get_page(page)

    context = {
            "title": "List",
            "object_list" : querySet,
        }
    return  render(request , "post_list.html" ,context)

def posts_update(request , id): # update

    # to validate that the post is edit by only superuser
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    recordId = id
    print("requesting editing:")
    instance = get_object_or_404(Post , id =id)
    form = PostForm(request.POST or None , request.FILES or None , instance = instance );
    if form.is_valid():
        instance_level = form.save(commit = False)
        instance_level.save()
        # now redirecting after editing the post ...
        #messages.success(request, "Post Sucesfully Edited !!!")
        return  HttpResponseRedirect("/posts/"+recordId)
    context ={
            "form" : form,
        }

    return  render(request , "post_create.html" ,context)

def posts_delete(request , id): # delete

    # to validate that the post is delete by only superuser
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    print("requesting delete")
    instance = get_object_or_404(Post , id=id)
    instance.delete()
    #messages.success(request , "Succeffully Post Deleted !!!")
    return  HttpResponseRedirect("/posts/list/")





