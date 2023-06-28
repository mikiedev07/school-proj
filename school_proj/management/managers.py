from django.contrib.auth.models import BaseUserManager


class TeacherManager(BaseUserManager):
    def create_user(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        if not phone:
            raise ValueError('The Phone field must be set')

        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not phone:
            raise ValueError('The Phone field must be set')

        user = self.create_user(phone, password, **extra_fields)
        return user
