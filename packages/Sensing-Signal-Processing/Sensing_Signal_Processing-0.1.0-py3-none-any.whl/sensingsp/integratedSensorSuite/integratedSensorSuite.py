import bpy
import sensingsp as ssp
import numpy as np
from mathutils import Vector
from ..constants import *
from ..utils.stochastics import Complex_Noise_Buffer
import scipy
from matplotlib import pyplot as plt
from ..radar.utils.rss import *
# class integratedSensorSuite:
def define_suite(isuite=0, location=Vector((0, 0, 0)), rotation=Vector((np.pi/2, 0, -np.pi/2))):
    bpy.ops.object.empty_add(type='PLAIN_AXES', align='WORLD', location=location, rotation=rotation, scale=(1, 1, 1))
    suite = bpy.context.object
    suite.name = f'SuitePlane_{isuite}'
    return suite


def SensorsSignalGeneration(): # input is ssp.Paths in ssp.config.CurrentFrame
    # def Generate_RadarSignal(self,frame_d_drate_amp,RadarSpecifications):
    SuiteRadarRangePulseRXSignals = []
    for radarSpecifications in ssp.RadarSpecifications:
        RadarRangePulseRX = {'radars':[],'lidars':[],'cameras':[]}
        for specifications in radarSpecifications:
          # B should be analog Filter Bandwidth
          RadarRangePulseRX['radars'].append(Complex_Noise_Buffer(specifications['N_ADC'],specifications['NPulse'],specifications['N_RX'],T=specifications['Tempreture_K'],B=specifications['FMCW_Bandwidth']))
        SuiteRadarRangePulseRXSignals.append(RadarRangePulseRX)
    for i,suite_info in enumerate(ssp.suite_information):
      for cam in suite_info['Camera']:
        SuiteRadarRangePulseRXSignals[i]['cameras'].append(ssp.camera.utils.render(cam))
      for lidar in suite_info['Lidar']:
        SuiteRadarRangePulseRXSignals[i]['lidars'].append(ssp.lidar.utils.pointcloud(lidar))
      
        
    Frame2ArrayIndex = ssp.config.CurrentFrame-bpy.context.scene.frame_start
    # Frame2ArrayIndex = 0
    for isrx,suiteRX_d_drate_amp in ssp.Paths[Frame2ArrayIndex].items():
        for irrx,radarRX_d_drate_amp in suiteRX_d_drate_amp.items():
          for irx,RX_d_drate_amp in radarRX_d_drate_amp.items():
            for istx,suiteTX_d_drate_amp in RX_d_drate_amp.items():
              if istx == isrx:
                for irtx,radarTX_d_drate_amp in suiteTX_d_drate_amp.items():
                  if irtx == irrx:
                    PRI = ssp.RadarSpecifications[isrx][irrx]['PRI']
                    Ts = ssp.RadarSpecifications[isrx][irrx]['Ts']
                    NPulse = ssp.RadarSpecifications[isrx][irrx]['NPulse']
                    N_ADC = ssp.RadarSpecifications[isrx][irrx]['N_ADC']
                    iADC = np.arange(N_ADC)

                    Lambda = ssp.RadarSpecifications[isrx][irrx]['Lambda']
                    FMCW_ChirpSlobe = ssp.RadarSpecifications[isrx][irrx]['FMCW_ChirpSlobe']
                    PrecodingMatrix = ssp.RadarSpecifications[isrx][irrx]['PrecodingMatrix']
                    
                    RadarMode = ssp.RadarSpecifications[isrx][irrx]['RadarMode']
                    FMCWRadar = 1
                    if RadarMode=='FMCW':
                      FMCWRadar = 1
                    if RadarMode=='Pulse':
                      FMCWRadar = 0
                      PulseWaveform = ssp.RadarSpecifications[isrx][irrx]['PulseWaveform']
                      Waveform = ssp.radar.radarwaveforms.barker_code(11)
                      ssp.RadarSpecifications[isrx][irrx]['PulseWaveform_Loaded']=Waveform
                      
                      
                            
                    for itx,TX_d_drate_amp in radarTX_d_drate_amp.items():

                      for d_drate_amp in TX_d_drate_amp:
                        if len(d_drate_amp[3])==0:
                          continue
                        HardwareDCBlockerAttenuation = 1 # d_drate_amp[1]
                        # if d_drate_amp[1]==0:
                        #   continue
                        # if d_drate_amp[0]==0: TX RX same position
                        #   continue
                        # if d_drate_amp[0] > PRI*LightSpeed:
                        #   Save it in a buffer for next pulses or fix PRF : effective_d = mod(d_drate_amp[0] , PRI*LightSpeed)
                        #   continue
                        
                        SimDopplerEffect = 1 # Should be 1; for test and analysis, can set to 0
                        for ip in range(NPulse):
                          d_of_t =  d_drate_amp[0] + (ip * PRI + iADC * Ts) * d_drate_amp[1]*SimDopplerEffect
                          
                          if FMCWRadar == 1:
                            phase2 = 2*np.pi*(
                              d_of_t/Lambda
                              +FMCW_ChirpSlobe/LightSpeed*iADC * Ts*d_of_t
                              -.5*FMCW_ChirpSlobe*(d_of_t/LightSpeed)*(d_of_t/LightSpeed)
                              )
                            ipPM = ip % PrecodingMatrix.shape[0]
                            SuiteRadarRangePulseRXSignals[isrx]['radars'][irrx][iADC,ip,irx] += PrecodingMatrix[ipPM][itx]*d_drate_amp[2]*np.exp(1j*phase2) * HardwareDCBlockerAttenuation
                        #   ssp.RadarSpecifications[isrx][irrx]['RangePulseRX'][iADC,ip,irx]+=PrecodingMatrix[ipPM][itx]*d_drate_amp[2]*np.exp(1j*phase2) * HardwareDCBlockerAttenuation
                          elif FMCWRadar == 0:
                            Window_Waveform = np.zeros_like(d_of_t,dtype=complex)
                            ind1 = int( (d_drate_amp[0] + (ip * PRI + 0 * Ts) * d_drate_amp[1]) / LightSpeed / Ts)
                            if ind1 < Window_Waveform.shape[0]:
                              ind1 = np.arange(ind1,min([ind1+Waveform.shape[0],Window_Waveform.shape[0]]))
                              ind2 = np.arange(0,ind1.shape[0])
                              Window_Waveform[ind1]=Waveform[ind2]
                              phase2 = 2*np.pi*(d_of_t/Lambda)
                              ipPM = ip % PrecodingMatrix.shape[0]
                              SuiteRadarRangePulseRXSignals[isrx]['radars'][irrx][iADC,ip,irx] += PrecodingMatrix[ipPM][itx]*d_drate_amp[2]*np.exp(1j*phase2)*Window_Waveform
    ## Ampedance and ADC 
    for isuite in range(len(SuiteRadarRangePulseRXSignals)):
      for iradar in range(len(SuiteRadarRangePulseRXSignals[isuite]['radars'])):
        specifications = ssp.RadarSpecifications[isuite][iradar]
        ImpedanceFactor = np.sqrt(specifications['ADC_ImpedanceFactor'])
        LNA_Gain = specifications['ADC_LNA_Gain']
        ADC_Peak2Peak = specifications['ADC_peak2peak']
        ADC_Levels = specifications['ADC_levels']
        SuiteRadarRangePulseRXSignals[isrx]['radars'][irrx] = apply_adc(SuiteRadarRangePulseRXSignals[isrx]['radars'][irrx],ADC_Peak2Peak,ADC_Levels,ImpedanceFactor,LNA_Gain,specifications['ADC_SaturationEnabled'])
        # real = np.real(SuiteRadarRangePulseRXSignals[isrx]['radars'][irrx])*ImpedanceFactor*LNA_Gain
        # real = (real + (ADC_Peak2Peak / 2)) / ADC_Peak2Peak
        # real = np.clip(real, 0, 1)
        # real = np.round(real * (ADC_Levels - 1))-(ADC_Levels - 1)/2
        # imag = np.imag(SuiteRadarRangePulseRXSignals[isrx]['radars'][irrx])*ImpedanceFactor*LNA_Gain
        # imag = (imag + (ADC_Peak2Peak / 2)) / ADC_Peak2Peak
        # imag = np.clip(imag, 0, 1)
        # imag = np.round(imag * (ADC_Levels - 1)) - (ADC_Levels - 1)/2
        # SuiteRadarRangePulseRXSignals[isrx]['radars'][irrx] = real+1j*imag
    return SuiteRadarRangePulseRXSignals

