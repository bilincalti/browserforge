"""
The undetected_patchright injector is a 1:1 copy of the patchright injector,
using the "undetected_patchright" import name for typing purposes.
"""

from .injector import AsyncNewContext, NewContext
from browserforge.injectors.utils import CheckIfInstalled

CheckIfInstalled('undetected_patchright')
