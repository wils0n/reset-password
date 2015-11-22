from django.shortcuts import render

from django.contrib.auth.views import password_reset, password_reset_confirm
from django.contrib.auth.models import User

def confirm(request, uidb64=None, token=None):
    print request, "request ---->"
    print "entroooooo <----"
    try:
        return password_reset_confirm(request, template_name='custom/confirm.html',
        uidb64=uidb64, token=token)
    except Exception, e:
        print e, "<--- Error--"


def reset(request):
    email = request.POST.get('email', None)
    template_name='custom/custom_password_reset_form.html'
    if request.POST:
        if email is not None:
            exist = User.objects.filter(email__iexact=email)
            template_name='custom/custom_password_reset_form.html'
            if exist:
                return password_reset(request, template_name=template_name,
                          email_template_name='custom/reset_email.html')
            else:
                return render(request, template_name=template_name, context={'email':False})
    else:
        return password_reset(request, template_name=template_name,
                          email_template_name='custom/reset_email.html', extra_context={'email':True})