def SensorsSignalGeneration_frame(path_d_drate_amp): # input is ssp.Paths in ssp.config.CurrentFrame
    # def Generate_RadarSignal(self,frame_d_drate_amp,RadarSpecifications):
    SuiteRadarRangePulseRXSignals = []
    for radarSpecifications in ssp.RadarSpecifications:
        RadarRangePulseRX = {'radars':[],'lidars':[],'cameras':[]}
        for specifications in radarSpecifications:
          # B should be analog Filter Bandwidth
          RadarRangePulseRX['radars'].append(Complex_Noise_Buffer(specifications['N_ADC'],specifications['NPulse'],specifications['N_RX'],T=specifications['Tempreture_K'],B=specifications['FMCW_Bandwidth']))
        SuiteRadarRangePulseRXSignals.append(RadarRangePulseRX)
    for i,suite_info in enumerate(ssp.suite_information):
      for cam in suite_info['Camera']:
        SuiteRadarRangePulseRXSignals[i]['cameras'].append(ssp.camera.utils.render(cam))
      for lidar in suite_info['Lidar']:
        SuiteRadarRangePulseRXSignals[i]['lidars'].append(ssp.lidar.utils.pointcloud(lidar))
    
    for isrx,suiteRX_d_drate_amp in path_d_drate_amp.items():
        for irrx,radarRX_d_drate_amp in suiteRX_d_drate_amp.items():
          for irx,RX_d_drate_amp in radarRX_d_drate_amp.items():
            for istx,suiteTX_d_drate_amp in RX_d_drate_amp.items():
              if istx == isrx:
                for irtx,radarTX_d_drate_amp in suiteTX_d_drate_amp.items():
                  if irtx == irrx:
                    PRI = ssp.RadarSpecifications[isrx][irrx]['PRI']
                    Ts = ssp.RadarSpecifications[isrx][irrx]['Ts']
                    NPulse = ssp.RadarSpecifications[isrx][irrx]['NPulse']
                    N_ADC = ssp.RadarSpecifications[isrx][irrx]['N_ADC']
                    iADC = np.arange(N_ADC)

                    Lambda = ssp.RadarSpecifications[isrx][irrx]['Lambda']
                    FMCW_ChirpSlobe = ssp.RadarSpecifications[isrx][irrx]['FMCW_ChirpSlobe']
                    PrecodingMatrix = ssp.RadarSpecifications[isrx][irrx]['PrecodingMatrix']
                    
                    RadarMode = ssp.RadarSpecifications[isrx][irrx]['RadarMode']
                    FMCWRadar = 1
                    if RadarMode=='FMCW':
                      FMCWRadar = 1
                    if RadarMode=='Pulse':
                      FMCWRadar = 0
                      PulseWaveform = ssp.RadarSpecifications[isrx][irrx]['PulseWaveform']
                      Waveform = ssp.radar.radarwaveforms.barker_code(11)
                      ssp.RadarSpecifications[isrx][irrx]['PulseWaveform_Loaded']=Waveform
                      
                      
                            
                    for itx,TX_d_drate_amp in radarTX_d_drate_amp.items():

                      for d_drate_amp in TX_d_drate_amp:
                        
                        # if len(d_drate_amp[3])==0:
                        #   continue
                        HardwareDCBlockerAttenuation = 1 # d_drate_amp[1]
                        # if d_drate_amp[1]==0:
                        #   continue
                        # if d_drate_amp[0]==0: TX RX same position
                        #   continue
                        # if d_drate_amp[0] > PRI*LightSpeed:
                        #   Save it in a buffer for next pulses or fix PRF : effective_d = mod(d_drate_amp[0] , PRI*LightSpeed)
                        #   continue
                        
                        SimDopplerEffect = 1 # Should be 1; for test and analysis, can set to 0
                        for ip in range(NPulse):
                          d_of_t =  d_drate_amp[0] + (ip * PRI + iADC * Ts) * d_drate_amp[1]*SimDopplerEffect
                          
                          if FMCWRadar == 1:
                            phase2 = 2*np.pi*(
                              d_of_t/Lambda
                              +FMCW_ChirpSlobe/LightSpeed*iADC * Ts*d_of_t
                              -.5*FMCW_ChirpSlobe*(d_of_t/LightSpeed)*(d_of_t/LightSpeed)
                              )
                            ipPM = ip % PrecodingMatrix.shape[0]
                            SuiteRadarRangePulseRXSignals[isrx]['radars'][irrx][iADC,ip,irx] += PrecodingMatrix[ipPM][itx]*d_drate_amp[2]*np.exp(1j*phase2) * HardwareDCBlockerAttenuation
                        #   ssp.RadarSpecifications[isrx][irrx]['RangePulseRX'][iADC,ip,irx]+=PrecodingMatrix[ipPM][itx]*d_drate_amp[2]*np.exp(1j*phase2) * HardwareDCBlockerAttenuation
                          elif FMCWRadar == 0:
                            Window_Waveform = np.zeros_like(d_of_t,dtype=complex)
                            ind1 = int( (d_drate_amp[0] + (ip * PRI + 0 * Ts) * d_drate_amp[1]) / LightSpeed / Ts)
                            if ind1 < Window_Waveform.shape[0]:
                              ind1 = np.arange(ind1,min([ind1+Waveform.shape[0],Window_Waveform.shape[0]]))
                              ind2 = np.arange(0,ind1.shape[0])
                              Window_Waveform[ind1]=Waveform[ind2]
                              phase2 = 2*np.pi*(d_of_t/Lambda)
                              ipPM = ip % PrecodingMatrix.shape[0]
                              SuiteRadarRangePulseRXSignals[isrx]['radars'][irrx][iADC,ip,irx] += PrecodingMatrix[ipPM][itx]*d_drate_amp[2]*np.exp(1j*phase2)*Window_Waveform
    ## Ampedance and ADC 
    for isuite in range(len(SuiteRadarRangePulseRXSignals)):
      for iradar in range(len(SuiteRadarRangePulseRXSignals[isuite]['radars'])):
        specifications = ssp.RadarSpecifications[isuite][iradar]
        ImpedanceFactor = np.sqrt(specifications['ADC_ImpedanceFactor'])
        LNA_Gain = specifications['ADC_LNA_Gain']
        ADC_Peak2Peak = specifications['ADC_peak2peak']
        ADC_Levels = specifications['ADC_levels']
        SuiteRadarRangePulseRXSignals[isrx]['radars'][irrx] = apply_adc(SuiteRadarRangePulseRXSignals[isrx]['radars'][irrx],ADC_Peak2Peak,ADC_Levels,ImpedanceFactor,LNA_Gain,specifications['ADC_SaturationEnabled'])
        # real = np.real(SuiteRadarRangePulseRXSignals[isrx]['radars'][irrx])*ImpedanceFactor*LNA_Gain
        # real = (real + (ADC_Peak2Peak / 2)) / ADC_Peak2Peak
        # real = np.clip(real, 0, 1)
        # real = np.round(real * (ADC_Levels - 1))-(ADC_Levels - 1)/2
        # imag = np.imag(SuiteRadarRangePulseRXSignals[isrx]['radars'][irrx])*ImpedanceFactor*LNA_Gain
        # imag = (imag + (ADC_Peak2Peak / 2)) / ADC_Peak2Peak
        # imag = np.clip(imag, 0, 1)
        # imag = np.round(imag * (ADC_Levels - 1)) - (ADC_Levels - 1)/2
        # SuiteRadarRangePulseRXSignals[isrx]['radars'][irrx] = real+1j*imag
    return SuiteRadarRangePulseRXSignals


