# For compatibility with Python2
from __future__ import print_function, division, absolute_import
#

import spekpy as sp
print("\n** Script to load a standard spectrum state from disk and print summary of metrics **\n")

# Load a standard spectrum state (from pre-existing library)
s = sp.Spek.load_state('NIST_NIST_L100')
# Summarize metrics
s.summarize(mode='full')
