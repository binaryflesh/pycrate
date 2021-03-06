# -*- coding: UTF-8 -*-
#/**
# * Software Name : pycrate
# * Version : 0.4
# *
# * Copyright 2018. Benoit Michau. ANSSI. P1sec.
# *
# * This library is free software; you can redistribute it and/or
# * modify it under the terms of the GNU Lesser General Public
# * License as published by the Free Software Foundation; either
# * version 2.1 of the License, or (at your option) any later version.
# *
# * This library is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# * Lesser General Public License for more details.
# *
# * You should have received a copy of the GNU Lesser General Public
# * License along with this library; if not, write to the Free Software
# * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, 
# * MA 02110-1301  USA
# *
# *--------------------------------------------------------
# * File Name : pycrate_csn1dir/e_utran_parameters_ie.py
# * Created : 2018-11-21
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.060 - d60
# section: 12.53 E-UTRAN Parameters
# top-level object: E-UTRAN Parameters IE

# external references
from pycrate_csn1dir.pcid_group_ie import pcid_group_ie

# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

gprs_e_utran_measurement_parameters_struct = CSN1List(name='gprs_e_utran_measurement_parameters_struct', list=[
  CSN1Bit(name='qsearch_p_e_utran', bit=4),
  CSN1Bit(name='e_utran_rep_quant'),
  CSN1Bit(name='e_utran_multirat_reporting', bit=2),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='e_utran_fdd_reporting_threshold', bit=3),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='e_utran_fdd_reporting_threshold_2', bit=6)])}),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='e_utran_fdd_reporting_offset', bit=3)])})])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='e_utran_tdd_reporting_threshold', bit=3),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='e_utran_tdd_reporting_threshold_2', bit=6)])}),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='e_utran_tdd_reporting_offset', bit=3)])})])})])

repeated_e_utran_pcid_to_ta_mapping_struct = CSN1List(name='repeated_e_utran_pcid_to_ta_mapping_struct', list=[
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Ref(name='pcid_to_ta_mapping', obj=pcid_group_ie)]),
  CSN1Val(name='', val='0'),
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Bit(name='e_utran_frequency_index', bit=3)]),
  CSN1Val(name='', val='0')])

repeated_e_utran_neighbour_cells_struct = CSN1List(name='repeated_e_utran_neighbour_cells_struct', list=[
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Bit(name='earfcn', bit=16),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='measurement_bandwidth', bit=3)])})]),
  CSN1Val(name='', val='0'),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='e_utran_priority', bit=3)])}),
  CSN1Bit(name='thresh_e_utran_high', bit=5),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='thresh_e_utran_low', bit=5)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='e_utran_qrxlevmin', bit=5)])})])

repeated_e_utran_not_allowed_cells_struct = CSN1List(name='repeated_e_utran_not_allowed_cells_struct', list=[
  CSN1Ref(name='not_allowed_cells', obj=pcid_group_ie),
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Bit(name='e_utran_frequency_index', bit=3)]),
  CSN1Val(name='', val='0')])

e_utran_parameters_ie = CSN1List(name='e_utran_parameters_ie', list=[
  CSN1Bit(name='e_utran_ccn_active'),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='gprs_e_utran_measurement_parameters', obj=gprs_e_utran_measurement_parameters_struct)])}),
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Ref(name='repeated_e_utran_neighbour_cells', obj=repeated_e_utran_neighbour_cells_struct)]),
  CSN1Val(name='', val='0'),
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Ref(name='repeated_e_utran_not_allowed_cells', obj=repeated_e_utran_not_allowed_cells_struct)]),
  CSN1Val(name='', val='0'),
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Ref(name='repeated_e_utran_pcid_to_ta_mapping', obj=repeated_e_utran_pcid_to_ta_mapping_struct)]),
  CSN1Val(name='', val='0')])