def SensorsSignalProccessing(Signals):
      
      RangeDopplerDistributed = []
      for isuite,radarSpecifications in enumerate(ssp.RadarSpecifications):
          RangeDopplerDistributed0 = []
          All_RangeResolutions = []
          for iradar,specifications in enumerate(radarSpecifications):

            XRadar = Signals[isuite]['radars'][iradar]
            FMCW_ChirpSlobe = ssp.RadarSpecifications[isuite][iradar]['FMCW_ChirpSlobe']
            Ts = ssp.RadarSpecifications[isuite][iradar]['Ts']
            PRI = ssp.RadarSpecifications[isuite][iradar]['PRI']
            Lambda = ssp.RadarSpecifications[isuite][iradar]['Lambda']
            PrecodingMatrix = ssp.RadarSpecifications[isuite][iradar]['PrecodingMatrix']

            All_RangeResolutions.append( LightSpeed/2/ssp.RadarSpecifications[isuite][iradar]['FMCW_Bandwidth'] )

            fast_time_window = scipy.signal.windows.hamming(XRadar.shape[0])
            X_windowed_fast = XRadar * fast_time_window[:, np.newaxis, np.newaxis]

            NFFT_Range_OverNextPow2 =  specifications['RangeFFT_OverNextP2']
            NFFT_Range = int(2 ** (np.ceil(np.log2(XRadar.shape[0]))+NFFT_Range_OverNextPow2))
            X_fft_fast = np.fft.fft(X_windowed_fast, axis=0, n=NFFT_Range)  # beat freq = Slobe * 2 * d / c =   ind / nfft * Fs ->
            d_fft = np.arange(NFFT_Range) * LightSpeed / 2 / FMCW_ChirpSlobe / NFFT_Range / Ts

            # plt.plot(d_fft,np.abs(X_fft_fast[:,0,0]))
            # yyyyyyy


            Range_Start = specifications['Range_Start']
            Range_End = specifications['Range_End']
            d1i = int(NFFT_Range*Range_Start/100.0)
            d2i = int(NFFT_Range*Range_End/100.0)
            d_fft = d_fft[d1i:d2i]
            X_fft_fast = X_fft_fast[d1i:d2i,:,:] #(67 Range, 96 Pulse, 4 RX)

            # STC_Enabled = 0
            # if STC_Enabled:
            #   STC_Signal = (d_fft + .001) **2
            #   X_fft_fast = X_fft_fast * STC_Signal[:, np.newaxis, np.newaxis]

            # print("XRadar shape:", XRadar.shape)
            # XRadar shape: (128, 192, 16)

            M_TX=PrecodingMatrix.shape[1]#specifications['M_TX']
            L = X_fft_fast.shape[1]
            Leff = int(L/M_TX)
            # slow_time_window = scipy.signal.windows.hamming(X_fft_fast.shape[1])
            # X_windowed_slow = X_fft_fast * slow_time_window[np.newaxis,:,np.newaxis,np.newaxis]
            N_Doppler = Leff
            f_Doppler = np.hstack((np.linspace(-0.5/PRI/M_TX, 0, N_Doppler)[:-1], np.linspace(0, 0.5/PRI/M_TX, N_Doppler)))

            PrecodingMatrixInv = np.linalg.pinv(PrecodingMatrix)

            rangeDopplerTXRX = np.zeros((X_fft_fast.shape[0], f_Doppler.shape[0], M_TX, X_fft_fast.shape[2]),dtype=complex)
            for idop , f_Doppler_i in enumerate(f_Doppler):
              dopplerSteeringVector = np.exp(1j*2*np.pi*f_Doppler_i*np.arange(L)*PRI)
              X_doppler_comp = X_fft_fast * np.conj(dopplerSteeringVector[np.newaxis,:,np.newaxis])
              if 1:
                rangeTXRX = np.einsum('ijk,lj->ilk', X_doppler_comp, PrecodingMatrixInv)
              else:
                rangeTXRX = np.zeros((X_doppler_comp.shape[0], PrecodingMatrixInv.shape[0], X_doppler_comp.shape[2]),dtype=X_doppler_comp.dtype)
                for i_r in range(X_doppler_comp.shape[0]):
                  for i_rx in range(X_doppler_comp.shape[2]):
                    temp = PrecodingMatrixInv @ X_doppler_comp[i_r,:,i_rx]
                    rangeTXRX[i_r,:,i_rx] = temp
                # print("with conj",np.linalg.norm(np.conj(np.einsum('ijk,lj->ilk', X_doppler_comp, PrecodingMatrixInv))-rangeTXRX)) % Not correct
                # print(np.linalg.norm((np.einsum('ijk,lj->ilk', X_doppler_comp, PrecodingMatrixInv))-rangeTXRX)) % Correct
                # print(np.linalg.norm(rangeTXRX))
                # ccccccccccccc

              # print(rangeTXRX.shape) (64, 12, 16)
              rangeDopplerTXRX[:, idop, :, :] = rangeTXRX

            # for irange in range(rangeDopplerTXRX.shape[0]):
            #   plt.plot(f_Doppler,np.abs(rangeDopplerTXRX[irange,:,0,0]))
            # plt.figure()
            # plt.imshow(np.abs(rangeDopplerTXRX[:,:,0,0]), aspect='auto')
            # xxxxxxxx
            RangeDopplerDistributed0.append([rangeDopplerTXRX,d_fft,f_Doppler])
          RangeDopplerDistributed.append(RangeDopplerDistributed0)
      # RangeAngleMapCalc = 1
      # if RangeAngleMapCalc:
      #   print("Range Angle Map Calculation ...")
      #   for isuite,radarSpecifications in enumerate(ssp.RadarSpecifications):
      #     for iradar,specifications in enumerate(radarSpecifications):
      #       global_location_TX,global_location_RX,global_location_Center = specifications['global_location_TX_RX_Center']
      #       PosIndex = np.array(specifications['Local_location_TXplusRX_Center'])
      #       azimuths = PosIndex[:, 0]
      #       elevations = PosIndex[:, 1]

      #       d_az = np.max(azimuths)-np.min(azimuths)
      #       d_el = np.max(elevations)-np.min(elevations)
      #       if d_az>d_el:
      #         sorted_indices = np.argsort(azimuths)
      #         sorted_PosIndex = PosIndex[sorted_indices,:]
      #         sorted_PosIndex[:,0]-=sorted_PosIndex[0,0]
      #         sorted_PosIndex[:,1]-=sorted_PosIndex[0,1]
      #         sorted_PosIndex[:,0]=np.round(sorted_PosIndex[:,0])
      #         sorted_PosIndex[:,1]=np.round(sorted_PosIndex[:,1])

      #         unique_azimuths, unique_indices = np.unique(sorted_PosIndex[:, 0], return_index=True)
      #         unique_PosIndex = sorted_PosIndex[unique_indices,:]

      #         # print(unique_PosIndex)




      #       rangeDopplerTXRX,d_fft,f_Doppler = RangeDopplerDistributed[isuite][iradar]
      #       rangeTXRX = np.mean(rangeDopplerTXRX,axis=1)

      #       # Selected_ind = [(0,0), (1,7), (2,6), (11,15)]
      #       # rows, cols = zip(*Selected_ind)
      #       rows = unique_PosIndex[:,2].astype(int)
      #       cols = unique_PosIndex[:,3].astype(int)
      #       # print(rows)
      #       # print(cols)
      #       rangeVA = rangeTXRX[:, rows, cols]
      #       angle_window = scipy.signal.windows.hamming(rangeVA.shape[1])
      #       X_windowed_rangeVA = rangeVA * angle_window[np.newaxis,:]

      #       NFFT_Angle_OverNextPow2 =  1
      #       NFFT_Angle = int(2 ** (np.ceil(np.log2(X_windowed_rangeVA.shape[1]))+NFFT_Angle_OverNextPow2))
      #       RangeAngleMap = np.fft.fft(X_windowed_rangeVA, axis=1, n=NFFT_Angle)  # beat freq = Slobe * 2 * d / c =   ind / nfft * Fs ->
      #       RangeAngleMap = np.fft.fftshift(RangeAngleMap, axes=1)
      #       # sina_fft = np.rad2deg(np.arcsin(np.linspace(-1,1,NFFT_AngleNFFT_Angle)))
      #       extent = [-.5 ,.5,d_fft[-1],d_fft[0]]
      #       plt.figure()
      #       plt.imshow(np.abs(RangeAngleMap), extent=extent, aspect='auto')

      #       angles = np.linspace(-np.pi/2, np.pi/2, NFFT_Angle)

      #       # Define range bins from d_fft
      #       ranges = d_fft
      #       R, Theta = np.meshgrid(ranges, angles)
      #       plt.figure()
      #       ax = plt.subplot(111, polar=True)
      #       c = ax.pcolormesh(Theta, R, np.abs(RangeAngleMap).T, shading='auto')
      #       ax.set_thetalim(-np.pi/2, np.pi/2)
      #       ax.set_ylim(0, ranges[-1])
      #       plt.colorbar(c, label='Magnitude')
      #       plt.show()

      # Uncomment2SeePolarRangeAngle
      # xxxxxxxxxxxxxxxx
      print("Grid Search")
      x_start, y_start, z_start = ssp.config.Detection_Parameters_xyz_start
      N_x, N_y, N_z = ssp.config.Detection_Parameters_xyz_N
      gridlen = ssp.config.Detection_Parameters_gridlen
      x_points = x_start + (np.arange(N_x)) * gridlen
      y_points = y_start + (np.arange(N_y)) * gridlen
      z_points = z_start + (np.arange(N_z)) * gridlen
      X, Y, Z = np.meshgrid(x_points, y_points, z_points, indexing='ij')
      grid_points = np.vstack([X.ravel(), Y.ravel(), Z.ravel()]).T # 1000 x 3

      vx_start, vy_start, vz_start = 0, 0, 0
      N_vx, N_vy, N_vz = 1, 1, 1
      gridvlen = 0
      vx_points = vx_start + (np.arange(N_vx)) * gridvlen
      vy_points = vy_start + (np.arange(N_vy)) * gridvlen
      vz_points = vz_start + (np.arange(N_vz)) * gridvlen
      X, Y, Z = np.meshgrid(vx_points, vy_points, vz_points, indexing='ij')
      grid_velocities = np.vstack([X.ravel(), Y.ravel(), Z.ravel()]).T # 1000 x 3
      all_outputs = []

      for i_grid_points in range(grid_points.shape[0]):
        # clear_output()
        print("Grid Search: ",i_grid_points,grid_points.shape[0])
        p0=Vector(grid_points[i_grid_points,:])
        for i_grid_velocities in range(grid_velocities.shape[0]):
          v0=Vector(grid_velocities[i_grid_velocities,:])
          # DetectionCount = 0
          Detection_data = []
          for isuite,radarSpecifications in enumerate(ssp.RadarSpecifications):
            for iradar,specifications in enumerate(radarSpecifications):
              global_location_TX,global_location_RX,global_location_Center = specifications['global_location_TX_RX_Center']

              R = np.linalg.norm(p0-global_location_Center)

              n = (p0-global_location_Center)/R
              fd = 2*v0.dot(n)/specifications['Lambda']

              rangeDopplerTXRX,d_fft,f_Doppler = RangeDopplerDistributed[isuite][iradar]

              indices = find_indices_within_distance(d_fft,R,1*np.sqrt(3)*gridlen)
              if indices.shape[0]==0:
                continue
              DopplerTXRX=rangeDopplerTXRX[indices,:,:,:]
              if 1:
                DopplerTXRX=np.mean(DopplerTXRX,axis=0)
              else:
                # max over axe 0
                DopplerTXRX=np.mean(DopplerTXRX,axis=0)

              indices_fd = find_indices_within_distance(f_Doppler,fd,2*gridvlen/specifications['Lambda'])

              if indices_fd.shape[0]==0:
                continue


              TXRX=DopplerTXRX[indices_fd,:,:]
              TXRX=np.mean(TXRX,axis=0)
              sv = 0*TXRX
              for itx , txPos in enumerate(global_location_TX):
                dtx = np.linalg.norm(p0-txPos)
                for irx , rxPos in enumerate(global_location_RX):
                  drx = np.linalg.norm(p0-rxPos)
                  sv[itx,irx]=np.exp(1j*2*np.pi/specifications['Lambda']*(dtx+drx))

              TXRX_vectorized = TXRX.reshape(-1, 1)
              sv_vectorized = sv.reshape(-1, 1)

              Guard_Len = 4
              Wing_Len = 2*sv.shape[0]*sv.shape[1]
              Complementary_indices_fd = CFAR_Window_Selection_F(f_Doppler.shape[0],indices_fd,Guard_Len,Wing_Len)

              Guard_Len_Range = 4
              Wing_Len_Range = 2*sv.shape[0]*sv.shape[1]
              Complementary_indices_range = CFAR_Window_Selection_F(d_fft.shape[0],indices,Guard_Len_Range,Wing_Len_Range)

              Complementary_indices_range = indices # temporary
              SecondaryData_RD = rangeDopplerTXRX[Complementary_indices_range,:,:,:]
              SecondaryData_RD = SecondaryData_RD[:,Complementary_indices_fd,:,:]
              energies = []
              indices = []
              for isd in range(SecondaryData_RD.shape[0]):
                  for isd1 in range(SecondaryData_RD.shape[1]):
                      TXRX_k = SecondaryData_RD[isd, isd1, :, :]
                      TXRX_k_vectorized = TXRX_k.reshape(-1, 1)
                      energy = np.abs(np.conj(TXRX_k_vectorized).T @ TXRX_k_vectorized)
                      energies.append(energy[0][0])
                      indices.append((isd, isd1))
              energies_array = np.array(energies)
              sorted_indices = np.argsort(energies_array)
              sorted_energies = energies_array[sorted_indices]
              sorted_indices_pairs = [indices[idx] for idx in sorted_indices]
              num_OSCFAR = int(0.7 * len(sorted_indices_pairs))
              Ntx = SecondaryData_RD.shape[2]
              Nrx = SecondaryData_RD.shape[3]
              print(num_OSCFAR,Ntx * Nrx)
              if 0:
                sum_matrix = np.zeros((Ntx * Nrx, Ntx * Nrx), dtype=SecondaryData_RD.dtype)
                for i in range(num_OSCFAR):
                    isd, isd1 = sorted_indices_pairs[i]
                    TXRX_k = SecondaryData_RD[isd, isd1, :, :]
                    TXRX_k_vectorized = TXRX_k.reshape(-1, 1)
                    product_matrix = TXRX_k_vectorized @ np.conj(TXRX_k_vectorized).T
                    sum_matrix += product_matrix

                Gamma_inv = np.linalg.pinv(sum_matrix)
              else:
                sum_en = 0
                for i in range(num_OSCFAR):
                    sum_en += sorted_energies[i]
                Gamma_inv = Ntx * Nrx / sum_en * np.eye(Ntx * Nrx, dtype=SecondaryData_RD.dtype)

              Kelly_num = np.abs(np.conj(sv_vectorized).T @ Gamma_inv @ TXRX_vectorized)[0][0]**2/np.abs(np.conj(sv_vectorized).T @ Gamma_inv @ sv_vectorized)[0][0]
              Kelly_denum = np.abs(np.conj(TXRX_vectorized).T @ Gamma_inv @ TXRX_vectorized)[0][0]
              # print(Kelly_num,Kelly_denum)
              Detection_data.append([Kelly_num,Kelly_denum])
          KellyNum = 0
          KellyDeNum = 1
          for idet,detdata in enumerate(Detection_data):
            Kelly_num,Kelly_denum = detdata
            KellyNum += Kelly_num
            KellyDeNum += Kelly_denum
          Kelly = KellyNum / KellyDeNum
          all_outputs.append(Kelly)

      return grid_points , grid_velocities , all_outputs
