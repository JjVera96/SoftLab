from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
	use_in_migrations = True

	def _create_user(self, identification, password, **extra_fields):
		"""
		Creates and saves a User with the given identification and password.
		"""
		if not identification:
			raise ValueError('The given identification must be set')
		user = self.model(identification=identification, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, identification, password=None, **extra_fields):
		extra_fields.setdefault('is_superuser', False)
		extra_fields.setdefault('is_active', False)
		extra_fields.setdefault('is_staff', False)
		return self._create_user(identification, password, **extra_fields)

	def create_superuser(self, identification, password, **extra_fields):
		extra_fields.setdefault('is_active', True)
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)

		return self._create_user(identification, password, **extra_fields)
