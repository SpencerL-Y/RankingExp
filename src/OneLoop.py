from z3 import *

L = [
lambda x :(True and (x[0] >= 0)),
lambda x :[(((x[0] + x[1]) - x[2]) - 1), x[1], x[2], ],
3,
0,
lambda x :[( ( ( x[0]+ x[1])- x[2])- 1), x[1], x[2], ],
lambda x :(And( True, ( x[0]>= 0))),
False,
]
