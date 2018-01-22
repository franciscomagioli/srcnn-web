from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from uploads.core.models import Document, SrcnnImage, BicubicImage
from uploads.core.forms import DocumentForm
from django.urls import reverse


def home(request):
    documents = Document.objects.all()
    return render(request, 'core/home.html', { 'documents': documents })

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })

def detail(request, document_id):
    #doc = Document.objects.get(pk=document_id)
    #srcnn = SrcnnImage.objects.get(original=document_id)
    #bicubic = BicubicImage.objects.get(original=document_id)
    doc = get_object_or_404(Document, pk=document_id)
    srcnn = get_object_or_404(SrcnnImage, original=document_id)
    bicubic = get_object_or_404(BicubicImage, original=document_id) 
    return render(request, 'core/detail.html', { 'doc': doc, 'srcnn':srcnn, 'bicubic':bicubic})