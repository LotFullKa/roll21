from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, **kwargs):
        """
        Creates and saves a User with the given user name, its all
        """

        if not username:
            raise ValueError('The username does not set')

        user = self.model(username=username, **kwargs)
        user.save(using=self._db)
        return user

    def creat_user(self, username, **kwargs):
        kwargs.setdefault('is_superuser', False)
        return self._create_user(username, **kwargs)

    def creat_superuser(self, username, **kwargs):
        kwargs.setdefault('is_superuser', True)

        if kwargs.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, **kwargs)
