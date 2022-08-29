import base64
from django.shortcuts import render
from django.conf import settings
# Create your views here.
from django.views.generic import FormView

from main.forms import IndexForm


class Index(FormView):
    template_name = 'main/index.html'
    form_class = IndexForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            image = request.FILES['uploaded_image']
            prediction_image = settings.MODEL.predict(image.temporary_file_path(), format='image')
            prediction_json = settings.MODEL.predict(image.temporary_file_path(), format='json')

            return render(request, self.template_name,
                          {'form': form, 'image': base64.b64encode(prediction_image).decode('utf-8'),
                           'json': prediction_json.json()})
        return super(Index, self).post(request, *args, **kwargs)
