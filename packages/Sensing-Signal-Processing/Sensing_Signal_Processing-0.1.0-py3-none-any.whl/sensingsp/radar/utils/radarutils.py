import bpy
import numpy as np
from mathutils import Vector

LightSpeed = 299792458  # Speed of light in m/s

def predefined_array_configs_TI_Cascade_AWR2243(isuite, iradar, location, rotation, f0=70e9):  # 3 x 4
    Lambda = LightSpeed / f0
    Suitename = f'SuitePlane_{isuite}'
    Suite_obj = bpy.data.objects[Suitename]

    bpy.ops.object.empty_add(type='PLAIN_AXES', align='WORLD', location=location, rotation=rotation, scale=(1, 1, 1))
    empty = bpy.context.object
    empty.name = f'RadarPlane_{isuite}_{iradar}_{0}'
    empty.parent = Suite_obj
    empty = setDefaults(empty,f0)

    s = 0.05
    Type = 'SPOT'

    tx_positions = [
        (0, 0),
        (-4, 0),
        (-8, 0),
        (-9, 1),
        (-10, 4),
        (-11, 6),
        (-12, 0),
        (-16, 0),
        (-20, 0),
        (-24, 0),
        (-28, 0),
        (-32, 0)
    ]

    for i, pos in enumerate(tx_positions):
        bpy.ops.object.light_add(type=Type, radius=1, location=(pos[0]*Lambda/2, pos[1]*Lambda/2, 0))
        tx = bpy.context.object
        tx.scale = (s*Lambda/2, s*Lambda/2, s*Lambda/2)
        tx.name = f'TX_{isuite}_{iradar}_{1}_{0}_{i+1:05}'
        tx.parent = empty

    bx0 = -17
    bx = bx0
    by = 34
    s = 1

    rx_positions = [
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 0),
        (11, 0),
        (11+1, 0),
        (11+2, 0),
        (11+3, 0),
        (46, 0),
        (46+1, 0),
        (46+2, 0),
        (46+3, 0),
        (53-3, 0),
        (53-2, 0),
        (53-1, 0),
        (53, 0)
    ]

    for i, pos in enumerate(rx_positions):
        bpy.ops.object.camera_add(location=( -(bx+pos[0])*Lambda/2, (by+pos[1])*Lambda/2, 0), rotation=(0, 0, 0))
        rx = bpy.context.object
        rx.scale = (s*Lambda/2, s*Lambda/2, s*Lambda/2)
        rx.name = f'RX_{isuite}_{iradar}_{1}_{0}_{i+1:05}'
        rx.parent = empty
        rx.data.lens = 10



def predefined_array_configs_LinearArray(isuite, iradar, location, rotation, f0=2.447e9,
                                         LinearArray_TXPos =[0],
                                         LinearArray_RXPos =[.56,.84,.98]):
    Lambda = LightSpeed / f0
    Suitename = f'SuitePlane_{isuite}'
    Suite_obj = bpy.data.objects[Suitename]

    bpy.ops.object.empty_add(type='PLAIN_AXES', align='WORLD', location=location, rotation=rotation, scale=(1, 1, 1))
    empty = bpy.context.object
    empty.name = f'RadarPlane_{isuite}_{iradar}_{0}'
    empty.parent = Suite_obj
    empty = setDefaults(empty,f0)
    s = 0.05
    Type = 'SPOT'
    for i, pos in enumerate(LinearArray_TXPos):
        bpy.ops.object.light_add(type=Type, radius=1, location=(pos, 0, 0))
        tx = bpy.context.object
        tx.scale = (s*Lambda/2, s*Lambda/2, s*Lambda/2)
        tx.name = f'TX_{isuite}_{iradar}_{1}_{0}_{i+1:05}'
        tx.parent = empty


    bx0 = 0
    bx = bx0
    by = 0
    s = 1

    rx_positions = [
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 0)
    ]

    for i, pos in enumerate(LinearArray_RXPos):
        bpy.ops.object.camera_add(location=( pos, 0, 0), rotation=(0, 0, 0))
        rx = bpy.context.object
        rx.scale = (s*Lambda/2, s*Lambda/2, s*Lambda/2)
        rx.name = f'RX_{isuite}_{iradar}_{1}_{0}_{i+1:05}'
        rx.parent = empty
        rx.data.lens = 10
        

def predefined_array_configs_TI_IWR6843(isuite, iradar, location, rotation, f0=70e9):  # 3 x 4
    Lambda = LightSpeed / f0
    Suitename = f'SuitePlane_{isuite}'
    Suite_obj = bpy.data.objects[Suitename]

    bpy.ops.object.empty_add(type='PLAIN_AXES', align='WORLD', location=location, rotation=rotation, scale=(1, 1, 1))
    empty = bpy.context.object
    empty.name = f'RadarPlane_{isuite}_{iradar}_{0}'
    empty.parent = Suite_obj
    empty = setDefaults(empty,f0)
    s = 0.05
    Type = 'SPOT'
    tx_positions = [
        (0, 0),
        (-4, 1),
        (-8, 0)
    ]

    for i, pos in enumerate(tx_positions):
        bpy.ops.object.light_add(type=Type, radius=1, location=(pos[0]*Lambda/2, pos[1]*Lambda/2, 0))
        tx = bpy.context.object
        tx.scale = (s*Lambda/2, s*Lambda/2, s*Lambda/2)
        tx.name = f'TX_{isuite}_{iradar}_{1}_{0}_{i+1:05}'
        tx.parent = empty


    bx0 = -6
    bx = bx0
    by = 0
    s = 1

    rx_positions = [
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 0)
    ]

    for i, pos in enumerate(rx_positions):
        bpy.ops.object.camera_add(location=( -(bx+pos[0])*Lambda/2, (by+pos[1])*Lambda/2, 0), rotation=(0, 0, 0))
        rx = bpy.context.object
        rx.scale = (s*Lambda/2, s*Lambda/2, s*Lambda/2)
        rx.name = f'RX_{isuite}_{iradar}_{1}_{0}_{i+1:05}'
        rx.parent = empty
        rx.data.lens = 10
        

