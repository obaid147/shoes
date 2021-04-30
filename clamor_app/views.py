from django.shortcuts import render


def ind(req):
    return render(req, 'clamor_app/index.html')
