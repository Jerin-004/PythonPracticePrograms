## modules = a file contaning python code. May contain function, classes, etc,
##           used with modular programming .Which is to separate a program into parts

from messages import hello,bye      ## name of the module

hello()
bye()

import messages as msg  ## this is called as an alias

msg.hello()
msg.bye()

help("modules")