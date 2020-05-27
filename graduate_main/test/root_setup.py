import sys
import os.path
root_directory=os.path.abspath(os.path.join(os.path.abspath(__file__),"../../../"))
print(root_directory)
sys.path.append(root_directory)