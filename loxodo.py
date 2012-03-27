#!/usr/bin/env python

import sys
import os
import platform

# On Windows CE, use the "ppygui" frontend.
if platform.system() == "Windows" and platform.release() == "CE":
    from Loxodo.frontends.ppygui import loxodo
    sys.exit()

# If cmdline arguments were given, use the "cmdline" frontend.
if len(sys.argv) > 1:
    from Loxodo.frontends.cmdline import loxodo
    sys.exit()

# In all other cases, use the "wx" frontend.    
#try:
#    import wx
#except ImportError, e:
#    print >> sys.stderr, 'Could not find wxPython, the wxWidgets Python bindings: %s' % e
#    print >> sys.stderr, 'Falling back to cmdline frontend.'
#    print >> sys.stderr, ''
#    from Loxodo.frontends.cmdline import loxodo
#    sys.exit()
#
#from Loxodo.frontends.wx import loxodo
from Loxodo.frontends.qt import loxodo
