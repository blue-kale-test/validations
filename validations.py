#!/usr/bin/env python3


def validate_user(username, minlen):
  """Checks if the received username matches the required conditions."""
  if type(username) != str:
    raise TypeError("username must be a string")
  # Username length should not be less than one.
  if minlen < 1:
    raise ValueError("minlen must be at least 1")
    
  # Username length can't be less than the minlen parameter provided to the funtion.
  if len(username) < minlen:
      return False
  if not username.isalnum():
      return False
  # Usernames can't begin with a number
  if username[0].isnumeric():
      return False
  return True

