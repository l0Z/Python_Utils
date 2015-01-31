#!/bin/python
import logging;
import sys;

instance = logging.getLogger("ColumnSubsetSelectionLogger");
instance.setLevel(logging.INFO);
handler  = logging.StreamHandler(sys.stderr);
handler.setLevel(logging.INFO);
instance.addHandler(handler);

def initlog(opts):
    global instance;
    global handler;
    instance.removeHandler(handler);
    instance = logging.getLogger("ColumnSubsetSelectionLogger");
    handler  = None;

    if "log" in opts:
        handler = logging.FileHandler(opts["log"]);
    else:
        handler = logging.StreamHandler(sys.stderr);

    if "level" in opts:
        if   "debug" == opts["level"].lowcase():
            instance.setLevel(logging.DEBUG);
        elif "info"  == opts["level"].lowcase():
            instance.setLevel(logging.INFO);
        else:
            instance.setLevel(logging.INFO);
    
    instance.addHandler(handler);
   