def predefined_array_configs_SISO(isuite, iradar, location, rotation, f0=70e9,Pulse1FMCW0=0):
    Lambda = LightSpeed / f0
    Suitename = f'SuitePlane_{isuite}'
    Suite_obj = bpy.data.objects[Suitename]

    bpy.ops.object.empty_add(type='PLAIN_AXES', align='WORLD', location=location, rotation=rotation, scale=(1, 1, 1))
    empty = bpy.context.object
    empty.name = f'RadarPlane_{isuite}_{iradar}_{0}'
    empty.parent = Suite_obj
    empty = setDefaults(empty,f0)
    if Pulse1FMCW0 == 1 :
        empty['RadarMode']='Pulse'
        empty['PulseWaveform']='WaveformFile.txt'
        
        empty['Fs_MHz']=1500
        empty['Ts_ns']=1000/empty['Fs_MHz']
        empty['Range_End']=100
        
    
    s = 0.05
    Type = 'SPOT'
    tx_positions = [
        (0, 0)
    ]

    for i, pos in enumerate(tx_positions):
        bpy.ops.object.light_add(type=Type, radius=1, location=(pos[0]*Lambda/2, pos[1]*Lambda/2, 0))
        tx = bpy.context.object
        tx.scale = (s*Lambda/2, s*Lambda/2, s*Lambda/2)
        tx.name = f'TX_{isuite}_{iradar}_{1}_{0}_{i+1:05}'
        tx.parent = empty


    bx0 = -6
    bx = bx0
    by = 0
    s = 1

    rx_positions = [
        (0, 0)
    ]

    for i, pos in enumerate(rx_positions):
        bpy.ops.object.camera_add(location=( -(bx+pos[0])*Lambda/2, (by+pos[1])*Lambda/2, 0), rotation=(0, 0, 0))
        rx = bpy.context.object
        rx.scale = (s*Lambda/2, s*Lambda/2, s*Lambda/2)
        rx.name = f'RX_{isuite}_{iradar}_{1}_{0}_{i+1:05}'
        rx.parent = empty
        rx.data.lens = 10
    
    
def setDefaults(empty,f0):
    empty["Transmit_Power_dBm"] = 12
    empty["Transmit_Antenna_Element_Gain_dbm"] = 3
    empty["Transmit_Antenna_Element_Azimuth_BeamWidth_deg"] = 120
    empty["Transmit_Antenna_Element_Elevation_BeamWidth_deg"] = 120
    empty["Receive_Antenna_Element_Gain_dbm"] = 0
    empty["Receive_Antenna_Element_Azimuth_BeamWidth_deg"] = 120
    empty["Receive_Antenna_Element_Elevation_BeamWidth_deg"] = 120
    empty["Center_Frequency_GHz"] = f0/1e9
    empty['PRI_us']=70
    empty['Fs_MHz']=5
    empty['Ts_ns']=1000/empty['Fs_MHz']
    empty['NPulse'] = 3 * 64
    empty['N_ADC']  = 128
    empty['RangeWindow']  = 'Hamming'
    empty['DopplerWindow']  = 'Hamming'
    empty['N_FFT_ADC']  = 128
    empty['N_FFT_Doppler']  = 128
    empty['Lambda_mm']=1000*LightSpeed/empty["Center_Frequency_GHz"]/1e9
    empty['FMCW_ChirpTime_us'] = 60
    empty['FMCW_Bandwidth_GHz'] = 1
    empty['Tempreture_K'] = 290
    empty['FMCW_ChirpSlobe_MHz_usec'] = 1000*empty['FMCW_Bandwidth_GHz']/empty['FMCW_ChirpTime_us']
    empty['RangeFFT_OverNextP2'] = 2
    empty['Range_Start']=0
    empty['Range_End']=50
    empty['CFAR_RD_guard_cells']=2
    empty['CFAR_RD_training_cells']=10
    empty['CFAR_RD_false_alarm_rate']=1e-3
    empty['STC_Enabled']=False #
    empty['MTI_Enabled']=False #
    empty['DopplerFFT_OverNextP2']=3
    empty['AzFFT_OverNextP2']=2
    empty['ElFFT_OverNextP2']=3
    empty['CFAR_Angle_guard_cells']=1
    empty['CFAR_Angle_training_cells']=3
    empty['CFAR_Angle_false_alarm_rate']=.1
    empty["FMCW"] = True
    empty['ADC_peak2peak']=2
    empty['ADC_levels']=256
    empty['ADC_ImpedanceFactor']=300
    empty['ADC_LNA_Gain']=1000
    empty['ADC_SaturationEnabled']=False
    empty['RadarMode']='FMCW'# 'Pulse'
    empty['PulseWaveform']='WaveformFile.txt'
    
    return empty
    # , levels,,,