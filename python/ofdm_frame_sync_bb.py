#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2018 <+YOU OR YOUR COMPANY+>.
#
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#

import numpy
from gnuradio import gr
import pmt
import math

class ofdm_frame_sync_bb(gr.basic_block):
    """
    Primer bloque en recepción para el sistema OFDM(A). Se encarga de la sincronización a nivel físico.
    Etiqueta el inicio de las tramas OFDM y elimina los preámbulos de capa física.
    """


    def PHY_Frame_Sync(self, input_signal, offset):
        return 0

    def __init__(self):
        gr.basic_block.__init__(self,
            name="ofdm_frame_sync_bb",
            in_sig=[numpy.complex64],
            out_sig=[numpy.complex64])



    def forecast(self, noutput_items, ninput_items_required):
        #setup size of input_items[i] for work call
        for i in range(len(ninput_items_required)):
            ninput_items_required[i] = noutput_items

    def general_work(self, input_items, output_items):
        output = output_items[0]
        input = input_items[0]
        in_i = 0
        out_i = 0
        # Realizamos la sincronización para decidir dónde empieza la trama
        in_i = self.PHY_Frame_Sync(input, in_i)
        output[:] = 1+1j
        """
        Here starts signal processing
        """
        while in_i< len(input):
            in_i += 100

        self.consume(0, len(input_items[0]))
        return len(output)
