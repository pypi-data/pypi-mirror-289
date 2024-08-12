import os

def get_env_variable(var_name, default=None):
    """
    Get the value of an environment variable.
    
    Args:
        var_name (str): Name of the environment variable.
        default: Default value if the environment variable is not set.
    
    Returns:
        The value of the environment variable or the default value.
    """
    return os.environ.get(var_name, default)