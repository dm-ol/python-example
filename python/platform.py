# Access to underlying platform’s identifying data
import platform
from platform import processor, system, architecture, machine, python_compiler

print('Platform processor:', platform.processor())
print('Operating system:', platform.system())
platform.architecture()
platform.machine()
platform.python_compiler()
