#!/usr/bin/env python3


def validate_user(username, minlen):
  """Checks if the received username matches the required conditions."""
  if type(username) != str:
    raise TypeError("username must be a string")
  if minlen < 1:
    raise ValueError("minlen must be at least 1")
    
  if len(username) < minlen:
      return False
  if not username.isalnum():
      return False
  # Usernames can't begin with a number
  if username[0].isnumeric():
      return False
    
  for i in username[1:]:
      if i.isdigit():
          p1 = True
      if i.isalpha():
          p2 = True
  if not p1 and p2:
      return False
  return True
