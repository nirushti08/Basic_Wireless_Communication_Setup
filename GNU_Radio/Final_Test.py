#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: gurrutchalla
# GNU Radio version: 3.10.1.1

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from gnuradio import blocks
import pmt
from gnuradio import channels
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from reciever_hier import reciever_hier  # grc-generated hier_block
from transmitter_hier import transmitter_hier  # grc-generated hier_block




class assembled7(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)

        ##################################################
        # Variables
        ##################################################
        self.taps = taps = [1.0, 0.25-0.25j, 0.50 + 0.10j, -0.3 + 0.2j]
        self.samp_rate = samp_rate = 32e3*3
        self.rf_rate = rf_rate = 1e6
        self.max_noise = max_noise = .584
        self.center_freq = center_freq = 3e9

        ##################################################
        # Blocks
        ##################################################
        self.transmitter_hier_0 = transmitter_hier()
        self.reciever_hier_0 = reciever_hier()
        self.channels_channel_model_0 = channels.channel_model(
            noise_voltage=.483,
            frequency_offset=1e-4,
            epsilon=1.00005,
            taps=taps,
            noise_seed=0,
            block_tags=False)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_tag_debug_0 = blocks.tag_debug(gr.sizeof_char*1, 'data', "")
        self.blocks_tag_debug_0.set_display(True)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, '/home/gurrutchalla/Documents/Octave/image_bin3.txt', False, 0, 0)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, '/home/gurrutchalla/Documents/Octave/recieved3.txt', False)
        self.blocks_file_sink_0.set_unbuffered(True)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_file_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.transmitter_hier_0, 0))
        self.connect((self.channels_channel_model_0, 0), (self.reciever_hier_0, 0))
        self.connect((self.reciever_hier_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.reciever_hier_0, 0), (self.blocks_tag_debug_0, 0))
        self.connect((self.transmitter_hier_0, 0), (self.channels_channel_model_0, 0))


    def get_taps(self):
        return self.taps

    def set_taps(self, taps):
        self.taps = taps
        self.channels_channel_model_0.set_taps(self.taps)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_rf_rate(self):
        return self.rf_rate

    def set_rf_rate(self, rf_rate):
        self.rf_rate = rf_rate

    def get_max_noise(self):
        return self.max_noise

    def set_max_noise(self, max_noise):
        self.max_noise = max_noise

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq




def main(top_block_cls=assembled7, options=None):
    tb = top_block_cls()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    tb.start()

    try:
        input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
