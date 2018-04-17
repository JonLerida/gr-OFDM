#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Wed Apr 18 00:14:53 2018
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

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import OFDM
import sip
import sys
from gnuradio import qtgui


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
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

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 64e3
        self.Payload_Size = Payload_Size = 20

        ##################################################
        # Blocks
        ##################################################
        self.window = Qt.QTabWidget()
        self.window_widget_0 = Qt.QWidget()
        self.window_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.window_widget_0)
        self.window_grid_layout_0 = Qt.QGridLayout()
        self.window_layout_0.addLayout(self.window_grid_layout_0)
        self.window.addTab(self.window_widget_0, 'PHY')
        self.window_widget_1 = Qt.QWidget()
        self.window_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.window_widget_1)
        self.window_grid_layout_1 = Qt.QGridLayout()
        self.window_layout_1.addLayout(self.window_grid_layout_1)
        self.window.addTab(self.window_widget_1, 'MAC LAYER')
        self.top_layout.addWidget(self.window)
        self._Payload_Size_range = Range(1, 100, 5, 20, 200)
        self._Payload_Size_win = RangeWidget(self._Payload_Size_range, self.set_Payload_Size, 'INFO_SIZE', "counter_slider", int)
        self.top_layout.addWidget(self._Payload_Size_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	1024*4, #size
        	samp_rate, #samp_rate
        	'', #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-0.5, 2)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)

        if not True:
          self.qtgui_time_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.window_layout_1.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_sink_x_0 = qtgui.sink_c(
        	1024*2, #fftsize
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
        self.window_layout_0.addWidget(self._qtgui_sink_x_0_win)

        self.qtgui_sink_x_0.enable_rf_freq(False)



        self.blocks_vector_source_x_0_0 = blocks.vector_source_b((1, 0), True, 1, [])
        self.blocks_uchar_to_float_0 = blocks.uchar_to_float()
        self.blocks_throttle_1 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.OFDM_PHY_OFDM_0 = OFDM.PHY_OFDM(64, (range(0, 30)), (0, ))
        self.OFDM_MAC_OFDM_0 = OFDM.MAC_OFDM((0x01, 0x02, 0x03, 0x04, 0x05, 0x06), (0x01, 0x02, 0x03, 0x04, 0x06, 0x07), Payload_Size)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.OFDM_MAC_OFDM_0, 0), (self.OFDM_PHY_OFDM_0, 0))
        self.connect((self.OFDM_MAC_OFDM_0, 0), (self.blocks_uchar_to_float_0, 0))
        self.connect((self.OFDM_PHY_OFDM_0, 0), (self.qtgui_sink_x_0, 0))
        self.connect((self.blocks_throttle_1, 0), (self.OFDM_MAC_OFDM_0, 0))
        self.connect((self.blocks_uchar_to_float_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_vector_source_x_0_0, 0), (self.blocks_throttle_1, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.blocks_throttle_1.set_sample_rate(self.samp_rate)

    def get_Payload_Size(self):
        return self.Payload_Size

    def set_Payload_Size(self, Payload_Size):
        self.Payload_Size = Payload_Size
        self.OFDM_MAC_OFDM_0.set_Info_Size(self.Payload_Size)


def main(top_block_cls=top_block, options=None):

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
