#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: gurrutchalla
# GNU Radio version: 3.10.10.0

from gnuradio import blocks
import pmt
from gnuradio import channels
from gnuradio.filter import firdes
from gnuradio import digital
from gnuradio import fec
from gnuradio import filter
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import gr, pdu
import assembled9_epy_block_0 as epy_block_0  # embedded python block




class assembled9(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)

        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 4
        self.qpsk = qpsk = digital.constellation_rect([+0.7071+0.7071j, -0.7071+0.7071j, +0.7071-0.7071j, -0.7071-0.7071j], [0, 1, 2, 3],
        4, 2, 2, 1, 1).base()
        self.nfilts = nfilts = 32
        self.excess_bw = excess_bw = 0.35
        self.variable_adaptive_algorithm_0 = variable_adaptive_algorithm_0 = digital.adaptive_algorithm_cma( qpsk, .0001, 4).base()
        self.taps = taps = [1.0, 0.25-0.25j, 0.50 + 0.10j, -0.3 + 0.2j]
        self.samp_rate = samp_rate = 32000
        self.rrc_taps = rrc_taps = firdes.root_raised_cosine(nfilts, nfilts,1.0/sps, excess_bw, (11*sps*nfilts))
        self.rf_rate = rf_rate = 3552000*8
        self.message_size = message_size = 256
        self.loop_bw = loop_bw = 62.8319e-3
        self.len_key = len_key = "packet length"
        self.enc_cc = enc_cc = fec.cc_encoder_make((12000*2),7, 2, [109,79], 0, fec.CC_TERMINATED, True)
        self.dec_cc = dec_cc = fec.cc_decoder.make((12000*2),7, 2, [109,79], 0, (-1), fec.CC_TERMINATED, True)
        self.center_freq = center_freq = 5000e6

        ##################################################
        # Blocks
        ##################################################

        self.rational_resampler_xxx_0_1 = filter.rational_resampler_ccc(
                interpolation=(3552000*8),
                decimation=3552000,
                taps=[],
                fractional_bw=0.4)
        self.rational_resampler_xxx_0_0_0 = filter.rational_resampler_ccc(
                interpolation=3552000,
                decimation=(3552000*8),
                taps=[],
                fractional_bw=0.4)
        self.pdu_tagged_stream_to_pdu_0_1 = pdu.tagged_stream_to_pdu(gr.types.byte_t, len_key)
        self.pdu_pdu_to_tagged_stream_0 = pdu.pdu_to_tagged_stream(gr.types.byte_t, len_key)
        self.fec_extended_encoder_0 = fec.extended_encoder(encoder_obj_list=enc_cc, threading= None, puncpat='11')
        self.fec_extended_decoder_0 = fec.extended_decoder(decoder_obj_list=dec_cc, threading= None, ann=None, puncpat='11', integration_period=10000)
        self.epy_block_0 = epy_block_0.blk()
        self.digital_scrambler_bb_0_0 = digital.scrambler_bb(0x8A, 0x7F, 7)
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_ccf(4.0, loop_bw, rrc_taps, nfilts, (nfilts/2), 1.5, 1)
        self.digital_map_bb_0_0 = digital.map_bb([-1,1])
        self.digital_map_bb_0 = digital.map_bb([0,1,2,3])
        self.digital_linear_equalizer_0 = digital.linear_equalizer(15, 1, variable_adaptive_algorithm_0, True, [ ], 'corr_est')
        self.digital_diff_decoder_bb_0 = digital.diff_decoder_bb(4, digital.DIFF_DIFFERENTIAL)
        self.digital_descrambler_bb_0 = digital.descrambler_bb(0x8a, 0x7F, 7)
        self.digital_costas_loop_cc_0 = digital.costas_loop_cc(loop_bw, 4, False)
        self.digital_correlate_access_code_xx_ts_0 = digital.correlate_access_code_bb_ts('11100001010110101110100010010011',
          3, len_key)
        self.digital_constellation_modulator_0 = digital.generic_mod(
            constellation=qpsk,
            differential=True,
            samples_per_symbol=sps,
            pre_diff_code=True,
            excess_bw=excess_bw,
            verbose=False,
            log=False,
            truncate=False)
        self.digital_constellation_decoder_cb_0 = digital.constellation_decoder_cb(qpsk)
        self.channels_channel_model_0 = channels.channel_model(
            noise_voltage=1.4,
            frequency_offset=(1e-4),
            epsilon=1.00005,
            taps=taps,
            noise_seed=0,
            block_tags=True)
        self.blocks_vector_to_stream_0_0 = blocks.vector_to_stream(gr.sizeof_char*1, 16)
        self.blocks_vector_to_stream_0 = blocks.vector_to_stream(gr.sizeof_char*1, 16)
        self.blocks_unpack_k_bits_bb_0_1_1_0_0_0 = blocks.unpack_k_bits_bb(8)
        self.blocks_unpack_k_bits_bb_0_1_1_0_0 = blocks.unpack_k_bits_bb(8)
        self.blocks_unpack_k_bits_bb_0_1_0 = blocks.unpack_k_bits_bb(2)
        self.blocks_unpack_k_bits_bb_0 = blocks.unpack_k_bits_bb(8)
        self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_char*1, 96e3,True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, 96e3,True)
        self.blocks_tag_debug_0 = blocks.tag_debug(gr.sizeof_char*1, 'data', "")
        self.blocks_tag_debug_0.set_display(True)
        self.blocks_stream_to_vector_0_0 = blocks.stream_to_vector(gr.sizeof_char*1, 16)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_char*1, 16)
        self.blocks_stream_to_tagged_stream_0_0 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, message_size, len_key)
        self.blocks_pack_k_bits_bb_0_0_2_1_0_0 = blocks.pack_k_bits_bb(8)
        self.blocks_pack_k_bits_bb_0_0_2_1_0 = blocks.pack_k_bits_bb(8)
        self.blocks_pack_k_bits_bb_0_0_2_1 = blocks.pack_k_bits_bb(8)
        self.blocks_pack_k_bits_bb_0_0_2_0 = blocks.pack_k_bits_bb(8)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_cc(.8)
        self.blocks_matrix_interleaver_0_0 = blocks.matrix_interleaver(
            itemsize=gr.sizeof_char * 16, rows=4, cols=4, deint=True
        )
        self.blocks_matrix_interleaver_0 = blocks.matrix_interleaver(
            itemsize=gr.sizeof_char * 16, rows=4, cols=4, deint=False
        )
        self.blocks_file_source_0_0_0 = blocks.file_source(gr.sizeof_char*1, 'F:\\Semester - 03\\EN2130_Communication Design Project\\Octave\\Octave\\image_bin1.txt', False, 0, 0)
        self.blocks_file_source_0_0_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0_0_0 = blocks.file_sink(gr.sizeof_char*1, 'F:\\Semester - 03\\EN2130_Communication Design Project\\Octave\\Octave\\recieved1.txt', False)
        self.blocks_file_sink_0_0_0.set_unbuffered(True)
        self.blocks_char_to_float_1_2_0 = blocks.char_to_float(1, 1)


        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.epy_block_0, 'PDU_out'), (self.pdu_pdu_to_tagged_stream_0, 'pdus'))
        self.msg_connect((self.pdu_tagged_stream_to_pdu_0_1, 'pdus'), (self.epy_block_0, 'PDU_in'))
        self.connect((self.blocks_char_to_float_1_2_0, 0), (self.fec_extended_decoder_0, 0))
        self.connect((self.blocks_file_source_0_0_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_matrix_interleaver_0, 0), (self.blocks_vector_to_stream_0, 0))
        self.connect((self.blocks_matrix_interleaver_0_0, 0), (self.blocks_vector_to_stream_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.channels_channel_model_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_0_0_2_0, 0), (self.blocks_stream_to_vector_0_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_0_0_2_1, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_0_0_2_1_0, 0), (self.blocks_throttle_0_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_0_0_2_1_0_0, 0), (self.digital_constellation_modulator_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0_0, 0), (self.pdu_tagged_stream_to_pdu_0_1, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.blocks_matrix_interleaver_0, 0))
        self.connect((self.blocks_stream_to_vector_0_0, 0), (self.blocks_matrix_interleaver_0_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_unpack_k_bits_bb_0_1_1_0_0, 0))
        self.connect((self.blocks_throttle_0_0, 0), (self.blocks_file_sink_0_0_0, 0))
        self.connect((self.blocks_throttle_0_0, 0), (self.blocks_tag_debug_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0, 0), (self.digital_map_bb_0_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0_1_0, 0), (self.digital_descrambler_bb_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0_1_1_0_0, 0), (self.fec_extended_encoder_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0_1_1_0_0_0, 0), (self.digital_scrambler_bb_0_0, 0))
        self.connect((self.blocks_vector_to_stream_0, 0), (self.blocks_stream_to_tagged_stream_0_0, 0))
        self.connect((self.blocks_vector_to_stream_0_0, 0), (self.blocks_unpack_k_bits_bb_0, 0))
        self.connect((self.channels_channel_model_0, 0), (self.rational_resampler_xxx_0_0_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self.digital_diff_decoder_bb_0, 0))
        self.connect((self.digital_constellation_modulator_0, 0), (self.rational_resampler_xxx_0_1, 0))
        self.connect((self.digital_correlate_access_code_xx_ts_0, 0), (self.blocks_pack_k_bits_bb_0_0_2_0, 0))
        self.connect((self.digital_costas_loop_cc_0, 0), (self.digital_constellation_decoder_cb_0, 0))
        self.connect((self.digital_descrambler_bb_0, 0), (self.digital_correlate_access_code_xx_ts_0, 0))
        self.connect((self.digital_diff_decoder_bb_0, 0), (self.digital_map_bb_0, 0))
        self.connect((self.digital_linear_equalizer_0, 0), (self.digital_costas_loop_cc_0, 0))
        self.connect((self.digital_map_bb_0, 0), (self.blocks_unpack_k_bits_bb_0_1_0, 0))
        self.connect((self.digital_map_bb_0_0, 0), (self.blocks_char_to_float_1_2_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.digital_linear_equalizer_0, 0))
        self.connect((self.digital_scrambler_bb_0_0, 0), (self.blocks_pack_k_bits_bb_0_0_2_1_0_0, 0))
        self.connect((self.fec_extended_decoder_0, 0), (self.blocks_pack_k_bits_bb_0_0_2_1_0, 0))
        self.connect((self.fec_extended_encoder_0, 0), (self.blocks_pack_k_bits_bb_0_0_2_1, 0))
        self.connect((self.pdu_pdu_to_tagged_stream_0, 0), (self.blocks_unpack_k_bits_bb_0_1_1_0_0_0, 0))
        self.connect((self.rational_resampler_xxx_0_0_0, 0), (self.digital_pfb_clock_sync_xxx_0, 0))
        self.connect((self.rational_resampler_xxx_0_1, 0), (self.blocks_multiply_const_vxx_0_0, 0))


    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/self.sps, self.excess_bw, (11*self.sps*self.nfilts)))

    def get_qpsk(self):
        return self.qpsk

    def set_qpsk(self, qpsk):
        self.qpsk = qpsk
        self.digital_constellation_decoder_cb_0.set_constellation(self.qpsk)

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/self.sps, self.excess_bw, (11*self.sps*self.nfilts)))

    def get_excess_bw(self):
        return self.excess_bw

    def set_excess_bw(self, excess_bw):
        self.excess_bw = excess_bw
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/self.sps, self.excess_bw, (11*self.sps*self.nfilts)))

    def get_variable_adaptive_algorithm_0(self):
        return self.variable_adaptive_algorithm_0

    def set_variable_adaptive_algorithm_0(self, variable_adaptive_algorithm_0):
        self.variable_adaptive_algorithm_0 = variable_adaptive_algorithm_0

    def get_taps(self):
        return self.taps

    def set_taps(self, taps):
        self.taps = taps
        self.channels_channel_model_0.set_taps(self.taps)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_rrc_taps(self):
        return self.rrc_taps

    def set_rrc_taps(self, rrc_taps):
        self.rrc_taps = rrc_taps
        self.digital_pfb_clock_sync_xxx_0.update_taps(self.rrc_taps)

    def get_rf_rate(self):
        return self.rf_rate

    def set_rf_rate(self, rf_rate):
        self.rf_rate = rf_rate

    def get_message_size(self):
        return self.message_size

    def set_message_size(self, message_size):
        self.message_size = message_size
        self.blocks_stream_to_tagged_stream_0_0.set_packet_len(self.message_size)
        self.blocks_stream_to_tagged_stream_0_0.set_packet_len_pmt(self.message_size)

    def get_loop_bw(self):
        return self.loop_bw

    def set_loop_bw(self, loop_bw):
        self.loop_bw = loop_bw
        self.digital_costas_loop_cc_0.set_loop_bandwidth(self.loop_bw)
        self.digital_pfb_clock_sync_xxx_0.set_loop_bandwidth(self.loop_bw)

    def get_len_key(self):
        return self.len_key

    def set_len_key(self, len_key):
        self.len_key = len_key

    def get_enc_cc(self):
        return self.enc_cc

    def set_enc_cc(self, enc_cc):
        self.enc_cc = enc_cc

    def get_dec_cc(self):
        return self.dec_cc

    def set_dec_cc(self, dec_cc):
        self.dec_cc = dec_cc

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq




def main(top_block_cls=assembled9, options=None):
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
