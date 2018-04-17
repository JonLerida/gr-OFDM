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
import math
import pmt

class OFDM_PHY_IMPL_cb(gr.basic_block):
    """
    docstring for block OFDM_PHY_IMPL_cb
    """
    def __init__(self, Nport, Occupied_Carriers, Pilot_Carriers):
        gr.basic_block.__init__(self,
            name="OFDM_PHY_IMPL_cb",
            in_sig=[numpy.complex64],
            out_sig=[numpy.uint8])
        self.d_Nport = Nport
        self.d_Occupied_Carriers = Occupied_Carriers
        self.d_Pilot_Carriers = Pilot_Carriers
        self.d_CP_Len = 16
        # Impedimos que las etiquetas entrantes vuelvan a salir
        self.set_tag_propagation_policy(1)



    def parse_tags(self, unparsed_tags):
        for index in range(0, len(unparsed_tags)):
            new_offset = unparsed_tags[index].offset - self.nitems_read(0)
            if new_offset < 0:
                Error_Flag = True
                return (None)
            else:
                unparsed_tags[index].offset = new_offset
        return unparsed_tags

    def forecast(self, noutput_items, ninput_items_required):
        #setup size of input_items[i] for work call
        for i in range(len(ninput_items_required)):
            ninput_items_required[i] = noutput_items

    def general_work(self, input_items, output_items):
        output = output_items[0]
        input = input_items[0]
        output[:] = numpy.uint8(1)
        tags = self.get_tags_in_window(0,
            0,
            len(input),
            pmt.intern("PHY Frame Start")
        )
        tags = self.parse_tags(tags)
        self.consume(0, len(input))
        return len(output)
