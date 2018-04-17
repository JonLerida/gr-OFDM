#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/leri/Escritorio/tfg/AccesoMedio/gr-OFDM/python
export PATH=/home/leri/Escritorio/tfg/AccesoMedio/gr-OFDM/build/python:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH
export PYTHONPATH=/home/leri/Escritorio/tfg/AccesoMedio/gr-OFDM/build/swig:$PYTHONPATH
/usr/bin/python2 /home/leri/Escritorio/tfg/AccesoMedio/gr-OFDM/python/qa_MAC_OFDM.py 
