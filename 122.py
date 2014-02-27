# -*- coding: utf-8 -*-

__title__ = ""

def solve():

    limit = 201
    paths = [[] for i in range(limit)]

    paths[1] = [[1]]
    paths[2] = [[1,2]]

    # Generate all paths
    s = 1
    from common import log
    for i in range(2, limit):
        for path in paths[i]:
            for step in path:
                k = step + i
                if k < limit:
                    new_path = path + [k]
                    if len(paths[k]) == 0:
                        paths[k].append(new_path)
                    else:
                        if len(new_path) < len(paths[k][0]):
                            paths[k]= [new_path]
                        elif len(new_path) == len(paths[k][0]):
                            paths[k].append(new_path)
        pathstr = map(str, paths[i][0])
        pathstr = ",".join(pathstr)
        log("%3d - %2d - %s " % (i, len(paths[i][0])-1, pathstr))
        s = s + len(paths[i][0])-1
    return s