def SensorsSignalProccessing_Angle(Signals):
  RangeDopplerDistributed = []
  for isuite,radarSpecifications in enumerate(ssp.RadarSpecifications):
      RangeDopplerDistributed0 = []
      All_RangeResolutions = []
      for iradar,specifications in enumerate(radarSpecifications):
        XRadar = Signals[isuite]['radars'][iradar]
        FMCW_ChirpSlobe = specifications['FMCW_ChirpSlobe']
        Ts = specifications['Ts']
        PRI = specifications['PRI']
        Lambda = specifications['Lambda']
        PrecodingMatrix = specifications['PrecodingMatrix']
        
        RadarMode = specifications['RadarMode']

        All_RangeResolutions.append( LightSpeed/2/specifications['FMCW_Bandwidth'] )

        fast_time_window = scipy.signal.windows.hamming(XRadar.shape[0])
        X_windowed_fast = XRadar * fast_time_window[:, np.newaxis, np.newaxis]

        if RadarMode == 'Pulse':
          waveform_MF = specifications['PulseWaveform_Loaded']
          matched_filter = np.conj(waveform_MF[::-1])
          X_fft_fast = np.apply_along_axis(lambda x: np.convolve(x, matched_filter, mode='full'), axis=0, arr=X_windowed_fast)
          X_fft_fast=X_fft_fast[matched_filter.shape[0]-1:,:,:]
          d_fft = np.arange(X_fft_fast.shape[0]) * LightSpeed * Ts /2
          
        else:
          NFFT_Range_OverNextPow2 =  specifications['RangeFFT_OverNextP2']
          NFFT_Range = int(2 ** (np.ceil(np.log2(XRadar.shape[0]))+NFFT_Range_OverNextPow2))
          X_fft_fast = np.fft.fft(X_windowed_fast, axis=0, n=NFFT_Range)  # beat freq = Slobe * 2 * d / c =   ind / nfft * Fs ->
          d_fft = np.arange(NFFT_Range) * LightSpeed / 2 / FMCW_ChirpSlobe / NFFT_Range / Ts
        Range_Start = specifications['Range_Start']
        Range_End = specifications['Range_End']
        d1i = int(X_fft_fast.shape[0]*Range_Start/100.0)
        d2i = int(X_fft_fast.shape[0]*Range_End/100.0)
        d_fft = d_fft[d1i:d2i]
        X_fft_fast = X_fft_fast[d1i:d2i,:,:] #(67 Range, 96 Pulse, 4 RX)

        # print("XRadar shape:", XRadar.shape)
        # XRadar shape: (128, 192, 16)

        M_TX=PrecodingMatrix.shape[1]#specifications['M_TX']
        L = X_fft_fast.shape[1]
        Leff = int(L/M_TX)
        
        if ssp.config.DopplerProcessingMethod_FFT_Winv:
          # slow_time_window = scipy.signal.windows.hamming(X_fft_fast.shape[1])
          # X_windowed_slow = X_fft_fast * slow_time_window[np.newaxis,:,np.newaxis,np.newaxis]
          N_Doppler = Leff
          f_Doppler = np.hstack((np.linspace(-0.5/PRI/M_TX, 0, N_Doppler)[:-1], np.linspace(0, 0.5/PRI/M_TX, N_Doppler)))

          PrecodingMatrixInv = np.linalg.pinv(PrecodingMatrix)

          rangeDopplerTXRX = np.zeros((X_fft_fast.shape[0], f_Doppler.shape[0], M_TX, X_fft_fast.shape[2]),dtype=complex)
          for idop , f_Doppler_i in enumerate(f_Doppler):
            dopplerSteeringVector = np.exp(1j*2*np.pi*f_Doppler_i*np.arange(L)*PRI)
            X_doppler_comp = X_fft_fast * np.conj(dopplerSteeringVector[np.newaxis,:,np.newaxis])
            rangeTXRX = np.einsum('ijk,lj->ilk', X_doppler_comp, PrecodingMatrixInv)
            rangeDopplerTXRX[:, idop, :, :] = rangeTXRX
        else:
          rangePulseTXRX = np.zeros((X_fft_fast.shape[0], Leff, M_TX, X_fft_fast.shape[2]),dtype=complex)
          for ipulse in range(Leff):
            ind = ipulse*M_TX
            rangePulseTXRX[:,ipulse,:,:]=X_fft_fast[:,ind:ind+M_TX,:]
          NFFT_Doppler_OverNextPow2=0
          NFFT_Doppler = int(2 ** (np.ceil(np.log2(Leff))+NFFT_Doppler_OverNextPow2))
          rangeDopplerTXRX = np.fft.fft(rangePulseTXRX, axis=1, n=NFFT_Doppler)
          rangeDopplerTXRX = np.fft.fftshift(rangeDopplerTXRX,axes=1)
          f_Doppler = np.linspace(0,1/PRI/M_TX,NFFT_Doppler)
            
            
        global_location_TX,global_location_RX,global_location_Center = specifications['global_location_TX_RX_Center']
        if len(global_location_TX)+len(global_location_RX)==2:
          ssp.config.ax[0,1].cla()
          ssp.config.ax[0,2].cla()
          ssp.config.ax[0,1].plot(np.real(XRadar[:,0,0]))
          ssp.config.ax[0,2].plot(np.abs(X_fft_fast[:,0,0]))
          
          plt.draw() 
          plt.pause(0.1)
          continue
        
        # RangeAngleMapCalc
        PosIndex = np.array(specifications['Local_location_TXplusRX_Center'])
        azimuths = PosIndex[:, 0]
        elevations = PosIndex[:, 1]
        
        d_az = np.max(azimuths)-np.min(azimuths)
        d_el = np.max(elevations)-np.min(elevations)
        if d_az>d_el:
          sorted_indices = np.argsort(azimuths)
          sorted_PosIndex = PosIndex[sorted_indices,:]
          sorted_PosIndex[:,0]-=sorted_PosIndex[0,0]
          sorted_PosIndex[:,1]-=sorted_PosIndex[0,1]
          sorted_PosIndex[:,0]=np.round(sorted_PosIndex[:,0])
          sorted_PosIndex[:,1]=np.round(sorted_PosIndex[:,1])

          unique_azimuths, unique_indices = np.unique(sorted_PosIndex[:, 0], return_index=True)
          unique_PosIndex = sorted_PosIndex[unique_indices,:]

          # print(unique_PosIndex)



        if 0:
          rangeTXRX = np.mean(rangeDopplerTXRX,axis=1)
        else:
          rangeTXRX = np.zeros((rangeDopplerTXRX.shape[0],rangeDopplerTXRX.shape[2],rangeDopplerTXRX.shape[3]),dtype=rangeDopplerTXRX.dtype)
          rangeDoppler4CFAR = np.mean(np.abs(rangeDopplerTXRX),axis=(2,3))
          ssp.config.ax[1,0].imshow(rangeDoppler4CFAR, aspect='auto')
          ssp.config.ax[1,0].set_title("Range Doppler abs(mean) (CFAR)")
          ssp.config.ax[1,0].set_xlabel('Doppler')
          ssp.config.ax[1,0].set_ylabel('Range')
          for irange in range(rangeDoppler4CFAR.shape[0]):
            doppler_ind = np.argmax(rangeDoppler4CFAR[irange])
            rangeTXRX[irange,:,:]=rangeDopplerTXRX[irange,doppler_ind,:,:]

        # Selected_ind = [(0,0), (1,7), (2,6), (11,15)]
        # rows, cols = zip(*Selected_ind)
        
        rows = unique_PosIndex[:,2].astype(int)
        cols = unique_PosIndex[:,3].astype(int)
        # print(rows)
        # print(cols)
        rangeVA = rangeTXRX[:, rows, cols]
        angle_window = scipy.signal.windows.hamming(rangeVA.shape[1])
        X_windowed_rangeVA = rangeVA * angle_window[np.newaxis,:]
        
        # Bartlet Angle 
        # Capon
        
        NFFT_Angle_OverNextPow2 =  1
        NFFT_Angle = int(2 ** (np.ceil(np.log2(X_windowed_rangeVA.shape[1]))+NFFT_Angle_OverNextPow2))
        RangeAngleMap = np.fft.fft(X_windowed_rangeVA, axis=1, n=NFFT_Angle)  # beat freq = Slobe * 2 * d / c =   ind / nfft * Fs ->
        RangeAngleMap = np.fft.fftshift(RangeAngleMap, axes=1)
        # sina_fft = np.rad2deg(np.arcsin(np.linspace(-1,1,NFFT_AngleNFFT_Angle)))
        extent = [-.5 ,.5,d_fft[-1],d_fft[0]]
        ssp.config.ax[1,1].imshow(np.abs(RangeAngleMap), extent=extent, aspect='auto')
        ssp.config.ax[1,1].set_xlabel('sin(az)')
        ssp.config.ax[1,1].set_ylabel('Range (m)')
        ssp.config.ax[1,1].set_title("Bartlet Beamformer")
        ssp.config.ax[0,1].cla()
        ssp.config.ax[0,2].cla()
        ssp.config.ax[0,1].plot(np.real(Signals[isuite]['radars'][iradar][:,0,0]))
        ssp.config.ax[0,2].plot(np.abs(np.fft.fft(Signals[isuite]['radars'][iradar][:,0,0])))
        
        ssp.config.ax[0,0].cla()
        for __ in ssp.lastScatterInfo[ssp.config.CurrentFrame-bpy.context.scene.frame_start]:
          _=__[0]
          ssp.config.ax[0,0].scatter(_[0],_[1],c='k',marker='x',s=20)
          # ssp.config.ax[2,2].scatter(_[0],_[1],_[2],c='k',marker='x',s=20)
        global_location_TX,global_location_RX,global_location_Center = specifications['global_location_TX_RX_Center']
        for _ in global_location_TX:
          ssp.config.ax[0,0].scatter(_[0],_[1],c='r',marker='x')
          # ssp.config.ax[2,2].scatter(_[0],_[1],_[2],c='r',marker='x')
        for _ in global_location_RX:
          ssp.config.ax[0,0].scatter(_[0],_[1],c='b',marker='x')
          # ssp.config.ax[2,2].scatter(_[0],_[1],_[2],c='b',marker='x')
          
        ssp.config.ax[2,2].cla()
        for __ in ssp.lastScatterInfo[ssp.config.CurrentFrame-bpy.context.scene.frame_start]:
          _=__[0]
          ssp.config.ax[2,2].scatter(_[0],_[1],_[2],c='k',marker='x',s=20)
        global_location_TX,global_location_RX,global_location_Center = specifications['global_location_TX_RX_Center']
        for _ in global_location_TX:
          ssp.config.ax[2,2].scatter(_[0],_[1],_[2],c='r',marker='x')
        for _ in global_location_RX:
          ssp.config.ax[2,2].scatter(_[0],_[1],_[2],c='b',marker='x')
          
        
        ssp.config.ax[0,1].set_xlabel('ADC sample')
        ssp.config.ax[0,1].set_ylabel('Amp')
        ssp.config.ax[0,1].set_title("ADC")
        ssp.config.ax[0,2].set_xlabel('Range')
        ssp.config.ax[0,2].set_ylabel('Amp')
        ssp.config.ax[0,2].set_title("Range FFT")
                
        
        plt.draw()  # Redraw the figure
        plt.pause(0.1)
        
        RangeDopplerDistributed0.append([rangeDopplerTXRX,d_fft,f_Doppler])
      RangeDopplerDistributed.append(RangeDopplerDistributed0)

      for icam in range(len(Signals[isuite]['cameras'])):
        ssp.config.ax[2,0].imshow(Signals[isuite]['cameras'][icam])
        plt.draw() 
        plt.pause(0.1)
        break
      
      ssp.config.ax[2,1].cla()
      for ilid in range(len(Signals[isuite]['lidars'])):
        pc = Signals[isuite]['lidars'][ilid]
        if pc.shape[0]==0:
          continue
        ssp.config.ax[2,1].scatter(pc[:,0],pc[:,1],pc[:,2])
        plt.draw() 
        plt.pause(0.1)
        break
  
  Triangles = ssp.utils.exportBlenderTriangles()
  for _ in Triangles:
      for __ in _:
          i,j=0,1
          ssp.config.ax[2,1].plot([__[i][0],__[j][0]],[__[i][1],__[j][1]],[__[i][2],__[j][2]])
          i,j=0,2
          ssp.config.ax[2,1].plot([__[i][0],__[j][0]],[__[i][1],__[j][1]],[__[i][2],__[j][2]])
          i,j=2,1
          ssp.config.ax[2,1].plot([__[i][0],__[j][0]],[__[i][1],__[j][1]],[__[i][2],__[j][2]])      
  plt.draw()  # Redraw the figure
  plt.pause(0.1)
