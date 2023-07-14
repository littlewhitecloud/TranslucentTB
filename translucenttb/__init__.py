from platform import system

if system() != "Windows":
	raise OSError("Platform not Windows!")


from .main import Settings, blur  # noqa: F401
