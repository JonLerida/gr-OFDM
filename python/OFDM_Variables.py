#!/usr/bin/env python
# -*- coding: utf-8 -*-


import numpy
import math

class MAC_Vars ():
    PREAMBLE   = numpy.uint8([1, 0, 1, 0, 1, 0, 1, 0] * 4)
    SFD        = numpy.uint8([1, 0, 1, 0, 1, 0, 1, 1])
    SRC_MAC_SIZE = 6 * 8
    DST_MAC_SIZE = 6 * 8
    CRC_SIZE   = 32
    MAC_SEQ_NUMBER_SIZE = 16
    #  [PREAMBLE] [SFD] [SRC MAC] [DST MAC][INFO] [PACKET NUMBER] [CRC]
    MAC_CONTROL_SIZE = len(PREAMBLE) + len(SFD) + SRC_MAC_SIZE + DST_MAC_SIZE + CRC_SIZE + MAC_SEQ_NUMBER_SIZE

class PHY_Vars():
    a1 = math.sqrt(2)
    a2 = math.sqrt(5)
    # len = 30
    # (x, y) --> x+j*y
    PHY_PREAMBLE = [
    (a1, a2),
    (a1, -a2),
    (-a1, a2),
    (-a1, -a2),
    (0, 0), (0, 0),
    (0, 0), (0, 0),
    (0, 0), (0, 0),
    (a2, a1),
    (a2, -a1),
    (-a2, a1),
    (-a2, -a1),
    (0, 0), (0, 0),
    (0, 0), (0, 0),
    (0, 0), (0, 0),
    (0, 0), (0, 0),
    (a2, a1),
    (a2, -a1),
    (a1, a2),
    (a1, a2),
    (a1, a2),
    (a1, a2),
    (0, 0), (0, 0),
    ]
    """ IFFT DEL PREAMBULO CAPA FISICA (64 puntos), multiplicada por 10
    [1.58265471+1.39754251j, -1.73951647-0.10946504j,  1.67556712-1.02391921j,
    -0.18382494+1.70171498j -0.75570760-1.25904937j  1.11721100-0.35170198j
    0.48262846-0.49988749j  1.82277298+0.13076717j  0.49585905+1.19360333j
    0.25692123+0.53608035j -0.55509608+0.33989766j  0.61876168-1.49719573j
    2.25725882+0.60526255j  0.44921151+1.11283926j  1.00217007+0.87666857j
    -0.56231298+1.65124484j -0.82718601-0.82718601j  1.37620182-0.55988072j
    1.02838866+0.68200864j  0.76798007+0.52863361j  0.85884598+1.00356546j
    -0.24741606+1.19762984j -0.38336284-0.50777771j  1.50911444-0.24918771j
    0.77429567+0.88110333j  1.27911803+0.02261127j  1.69495073+2.0748966j
    -0.75729728+1.66970186j  0.32099505+0.08485573j  0.61858409+1.12062934j
    0.45691949+0.53215537j  1.45357408+1.4790517j   0.00000000+2.7233677j
    -1.36123011+1.57583646j -0.74906946+0.47145923j -0.26837573+0.84066729j
    -0.41556244+0.70782065j -0.00763047+1.32941762j -1.74531629+1.658247j
    -1.77620381-0.55324407j -0.31074684-0.23800255j -0.70058424-0.09147638j
    -0.11252170+0.04593105j -1.21148104+0.41797286j -1.08598878-1.3040338j
    0.31103718-1.16493449j  0.69977208-0.70651547j  0.86820215+0.27261251j
    -0.38524428+0.38524428j -0.35620176-0.82507334j  0.68975145-1.22910138j
    1.83430074-0.34204707j  1.19630752+0.94520577j  0.68201740+0.93682703j
    -0.48082015+1.26763238j -0.59037383-1.17341313j  2.20590155+0.07449744j
    -0.21336514+1.52002883j  0.89088122-0.33385449j  0.24127983+2.70206077j
    -2.37614855-0.78362698j  2.07117582-0.65919801j -1.05930890+1.94232929j
    -0.23058253-1.98916984j]"""
    Orden_Modulacion = 1