def SensorsSignalProccessing_Angle_frame(Signals):
  RangeDopplerDistributed = []
  for isuite,radarSpecifications in enumerate(ssp.RadarSpecifications):
      RangeDopplerDistributed0 = []
      All_RangeResolutions = []
      for iradar,specifications in enumerate(radarSpecifications):
        XRadar = Signals[isuite]['radars'][iradar]
        FMCW_ChirpSlobe = specifications['FMCW_ChirpSlobe']
        Ts = specifications['Ts']
        PRI = specifications['PRI']
        Lambda = specifications['Lambda']
        PrecodingMatrix = specifications['PrecodingMatrix']
        
        RadarMode = specifications['RadarMode']

        All_RangeResolutions.append( LightSpeed/2/specifications['FMCW_Bandwidth'] )

        fast_time_window = scipy.signal.windows.hamming(XRadar.shape[0])
        X_windowed_fast = XRadar * fast_time_window[:, np.newaxis, np.newaxis]

        if RadarMode == 'Pulse':
          waveform_MF = specifications['PulseWaveform_Loaded']
          matched_filter = np.conj(waveform_MF[::-1])
          X_fft_fast = np.apply_along_axis(lambda x: np.convolve(x, matched_filter, mode='full'), axis=0, arr=X_windowed_fast)
          X_fft_fast=X_fft_fast[matched_filter.shape[0]-1:,:,:]
          d_fft = np.arange(X_fft_fast.shape[0]) * LightSpeed * Ts /2
          
        else:
          NFFT_Range_OverNextPow2 =  specifications['RangeFFT_OverNextP2']
          NFFT_Range = int(2 ** (np.ceil(np.log2(XRadar.shape[0]))+NFFT_Range_OverNextPow2))
          X_fft_fast = np.fft.fft(X_windowed_fast, axis=0, n=NFFT_Range)  # beat freq = Slobe * 2 * d / c =   ind / nfft * Fs ->
          d_fft = np.arange(NFFT_Range) * LightSpeed / 2 / FMCW_ChirpSlobe / NFFT_Range / Ts
        Range_Start = specifications['Range_Start']
        Range_End = specifications['Range_End']
        d1i = int(X_fft_fast.shape[0]*Range_Start/100.0)
        d2i = int(X_fft_fast.shape[0]*Range_End/100.0)
        d_fft = d_fft[d1i:d2i]
        X_fft_fast = X_fft_fast[d1i:d2i,:,:] #(67 Range, 96 Pulse, 4 RX)

        # print("XRadar shape:", XRadar.shape)
        # XRadar shape: (128, 192, 16)

        M_TX=PrecodingMatrix.shape[1]#specifications['M_TX']
        L = X_fft_fast.shape[1]
        Leff = int(L/M_TX)
        
        if ssp.config.DopplerProcessingMethod_FFT_Winv:
          # slow_time_window = scipy.signal.windows.hamming(X_fft_fast.shape[1])
          # X_windowed_slow = X_fft_fast * slow_time_window[np.newaxis,:,np.newaxis,np.newaxis]
          N_Doppler = Leff
          f_Doppler = np.hstack((np.linspace(-0.5/PRI/M_TX, 0, N_Doppler)[:-1], np.linspace(0, 0.5/PRI/M_TX, N_Doppler)))

          PrecodingMatrixInv = np.linalg.pinv(PrecodingMatrix)

          rangeDopplerTXRX = np.zeros((X_fft_fast.shape[0], f_Doppler.shape[0], M_TX, X_fft_fast.shape[2]),dtype=complex)
          for idop , f_Doppler_i in enumerate(f_Doppler):
            dopplerSteeringVector = np.exp(1j*2*np.pi*f_Doppler_i*np.arange(L)*PRI)
            X_doppler_comp = X_fft_fast * np.conj(dopplerSteeringVector[np.newaxis,:,np.newaxis])
            rangeTXRX = np.einsum('ijk,lj->ilk', X_doppler_comp, PrecodingMatrixInv)
            rangeDopplerTXRX[:, idop, :, :] = rangeTXRX
        else:
          rangePulseTXRX = np.zeros((X_fft_fast.shape[0], Leff, M_TX, X_fft_fast.shape[2]),dtype=complex)
          for ipulse in range(Leff):
            ind = ipulse*M_TX
            rangePulseTXRX[:,ipulse,:,:]=X_fft_fast[:,ind:ind+M_TX,:]
          NFFT_Doppler_OverNextPow2=0
          NFFT_Doppler = int(2 ** (np.ceil(np.log2(Leff))+NFFT_Doppler_OverNextPow2))
          rangeDopplerTXRX = np.fft.fft(rangePulseTXRX, axis=1, n=NFFT_Doppler)
          rangeDopplerTXRX = np.fft.fftshift(rangeDopplerTXRX,axes=1)
          f_Doppler = np.linspace(0,1/PRI/M_TX,NFFT_Doppler)
            
            
        global_location_TX,global_location_RX,global_location_Center = specifications['global_location_TX_RX_Center']
        if len(global_location_TX)+len(global_location_RX)==2:
          ssp.config.ax[0,1].cla()
          ssp.config.ax[0,2].cla()
          ssp.config.ax[0,1].plot(np.real(XRadar[:,0,0]))
          ssp.config.ax[0,2].plot(np.abs(X_fft_fast[:,0,0]))
          
          plt.draw() 
          plt.pause(0.1)
          continue
        
        # RangeAngleMapCalc
        PosIndex = np.array(specifications['Local_location_TXplusRX_Center'])
        azimuths = PosIndex[:, 0]
        elevations = PosIndex[:, 1]
        
        d_az = np.max(azimuths)-np.min(azimuths)
        d_el = np.max(elevations)-np.min(elevations)
        if d_az>d_el:
          sorted_indices = np.argsort(azimuths)
          sorted_PosIndex = PosIndex[sorted_indices,:]
          sorted_PosIndex[:,0]-=sorted_PosIndex[0,0]
          sorted_PosIndex[:,1]-=sorted_PosIndex[0,1]
          sorted_PosIndex[:,0]=np.round(sorted_PosIndex[:,0])
          sorted_PosIndex[:,1]=np.round(sorted_PosIndex[:,1])

          unique_azimuths, unique_indices = np.unique(sorted_PosIndex[:, 0], return_index=True)
          unique_PosIndex = sorted_PosIndex[unique_indices,:]

          # print(unique_PosIndex)



        if 0:
          rangeTXRX = np.mean(rangeDopplerTXRX,axis=1)
        else:
          rangeTXRX = np.zeros((rangeDopplerTXRX.shape[0],rangeDopplerTXRX.shape[2],rangeDopplerTXRX.shape[3]),dtype=rangeDopplerTXRX.dtype)
          rangeDoppler4CFAR = np.mean(np.abs(rangeDopplerTXRX),axis=(2,3))
          ssp.config.ax[1,0].imshow(rangeDoppler4CFAR, aspect='auto')
          ssp.config.ax[1,0].set_title("Range Doppler abs(mean) (CFAR)")
          ssp.config.ax[1,0].set_xlabel('Doppler')
          ssp.config.ax[1,0].set_ylabel('Range')
          for irange in range(rangeDoppler4CFAR.shape[0]):
            doppler_ind = np.argmax(rangeDoppler4CFAR[irange])
            rangeTXRX[irange,:,:]=rangeDopplerTXRX[irange,doppler_ind,:,:]

        # Selected_ind = [(0,0), (1,7), (2,6), (11,15)]
        # rows, cols = zip(*Selected_ind)
        
        rows = unique_PosIndex[:,2].astype(int)
        cols = unique_PosIndex[:,3].astype(int)
        # print(rows)
        # print(cols)
        rangeVA = rangeTXRX[:, rows, cols]
        angle_window = scipy.signal.windows.hamming(rangeVA.shape[1])
        X_windowed_rangeVA = rangeVA * angle_window[np.newaxis,:]
        
        # Bartlet Angle 
        # Capon
        
        NFFT_Angle_OverNextPow2 =  1
        NFFT_Angle = int(2 ** (np.ceil(np.log2(X_windowed_rangeVA.shape[1]))+NFFT_Angle_OverNextPow2))
        RangeAngleMap = np.fft.fft(X_windowed_rangeVA, axis=1, n=NFFT_Angle)  # beat freq = Slobe * 2 * d / c =   ind / nfft * Fs ->
        RangeAngleMap = np.fft.fftshift(RangeAngleMap, axes=1)
        # sina_fft = np.rad2deg(np.arcsin(np.linspace(-1,1,NFFT_AngleNFFT_Angle)))
        extent = [-.5 ,.5,d_fft[-1],d_fft[0]]
        ssp.config.ax[1,1].imshow(np.abs(RangeAngleMap), extent=extent, aspect='auto')
        ssp.config.ax[1,1].set_xlabel('sin(az)')
        ssp.config.ax[1,1].set_ylabel('Range (m)')
        ssp.config.ax[1,1].set_title("Bartlet Beamformer")
        if iradar==0:
          polar_range_angle(RangeAngleMap,d_fft,np.linspace(-np.pi/2, np.pi/2, NFFT_Angle),ssp.config.ax[1,2])
        else:
          polar_range_angle(RangeAngleMap,d_fft,np.linspace(-np.pi/2, np.pi/2, NFFT_Angle),ssp.config.ax[2,0])
        # ssp.config.ax[1,1].set_xlabel('sin(az)')
        # ssp.config.ax[1,1].set_ylabel('Range (m)')
        # ssp.config.ax[1,1].set_title("Bartlet Beamformer")
        
        ssp.config.ax[0,1].cla()
        ssp.config.ax[0,2].cla()
        ssp.config.ax[0,1].plot(np.real(Signals[isuite]['radars'][iradar][:,0,0]))
        ssp.config.ax[0,2].plot(np.abs(np.fft.fft(Signals[isuite]['radars'][iradar][:,0,0])))
        
        
        
        ssp.config.ax[0,0].cla()
        for __ in ssp.lastScatterInfo:
          _=__[0]
          ssp.config.ax[0,0].scatter(_[0],_[1],c='k',marker='x',s=20)
          # ssp.config.ax[2,2].scatter(_[0],_[1],_[2],c='k',marker='x',s=20)
        global_location_TX,global_location_RX,global_location_Center = specifications['global_location_TX_RX_Center']
        for _ in global_location_TX:
          ssp.config.ax[0,0].scatter(_[0],_[1],c='r',marker='x')
          # ssp.config.ax[2,2].scatter(_[0],_[1],_[2],c='r',marker='x')
        for _ in global_location_RX:
          ssp.config.ax[0,0].scatter(_[0],_[1],c='b',marker='x')
          # ssp.config.ax[2,2].scatter(_[0],_[1],_[2],c='b',marker='x')
          
        ssp.config.ax[2,2].cla()
        for __ in ssp.lastScatterInfo:
          _=__[0]
          ssp.config.ax[2,2].scatter(_[0],_[1],_[2],c='k',marker='x',s=20)
        global_location_TX,global_location_RX,global_location_Center = specifications['global_location_TX_RX_Center']
        for _ in global_location_TX:
          ssp.config.ax[2,2].scatter(_[0],_[1],_[2],c='r',marker='x')
        for _ in global_location_RX:
          ssp.config.ax[2,2].scatter(_[0],_[1],_[2],c='b',marker='x')
          
        
        ssp.config.ax[0,1].set_xlabel('ADC sample')
        ssp.config.ax[0,1].set_ylabel('Amp')
        ssp.config.ax[0,1].set_title("ADC")
        ssp.config.ax[0,2].set_xlabel('Range')
        ssp.config.ax[0,2].set_ylabel('Amp')
        ssp.config.ax[0,2].set_title("Range FFT")
                
        
        plt.draw()  # Redraw the figure
        plt.pause(0.1)
        
        RangeDopplerDistributed0.append([rangeDopplerTXRX,d_fft,f_Doppler])
      RangeDopplerDistributed.append(RangeDopplerDistributed0)

      for icam in range(len(Signals[isuite]['cameras'])):
        ssp.config.ax[2,0].imshow(Signals[isuite]['cameras'][icam])
        plt.draw() 
        plt.pause(0.1)
        break
      
      ssp.config.ax[2,1].cla()
      for ilid in range(len(Signals[isuite]['lidars'])):
        pc = Signals[isuite]['lidars'][ilid]
        if pc.shape[0]==0:
          continue
        ssp.config.ax[2,1].scatter(pc[:,0],pc[:,1],pc[:,2])
        plt.draw() 
        plt.pause(0.1)
        break
  
  Triangles = ssp.utils.exportBlenderTriangles()
  for _ in Triangles:
      for __ in _:
          i,j=0,1
          ssp.config.ax[2,1].plot([__[i][0],__[j][0]],[__[i][1],__[j][1]],[__[i][2],__[j][2]])
          i,j=0,2
          ssp.config.ax[2,1].plot([__[i][0],__[j][0]],[__[i][1],__[j][1]],[__[i][2],__[j][2]])
          i,j=2,1
          ssp.config.ax[2,1].plot([__[i][0],__[j][0]],[__[i][1],__[j][1]],[__[i][2],__[j][2]])      
  plt.draw()  # Redraw the figure
  plt.pause(0.1)
        
        

def polar_range_angle(RangeAngleMap,ranges,angles,ax_polar_True):
    R, Theta = np.meshgrid(ranges, angles)
    # plt.figure()
    # ax = plt.subplot(111, polar=True)
    c = ax_polar_True.pcolormesh(Theta, R, (np.abs(RangeAngleMap).T), shading='auto')
    # c = ax_polar_True.pcolormesh(Theta, R, np.log10(np.abs(RangeAngleMap).T), shading='auto')
    ax_polar_True.set_thetalim(-np.pi/2, np.pi/2)
    ax_polar_True.set_ylim(0, ranges[-1]*.4)
    # plt.colorbar(c, label='Magnitude')
    # ax_polar_True.axis('off')
    # plt.show()
    # plt.subplots_adjust(left=0, right=1, top=1, bottom=0)