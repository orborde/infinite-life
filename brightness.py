#! /usr/bin/env python3

import collections

ON='ON'
OFF='OFF'
COMPOSITIONS = {
    ON : {
        ON : 10,
        OFF: 90,
        },
    OFF: {
        ON :  1,
        OFF: 99,
    },
}

def zoom(counts):
    new_counts = collections.defaultdict(int)
    for typ, ct in counts.items():
        for ntyp, nct in COMPOSITIONS[typ].items():
            new_counts[ntyp] += ct * nct
    return new_counts

def printfrac(counts):
    sm = sum(counts.values())
    print('{:7.3} {:7.3}'.format(counts[ON]/sm, counts[OFF]/sm))

def iterate(counts):
    for i in range(10):
        printfrac(counts)
        counts = zoom(counts)

print(ON)
oncts = collections.defaultdict(int)
oncts[ON] = 1
iterate(oncts)
print()

print(OFF)
offcts = collections.defaultdict(int)
offcts[OFF] = 1
iterate(offcts)
