from django.http import HttpResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from .forms import ContactForm
from django.shortcuts import render
# Create your views here.
# views.py
def generate_pdf_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            full_name = data['first_name'] + ' ' + data['last_name']
            data['name'] = full_name  
            html = render_to_string('pdf_template.html', {'data': data})
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="form_data.pdf"'
            pisa.CreatePDF(html, dest=response)
            return response
    else:
        form = ContactForm()
    return render(request, 'form.html', {'form': form})
