"""
This module provides utility functions.

Author: Dilip Thakkar [dilip.thakkar.eng@gmail.com]
"""


def update_kw(kw: dict, **kwargs):
    """
    Updates a given dictionary `kw` with additional keyword arguments and removes specific keys.

    Args:
        kw (dict): The original dictionary to be updated.
        **kwargs: Additional keyword arguments to update the dictionary `kw`.

    Returns:
        dict: The updated dictionary with the specified keys removed.
    """
    r = kw.copy()
    r.update(**kwargs)
    delete_keys = ['key', 'on_change', 'args', 'kwargs']
    for k in delete_keys:
        if k in r.keys():
            del r[k]
    return r
