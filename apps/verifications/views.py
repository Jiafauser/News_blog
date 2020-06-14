from django.shortcuts import render
from utils.captcha.captcha import captcha
from django.http import HttpResponse
# Create your views here.
from django.views import View


class ImageCode(View):
    def get(self, request, image_code_id):
        text, image = captcha.generate_captcha()
        return HttpResponse(content=image, content_type='image/jpg')
