#!/usr/bin/env python3


def validate_user(username, minlen):
  """Checks if the received username matches the required conditions.
     Comprueba si el nombre de usuario recibido coincide con las condiciones requeridas"""
  if type(username) != str:
    raise TypeError("username must be a string")
  if minlen < 1:
    raise ValueError("minlen must be at least 1")
    
  if len(username) < minlen:
      return False
  if not username.isalnum():
      return False
  # Usernames can't begin with a number
  # Los nombres de usuario no pueden comenzar con un número
  if username[0].isnumeric():
      return False
  return True
