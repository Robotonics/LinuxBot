#!/usr/bin/env python

#!/usr/bin/env python

import os
import sys
from ping import *
import ping
from numpy import *

if not os.getegid() == 0:
    sys.exit('Script must be run as root')


__author__ = "David Cotterill-Drew"
__copyright__ = "Copyright 2014, RoboTonics"
__credits__ = ["David Cotterill-Drew"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = __author__
__email__ = "roboshopz@gmail.com"



a=array([1,3,4])
insert(a,[1],50)
print a



