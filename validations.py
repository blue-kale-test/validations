#!/usr/bin/env python3


def validate_user(username, min_len):
  """Checks if the received username matches the required conditions."""
  if type(username) != str:
    raise TypeError("username must be a string")
  if min_len < 1:
    raise ValueError("min_len must be at least 1")
    
  if len(username) < min_len:
      return False
  if not username.isalnum():
      return False
  # Usernames can't begin with a number
  if username[0].isnumeric():
      return False
  return True
