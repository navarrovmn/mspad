from django.shortcuts import render, redirect
from .models import *


def home(request):
    ctx={}
    return render(request, 'home.html',ctx)

def editor(request, path, name, ext):
    last_father = ""

    if path is not None:
        folders = path.split('/')
        print(folders)

        for idx, folder in enumerate(folders):
            try:
                get_folder = Folder.objects.get(name=folder)
            except Folder.DoesNotExist:
                if idx==0:
                    get_folder = Folder.objects.create(name=folder)
                else:
                    get_folder = Folder.objects.create(name=folder, folder=Folder.objects.get(name=last_father))

            last_father = folder

    try:
        archive = File.objects.get(name=name)
    except File.DoesNotExist:
        archive = File.objects.create(text="", name=name, url=path+name+ext, folder=Folder.objects.get(name=last_father))

    ctx = {
        'archive': archive
    }

    return render(request, 'micropad/editor.html', ctx)


def folder_list(request, path):
    ctx = {
        'path': path,
    }

    return render(request, 'micropad/folder-list.html', ctx)


def lock(request, path, name, ext):
    mfile = _set_page_lock(name, True)
    return redirect('/' + mfile.url)

def unlock(request, path, name, ext):
    mfile = _set_page_lock(name, False)
    return redirect('/' + mfile.url)

def _set_page_lock(page_name, boolean):
    mfile = File.objects.get(name=page_name)
    mfile.lock = boolean
    mfile.save()

    return mfile
    