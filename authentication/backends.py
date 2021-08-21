from django.db.models import Q
from .models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend


class EmailOrCnicAuthBackend(BaseBackend):

    def authenticate(self, request, email=None, password=None, **kwargs):
        my_user_model = get_user_model()
        try:
            user = my_user_model.objects.get(
                Q(email=email) | Q(cnic=email))
            if user.check_password(password):
                return user
        except my_user_model.DoesNotExist:
            return None
        except:
            return None

    def get_user(self, user_id):
        my_user_model = get_user_model()
        try:
            return my_user_model.objects.get(pk=user_id)
        except my_user_model.DoesNotExist:
            return None
