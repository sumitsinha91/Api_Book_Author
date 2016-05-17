from django.apps import AppConfig


class BookConfig(AppConfig):
    name = 'book'


class UserConfig(AppConfig):
	name = 'user'


	def ready(self):
		import user.singnals
