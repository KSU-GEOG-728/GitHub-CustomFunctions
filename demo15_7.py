# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: demo15_7.py
    Author: Shawn Hutchinson
    Description:  Modifying system paths for running custom modules
    Date created: December 1, 2025
    Python Version: 3.11.11
"""

# Import required module(s)
import sys

# Print current system paths
print(sys.path)

# Temporarily add a different system path to a script
sys.path.append("D:/Research/CustomModules")