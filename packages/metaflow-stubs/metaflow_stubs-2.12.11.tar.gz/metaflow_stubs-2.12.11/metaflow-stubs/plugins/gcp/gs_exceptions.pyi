##################################################################################
#                       Auto-generated Metaflow stub file                        #
# MF version: 2.12.11                                                            #
# Generated on 2024-08-09T01:05:47.364893                                        #
##################################################################################

from __future__ import annotations

import typing
if typing.TYPE_CHECKING:
    import metaflow.exception

class MetaflowException(Exception, metaclass=type):
    def __init__(self, msg = "", lineno = None):
        ...
    def __str__(self):
        ...
    ...

class MetaflowGSPackageError(metaflow.exception.MetaflowException, metaclass=type):
    ...

