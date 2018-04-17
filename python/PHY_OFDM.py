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
import math
import binascii
from gnuradio import gr
from itertools import chain
import imp
from MAC_OFDM import MAC_OFDM

OFDM_Variables = imp.load_source('PHY_Vars', '/home/leri/Escritorio/tfg/AccesoMedio/gr-OFDM/python/OFDM_Variables.py')
PHY_Class = OFDM_Variables.PHY_Vars
MAC_Class = OFDM_Variables.MAC_Vars

class PHY_OFDM(gr.basic_block):
    """
    Physical layer for the OFDM block. Packages the MAC layer frame and adds control headers. Lastly, proceeds to make the OFDM modulation.
    Return a stream of PHY frames.
    """
    def __init__(self, Nport, Occupied_Carriers, Pilot_Carriers):
        gr.basic_block.__init__(self,
            name="PHY_OFDM",
            in_sig=[numpy.uint8],
            out_sig=[numpy.complex64])

        # Variables del bloque
        self.d_Nport = Nport
        self.d_Occupied_Carriers = Occupied_Carriers
        self.d_Pilot_Carriers = Pilot_Carriers
        self.d_CP_Len = 16
        # Importamos las variables del fichero: MAC LAYER
        self.MAC_FRAME_SIZE = 0
        self.MAC_CONTROL_SIZE = MAC_Class.MAC_CONTROL_SIZE
        # Importamos las variables del fichero: PHY LAYER
        self.d_PHY_PREAMBLE = self.Parse_Preamble(PHY_Class.PHY_PREAMBLE)
        self.d_PHY_FRAME_SIZE = 0

        # Impedimos que las etiquetas entrantes vuelvan a salir
        self.set_tag_propagation_policy(1)


    """
    Realiza la IFFT + Prefijo Cíclico de N puntos de la señal compleja entrante
    """
    def OFDM (self, complex_signal):
        phy_signal = numpy.fft.ifft(complex_signal, self.d_Nport)
        CP = phy_signal[-self.d_CP_Len:]
        CP[:] = 0.3
        OFDM_symbol = numpy.complex64(numpy.append(CP, phy_signal))
        return OFDM_symbol
    """
    Toma una señal de NPortadoras muestras y la rellena completando el símbolo OFDM
    Si el usuario tiene 0-30 portadoras, devuelve 0-30 (info) y 31-64 ceros.
    """
    def Fill_OFDM_Symbol (self, symbol):
        Used_Carriers = len(self.d_Occupied_Carriers)
        First_Carrier = self.d_Occupied_Carriers[0]
        Last_Carrier = self.d_Occupied_Carriers[-1]
        if len(symbol) < Used_Carriers:
            symbol = numpy.append(symbol, (Used_Carriers-len(symbol))*[0])
        full_symbol = numpy.insert(symbol, 0, First_Carrier*[0])
        full_symbol = numpy.insert(full_symbol, Used_Carriers, (self.d_Nport -Used_Carriers - First_Carrier)*[0])
        full_symbol = numpy.complex64(full_symbol)
        return full_symbol


    """
    Convierte el preámbulo en un símbolo OFDM de longitud 64 + CP muestras.
    """
    def Parse_Preamble(self, preamble):
        complex_preamble = numpy.array([])
        for index, element in enumerate(preamble):
            auxiliar_signal = numpy.complex64(element[0]+1j*element[1])
            complex_preamble = numpy.append(complex_preamble, auxiliar_signal)
        full_complex_preamble = self.Fill_OFDM_Symbol(complex_preamble)
        modulated_OFDM_Preamble = self.OFDM(full_complex_preamble)
        return modulated_OFDM_Preamble


    def decimal_to_binary (self, number):
        binary = "{0:0b}".format(number)  # string de 8 bits con el número codificado
        binary = binary.zfill(16)
        binary = list(binary)              # Convertimos en lista
        binary = numpy.uint8(binary)       # Pasamos a numpy.uint8
        return binary



    def forecast(self, noutput_items, ninput_items_required):
        #setup size of input_items[i] for work call
        for i in range(len(ninput_items_required)):
            ninput_items_required[i] = noutput_items

    def parse_tags(self, unparsed_tags):
        for index in range(0, len(unparsed_tags)):
            new_offset = unparsed_tags[index].offset - self.nitems_read(0)
            if new_offset < 0:
                Error_Flag = True
                return (None)
            else:
                unparsed_tags[index].offset = new_offset
        return unparsed_tags

    def extract_MAC_frame (self, source, start, MAC_FRAME_SIZE):
        end = start + MAC_FRAME_SIZE
        return source [start:end]

    def create_PHY_frame(self, mod_frame):
        self.d_PHY_PREAMBLE[:] = 2+2j
        PHY_frame = numpy.concatenate(
            (
            self.d_PHY_PREAMBLE,
            mod_frame,
            )
        )
        PHY_frame = numpy.complex64(PHY_frame)
        return PHY_frame
    """
    BPSK MOD
    """
    def Modulate(self, signal):
        signal = numpy.int8(signal)
        mod_signal = signal * 2 - 1
        mod_signal = numpy.complex64(mod_signal)
        return mod_signal

    def OFDM_Modulation (self, signal):
        i = 0
        Used_Carriers = len(self.d_Occupied_Carriers)
        exit_signal = numpy.array([])
        while i < len(signal) -1 :
            current_symbol = signal[i:i+Used_Carriers]
            filled_symbol = self.Fill_OFDM_Symbol(current_symbol)
            OFDM_Symbol = self.OFDM(filled_symbol)
            i += Used_Carriers
            exit_signal = numpy.append(exit_signal, OFDM_Symbol)
        exit_signal = numpy.complex64(exit_signal)
        return exit_signal



    def Compute_PHY_Frame_Size(self, MAC_SIZE):
        self.d_PHY_FRAME_SIZE = (self.MAC_FRAME_SIZE / len(self.d_Occupied_Carriers) + 1)*(self.d_Nport+self.d_CP_Len) + (self.d_Nport+self.d_CP_Len)

    def Change_MAC_Frame_Size(self, MAC_SIZE):
        self.MAC_FRAME_SIZE = MAC_SIZE


    def general_work(self, input_items, output_items):
        input = input_items[0]
        output = output_items[0]
        in_i = 0
        out_i = 0
        tags = self.get_tags_in_window(0,
                0,
                len(input),
                pmt.intern("MAC Start")
        )
        #Quitamos el offset a las etiquetas, para saber dónde esta cada una
        tags = self.parse_tags(tags)
        # Si tags = None, significa que algún offset era negativo, así que algún error habrá. Salimos de la función
        if tags == None:
            print "PHY:   Tag Error: Negative Offset in tag"
            self.consume(0, len(input))
            return len(output)
        for index, tag in enumerate(tags):
            # Cambiamos el tamaño del paquete MAC, recogiendo de la etiqueta el valor
            self.Change_MAC_Frame_Size(int(pmt.to_double(tag.value)))
            # Recalculamos el tamaño de la trama física
            self.Compute_PHY_Frame_Size(self.MAC_FRAME_SIZE)
            if tag.offset + self.MAC_FRAME_SIZE > len(input):
                print "PHY Error: Not enough samples to extract a full frame.  "
                break
            MAC_frame = self.extract_MAC_frame(input, in_i, self.MAC_FRAME_SIZE)
            if len(MAC_frame) != self.MAC_FRAME_SIZE:
                print "PHY: Wrong MAC frame length"
                continue
            # De momento modulamos todas las portadoras en BPSK
            BPSK_signal = self.Modulate(MAC_frame)
            # Modulación OFDM
            OFDM_signal = self.OFDM_Modulation(BPSK_signal)
            # Creamos la trama física: añadimos las cabeceras PHY
            PHY_FRAME = self.create_PHY_frame(OFDM_signal)
            try:
                end_i = out_i + self.d_PHY_FRAME_SIZE
                output[out_i:end_i] = PHY_FRAME
                out_i = end_i
                #self.MAC_SEQ_NUMBER += 1
            except ValueError, error:
                #output = numpy.append(output, frame_crc)
                out_i = len(output)
                #self.MAC_SEQ_NUMBER += 1
                break
        self.consume(0, len(input))
        return out_i
