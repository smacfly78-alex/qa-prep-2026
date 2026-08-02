from functools import wraps

current_user = None

def authorize(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if current_user is None:
            raise PermissionError("User not authorized")
        return func(*args, **kwargs)
    return wrapper

@authorize
def secret_action() -> str:
    return "Secret data!"


# Попытка без логина
try:
    secret_action()
except PermissionError as e:
    print(f"Denied: {e}")
# Denied: User not authorized

# После логина
current_user = {"name": "Igor", "role": "admin"}
result = secret_action()
print(result)
# Secret data!