from django.shortcuts import render, redirect
from django.http import Http404
from .models import *
from .rules import *


def home(request):
    if request.GET.get("drawer") == "true":
        return folder_list(request, '/')
    ctx={}
    return render(request, 'home.html',ctx)


def editor(request, path, name, ext):
    archive = get_file(path, name, ext)
    print('sdifosifhsdi', ext)
    ctx = {
        'archive': archive,
        'perm': not can_edit_page(request.user, archive),
        'ext': LANGUAGE_MAP.get(ext, 'text'),
    }
    return render(request, 'micropad/editor.html', ctx)


def folder_list(request, path):
    ctx = {
        'folder': get_folder(path),
        'path': path,
    }
    return render(request, 'micropad/folder-list.html', ctx)


def lock(request, path, name, ext):
    mfile = File.objects.get(name=name)
    if is_page_owner(request.user, mfile):
        mfile = _set_page_lock(mfile, True)
        mfile.save()
        return redirect('/' + mfile.url)
    return Http404    


def unlock(request, path, name, ext):
    mfile = File.objects.get(name=name)
    if is_page_owner(request.user, mfile):
        mfile = _set_page_lock(mfile, False)
        mfile.owner_name = None
        mfile.save()
        return redirect('/' + mfile.url)
    return Http404


def _set_page_lock(mfile, boolean):
    mfile.lock = boolean
    return mfile
    

def get_file(path, name, ext):
    url = path + name + ext

    try:
        return File.objects.get(url=url)
    except File.DoesNotExist:
        pass

    parent = get_folder(path)
    archive, _ = File.objects.get_or_create(
        text="", 
        name=name, 
        url=url, 
        folder=parent,
        ext=ext,
    )
    return archive


def get_folder(path):
    folder, _ = Folder.objects.get_or_create(name='/') 
    for subpath in path.strip('/').split('/'):
        folder, _ = Folder.objects.get_or_create(name=subpath, parent=folder)
    return folder


LANGUAGE_MAP = {
    ".txt": "plaintext", 
    ".ts": "type", 
    ".js": "java", 
    ".json": "json", 
    ".bat": "bat", 
    ".cs": "coffee", 
    ".c": "c", 
    ".cpp": "cpp", 
    ".cs": "csharp", 
    ".csp": "csp", 
    ".css": "css", 
    ".fs": "fsharp", 
    ".go": "go", 
    ".handlebars": "handlebars", 
    ".html": "html", 
    ".htm": "html", 
    ".ini": "ini", 
    ".java": "java", 
    ".less": "less", 
    ".lua": "lua", 
    ".md": "markdown", 
    ".msdax": "msdax", 
    ".mysql": "mysql", 
    ".objc": "objective-c", 
    ".pgsql": "pgsql", 
    ".php": "php", 
    ".postiats": "postiats", 
    ".powershell": "powershell", 
    ".pug": "pug", 
    ".py": "python", 
    ".r": "r", 
    ".razor": "razor", 
    ".redis": "redis", 
    ".redshift": "redshift", 
    ".ruby": "ruby", 
    ".rs": "rust", 
    ".sb": "sb", 
    ".scss": "scss", 
    ".sol": "sol", 
    ".sql": "sql", 
    ".st": "st", 
    ".swift": "swift", 
    ".vb": "vb", 
    ".xml": "xml", 
    ".yaml": "yaml",
    ".yml": "yaml",
}