"""
!-- test file --!
"""

import os
from pathlib import Path

project_folder = os.path.dirname(__file__)
BASE_DIR = Path(__file__).resolve().parent
print(project_folder, '\n', BASE_DIR)
