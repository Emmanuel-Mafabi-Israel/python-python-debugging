# GLORY BE TO GOD,
# PYTHON DEBUGGING,
# BY ISRAEL MAFABI EMMANUEL

# import pdb
import ipdb

# def add(l_oper:int, r_oper:int) -> int:
#     pdb.set_trace() # start debug watch...
#     return l_oper + r_oper

# add(98, 2)

def tracing() -> None:
    in_function:str = " debugger: currently inside the function."
    stop_msg:str = " debugger[notify]: stopping because of ipdb!"

    print(in_function)
    print(stop_msg)

    ipdb.set_trace() # start debugging
    
    buffer_var:str = " -> Program froze before it could read me! - [buffer_var]"
    print(buffer_var)

tracing()