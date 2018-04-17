#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Tx And Rx
# Generated: Tue Apr 17 21:07:12 2018
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from ofdm_phy_rx_hier import ofdm_phy_rx_hier  # grc-generated hier_block
from optparse import OptionParser
import OFDM
import sip
from gnuradio import qtgui


class Tx_and_Rx(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Tx And Rx")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Tx And Rx")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "Tx_and_Rx")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000
        self.Payload_Size = Payload_Size = 20

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_sink_x_0 = qtgui.sink_f(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_sink_x_0_win)

        self.qtgui_sink_x_0.enable_rf_freq(False)



        self.ofdm_phy_rx_hier_0 = ofdm_phy_rx_hier()
        self.blocks_vector_source_x_0_0 = blocks.vector_source_b((1, 0), True, 1, [])
        self.blocks_uchar_to_float_0 = blocks.uchar_to_float()
        self.blocks_throttle_1 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.OFDM_PHY_OFDM_0 = OFDM.PHY_OFDM(64, (range(0, 30)), (0, ))
        self.OFDM_MAC_OFDM_0 = OFDM.MAC_OFDM((0x01, 0x02, 0x03, 0x04, 0x05, 0x06), (0x01, 0x02, 0x03, 0x04, 0x06, 0x07), Payload_Size)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.OFDM_MAC_OFDM_0, 0), (self.OFDM_PHY_OFDM_0, 0))
        self.connect((self.OFDM_PHY_OFDM_0, 0), (self.ofdm_phy_rx_hier_0, 0))
        self.connect((self.blocks_throttle_1, 0), (self.OFDM_MAC_OFDM_0, 0))
        self.connect((self.blocks_uchar_to_float_0, 0), (self.qtgui_sink_x_0, 0))
        self.connect((self.blocks_vector_source_x_0_0, 0), (self.blocks_throttle_1, 0))
        self.connect((self.ofdm_phy_rx_hier_0, 0), (self.blocks_uchar_to_float_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Tx_and_Rx")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.blocks_throttle_1.set_sample_rate(self.samp_rate)

    def get_Payload_Size(self):
        return self.Payload_Size

    def set_Payload_Size(self, Payload_Size):
        self.Payload_Size = Payload_Size


def main(top_block_cls=Tx_and_Rx, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
