bp1="""3
   *
  ***
******"""

def house(blueprint):
    bp = blueprint.splitlines()
    lines = int(bp.pop(0))
    walling=False
    for i in xrange(lines-1, -1, -1):
        for char in bp[i]:
            if char=="*":
                if walling:
                    pass
                else:
                    walling = True
            else:
                pass
