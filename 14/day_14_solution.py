# IMPORT
# ----------------------------------------------------------------------------
import os
import sys
# get path to directory where this file is present
current = os.path.dirname(os.path.realpath(__file__))
# get path to parent directory where this directory is present
parent = os.path.dirname(current)
# add parent directory to sys.path
sys.path.append(parent)
# import the module
import functions as fn

# CLASSES
# ----------------------------------------------------------------------------

# FUNCTIONS
# ----------------------------------------------------------------------------

# EXECUTE
# ----------------------------------------------------------------------------

if __name__ == "__main__":
    pass