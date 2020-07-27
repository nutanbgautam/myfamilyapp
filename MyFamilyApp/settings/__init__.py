try :
    from .local import *
except:
    from .production import *

#Temporary Settings
try:
    from .temporary import *
except:pass
