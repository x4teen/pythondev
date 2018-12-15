print(""" False : {0}
None: {1}
0.0 : {2}
5.0 : {3}
empty list [] : {4}
non-empty list [4,5] : {5}
string 'aa': {6}
empty string "": {7}
empty mapping {{}} : {8}
""".format(False, bool(None), bool(0.0), bool(5.0),
           bool([]), bool([4, 5]), bool('aa'), bool(""), bool({})))
