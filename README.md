# validations

This module is used for check the valid name.
Turn "username, minlen" into "True" or "False"

# Examples

calling 'validate_user("Mohammad", 5)' will return 'True'
calling 'validate_user("Mohammad", 9)' will return 'False'
calling 'validate_user("Mohammad", 0)' will return 'False'
calling 'validate_user(1234, 4)' will return "username must be a string"
calling 'validate_user("Mohammad", 0)' will return "minlen must be at least 1"
