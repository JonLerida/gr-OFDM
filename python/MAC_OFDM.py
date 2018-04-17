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
import pmt
import binascii
from gnuradio import gr
from itertools import chain
import imp

# This path should be changed in another PC implementation

OFDM_Variables = imp.load_source('MAC_Vars', '/home/leri/Escritorio/tfg/AccesoMedio/gr-OFDM/python/OFDM_Variables.py')
MAC_Class = OFDM_Variables.MAC_Vars


class MAC_OFDM(gr.basic_block):
    """
    Crea frames MAC a partir de una fuente binaria. Añade preámbulo MAC, CRC, direcciones origen y destino
    y el contador de paquete.
    Añade etiquetas GNU para el siguiente nivel
    """
    def __init__(self, SRC_MAC, DST_MAC, Payload_Size):
        gr.basic_block.__init__(self,
            name="MAC_OFDM",
            in_sig=[numpy.uint8],
            out_sig=[numpy.uint8])
        # Importamos las variables del fichero: MAC LAYER
        self.PREAMBLE = MAC_Class.PREAMBLE
        self.SFD = MAC_Class.SFD
        self.SRC_MAC_SIZE = MAC_Class.SRC_MAC_SIZE
        self.DST_MAC_SIZE = MAC_Class.DST_MAC_SIZE
        self.CRC_SIZE = MAC_Class.CRC_SIZE
        self.MAC_SEQ_NUMBER_SIZE = MAC_Class.MAC_SEQ_NUMBER_SIZE
        self.MAC_SEQ_NUMBER = 0
        # Variables del bloque
        self.d_SRC_MAC = self.process_MAC_Directions(SRC_MAC)
        self.d_DST_MAC = self.process_MAC_Directions(DST_MAC)
        self.d_INFO_SIZE = Payload_Size * 8
        # Tamaño del paquete MAC
        self.MAC_FRAME_SIZE = MAC_Class.MAC_CONTROL_SIZE + self.d_INFO_SIZE

    def set_Info_Size(self, Payload_Size):
        self.d_INFO_SIZE = Payload_Size * 8
        self.MAC_FRAME_SIZE = MAC_Class.MAC_CONTROL_SIZE + self.d_INFO_SIZE


    def decimal_to_binary (self, number, length):
        binary = "{0:0b}".format(number)  # string de 8 bits con el número codificado
        binary = binary.zfill(length)
        binary = list(binary)              # Convertimos en lista
        binary = numpy.uint8(binary)       # Pasamos a numpy.uint8
        return binary

    def process_MAC_Directions (self, MAC):
        parsed_mac = []
        if len(MAC) != self.SRC_MAC_SIZE / 8 :
            return None
        for dir in MAC:
            parsed_mac.append(self.decimal_to_binary(dir, 8))

        parsed_mac = numpy.uint8(parsed_mac)
        parsed_mac = list(chain(*parsed_mac))
        return parsed_mac




    def forecast(self, noutput_items, ninput_items_required):
        #setup size of input_items[i] for work call
        for i in range(len(ninput_items_required)):
            ninput_items_required[i] = noutput_items


    def create_frame (self, payload, seq_number):

        frame = numpy.concatenate(
        (
            self.PREAMBLE,
            self.SFD,
            self.d_SRC_MAC,
            self.d_DST_MAC,
            payload,
            seq_number,
        ))
        #frame = numpy.uint8(frame)
        return frame

    def add_crc(self, frame, offset):
        crc = binascii.crc32(frame) & 0xFFFFFFFF
        crc = "{0:0b}".format(crc)  # string de 16 bits con el número codificado
        crc = crc.zfill(32)
        crc = numpy.uint8(list(crc))
        # Debug option
        crc[:] = 2
        frame_crc = numpy.append(frame, crc)
        check = sum(frame_crc)
        self.add_item_tag(0, # Port number
            self.nitems_written(0) + offset, # Offset
            pmt.intern("MAC Start"), # Key
            pmt.from_double(self.MAC_FRAME_SIZE),
            #pmt.from_double() # Value
        )
        return frame_crc



    def general_work(self, input_items, output_items):
        """
        Recoge grupos de información y forma paquetes.
        info = X bytes
        """
        input = input_items[0]
        output = output_items[0]
        in_i = 0
        out_i = 0
        while in_i + self.d_INFO_SIZE <= len(input):
            info = input [in_i:in_i+self.d_INFO_SIZE]
            counter_binary = self.decimal_to_binary(self.MAC_SEQ_NUMBER, self.MAC_SEQ_NUMBER_SIZE)
            frame = self.create_frame(info, counter_binary)
            frame_crc = self.add_crc(frame, out_i)
            in_i += self.d_INFO_SIZE
            try:
                end_i = out_i + len(frame_crc)
                output[out_i:end_i] = frame_crc

                out_i = end_i
                #self.MAC_SEQ_NUMBER += 1
            except ValueError, error:
                #output = numpy.append(output, frame_crc)
                out_i = len(output)
                #self.MAC_SEQ_NUMBER += 1
                break
        self.consume(0, len(input))
        return out_i
