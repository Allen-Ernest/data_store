from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from documents.models import Document


@login_required
def get_add_document_form(request):
    return render(request, "add_documents.html")

@login_required
def add_document(request):
    if request.method == 'POST':
        name = request.POST['name']
        owner = request.user
        date = request.POST['date']
        file = request.FILES['document']
        if name is None or name == "" or owner is None or date is None or date == "" or file is None or file == "":
            context = {"Success": False}
            return render(request, "add_documents.html")
        doc = Document.objects.create(
            name = name,
            owner = owner,
            date = date,
            file = file,
            size = file.size
        )
        context = {"Success": True}
        return render(request, 'add_documents.html', context)

    context = {"Success": False}
    return render(request, 'add_documents.html')
