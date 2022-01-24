from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.urls import reverse
from django.shortcuts import redirect

def right_role(roles=[]):
    def decorator(view_func):
        def wrap(request,*args, **kwargs):
            if request.user.profile.userStatus in roles:
                return view_func(request,*args,**kwargs)
            else:
                return redirect(request,"posts/error403.html")
            return wrap
        return decorator