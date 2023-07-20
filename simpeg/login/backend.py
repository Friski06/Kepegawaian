from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from login.models import User

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        # user = None
        try:
            # user = UserModel.objects.get(Q(username_iexact=username) | Q(email_iexact=username))
            user = User.objects.get(email=username)
        
        except UserModel.DoesNotExist:
            # UserModel().set_password(password)
           
            return None
        # except UserModel.MultipleObjectsReturned:
        #     user = UserModel.objects.filter(Q(username_iexact=username) | Q(email_iexact=username)).order_by('id').first()

        if user.check_password(password) and self.user_can_authenticate(user):
          return user