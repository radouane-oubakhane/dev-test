from django.shortcuts import render
from .forms import UploadFileForm
from .utils import handle_uploaded_file, send_summary_email



def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                summary = handle_uploaded_file(request.FILES['file'])
                send_summary_email(summary)
            except ValueError as e:
                return render(request, 'fileupload/error.html', {'error': str(e)})
            return render(request, 'fileupload/summary.html', {'summary': summary.to_dict(orient='records')})
    else:
        form = UploadFileForm()
    return render(request, 'fileupload/upload.html', {'form': form})

