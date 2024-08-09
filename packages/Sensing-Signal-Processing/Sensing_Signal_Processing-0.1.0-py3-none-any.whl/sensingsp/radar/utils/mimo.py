import numpy as np
from scipy.linalg import hadamard
import scipy.special as sp
import scipy.stats as stats
import math




class MIMO_Functions:
  
  def sv(self,az,fd,W):
    NPulse=W.shape[0]
    M=W.shape[1]
    a=np.exp(1j*np.pi*np.arange(M)*np.sin(np.deg2rad(az)))
    d=np.exp(1j*2*np.pi*np.arange(NPulse)*fd)
    s = (W @ a)*d
    return s

  def plot_Angle_Doppler(self,W,st,ax):
    x = self.sv(20,0,W)
    azv = np.linspace(-90,90,100)
    fdv = np.linspace(-.5,.5,500)
    Im = np.zeros((azv.shape[0],fdv.shape[0]),dtype=np.float64)
    for i in range(azv.shape[0]):
      for j in range(fdv.shape[0]):
        Im[i,j] = (np.abs(np.conj(self.sv(azv[i],fdv[j],W)).T@x))
    im = ax.imshow(Im.T, extent=(-90, 90, -0.5, 0.5), aspect='auto', cmap='viridis')  # Added cmap for better color representation
    ax.set_title(st)
    cbar = plt.colorbar(im, ax=ax)
    # cbar.set_label('Log-Power (dB)')

  def AD_matrix(self,NPulse,M,tech='TDM'):
    W = np.zeros((NPulse,M),dtype=np.complex128)
    match tech:
      case "DDM":
        for p in range(NPulse):
          for m in range(M):
            W[p,m]=np.exp(1j*2*np.pi*m*p/M)
      case "DDM2":
        for p in range(NPulse):
          for m in range(M):
            W[p,m]=np.exp(1j*2*np.pi*m*p/NPulse)
      case "DDM_RandPhase":
        for p in range(NPulse):
          for m in range(M):
            W[p,m]=np.exp(1j*2*np.pi*np.random.rand())
      case "TDM":
        for p in range(NPulse):
          for m in range(M):
            W[p,m]=0
            if p%M == m:
              W[p,m]=1
      case "BPM":
        H = hadamard(M, dtype=complex)
        for p in range(NPulse):
          for m in range(M):
            W[p,m]=H[p%M,m]
      case _:
          print("Not Valid!")
    return W
  

def steeringVector_position(specifications,p0):
  global_location_TX,global_location_RX,global_location_Center = specifications['global_location_TX_RX_Center']
  sv = np.zeros((len(global_location_TX)*len(global_location_RX),1),dtype=complex)
  k=0
  for itx , txPos in enumerate(global_location_TX):
    dtx = np.linalg.norm(p0-txPos)
    for irx , rxPos in enumerate(global_location_RX):
      drx = np.linalg.norm(p0-rxPos)
      sv[k,0]=np.exp(1j*2*np.pi/specifications['Lambda']*(dtx+drx))
      k+=1
  return sv

def update_block_diag_matrix(Z, vec):
    if Z is None:
        return vec
    rowsZ, colsZ = Z.shape
    newZ = np.zeros((rowsZ + vec.shape[0], colsZ + vec.shape[1]),dtype=complex)
    newZ[:rowsZ, :colsZ] = Z
    newZ[rowsZ:, colsZ:] = vec
    return newZ

def Distributed_MIMO_steeringMatrix_position(RadarSpecifications,p0,allSuites=1):
  if allSuites==1:
    steeringMatrix = None
    for radarSpecifications in RadarSpecifications:
      for specifications in radarSpecifications:
        steeringMatrix = update_block_diag_matrix(steeringMatrix,steeringVector_position(specifications,p0))
    return steeringMatrix
  elif allSuites==2:
    steeringMatrix=[]
    for radarSpecifications in RadarSpecifications:
      steeringMatrix0 = None
      for specifications in radarSpecifications:
        steeringMatrix0 = update_block_diag_matrix(steeringMatrix,steeringVector_position(specifications,p0))
      steeringMatrix.append(steeringMatrix0)
    return steeringMatrix
  elif allSuites==3:
    steeringMatrix=[]
    for radarSpecifications in RadarSpecifications:
      for specifications in radarSpecifications:
        steeringMatrix.append(steeringVector_position(specifications,p0))
    return steeringMatrix
  
def generate_covariance_matrix(N, rho):
    covariance_matrix = np.zeros((N, N), dtype=complex)
    for i in range(N):
        for j in range(N):
            # covariance_matrix[i, j] = np.exp(-spread * abs(i - j))
            covariance_matrix[i, j] = (rho**abs(i - j))*np.exp(1j* np.pi/2 *(i - j))
    return covariance_matrix
  
def generate_complex_gaussian_samples(cholesky_covariance_matrix, K):
    N = cholesky_covariance_matrix.shape[0]
    real_part = np.random.randn(N, K)
    imag_part = np.random.randn(N, K)
    Z = (real_part + 1j * imag_part) / np.sqrt(2)
    samples = cholesky_covariance_matrix @ Z
    return samples

def pfaTHR_tH0(tH0,pfa_v):
  N_MC = tH0.shape[0]
  detector_THR = tH0[tH0.argsort()]
  indices = []
  Pfa_THR  = []
  for pfai in pfa_v:
      ind = round((1 - pfai) * (N_MC - 1))
      if ind not in indices:
          indices.append(ind)
          THR = detector_THR[ind]
          pfa = np.sum(tH0>THR)/N_MC
          Pfa_THR.append([pfa,THR])
  return np.array(Pfa_THR)

def ROC_tH1H0(tH0H1,pfa_v):
    N_MC = tH0H1.shape[0]
    detector_THR = tH0H1[:, 0]   
    detector_THR = detector_THR[detector_THR.argsort()]
    indices = []
    Pd_Pfa_THR  = []
    for pfai in pfa_v:
        ind = round((1 - pfai) * (N_MC - 1))
        if ind not in indices:
            indices.append(ind)
            THR = detector_THR[ind]
            pfa = np.sum(tH0H1[:, 0]>THR)/N_MC
            pd  = np.sum(tH0H1[:, 1]>THR)/N_MC
            Pd_Pfa_THR.append([pd,pfa,THR])
    return np.array(Pd_Pfa_THR)
  
def ROC_tH1(tH1,pfa_v,THR_v):
    Pd_Pfa  = []
    for i in range(pfa_v.shape[0]):
        pd  = np.sum(tH1>THR_v[i])/tH1.shape[0]
        Pd_Pfa.append([pd,pfa_v[i]])
    return np.array(Pd_Pfa)

def array_detector_ABC(A,B,C):
  return A@B@C

def array_detector_ABC_inv(A,B,C):
  return np.linalg.pinv(array_detector_ABC(A,B,C))

def array_detector_Hermitian(A):
  return np.conj(A.T)

## MF
def array_detector_MF(x,Rinv,S):
  v = array_detector_ABC(array_detector_Hermitian(S),Rinv,x)
  A = array_detector_ABC(array_detector_Hermitian(S),Rinv,S)
  A = np.linalg.pinv(A)
  t = array_detector_ABC(array_detector_Hermitian(v),A,v)[0,0]
  return np.abs(t)

def MF_pfa(Q , threshold):
    P_fa = 1-stats.chi2.cdf(threshold*2, 2*Q)
    # P_fa = np.exp(-threshold) * sum((threshold**q) / math.factorial(q) for q in range(Q))
    return P_fa

def MF_threshold(Q,pfa):
  return stats.chi2.ppf(1 - pfa, 2 * Q) / 2

def MF_pd(Q , threshold,SCINR_Post):
  # term1 = np.sqrt(2 * SCINR_Post)
  # term2 = np.sqrt(2 * threshold)
  # non_centrality = term1**2
  # Pd = 1 - stats.ncx2.cdf(term2, 2*Q, non_centrality)
  # return Pd
  return 1-stats.ncx2.cdf(x=2 * threshold,df=2*Q,nc=2 * SCINR_Post)
    # P_d_value = sp.marcumq(Q, np.sqrt(2 * SCINR_Post), np.sqrt(2 * threshold))
    # return P_d_value

def array_detector_EstimatedAmplitude(x,Rinv,S):
  v = array_detector_ABC(array_detector_Hermitian(S),Rinv,x)
  A = array_detector_ABC(array_detector_Hermitian(S),Rinv,S)
  return np.linalg.pinv(A)@v

def array_detector_ED(x,Rinv):
  t = array_detector_ABC(array_detector_Hermitian(x),Rinv,x)[0,0]
  return np.abs(t)

def ED_pfa(Q , threshold):
    P_fa = 1-stats.chi2.cdf(threshold*2, 2*Q)
    # P_fa = np.exp(-threshold) * sum((threshold**q) / math.factorial(q) for q in range(Q))
    return P_fa

def array_detector_ACE(x,Rinv,S):
  return array_detector_MF(x,Rinv,S)/array_detector_ED(x,Rinv)

## Kelly
def array_detector_Kelly(x,Rinv,S):
  return array_detector_MF(x,Rinv,S)/(1+array_detector_ED(x,Rinv))

def Kelly_pfa(Q, NSD, NDim, threshold):
    P_fa = 1 - sp.betainc(Q, NSD - NDim + 1, threshold)
    return P_fa

def Kelly_threshold(Q, NSD, NDim,pfa):
  return sp.betaincinv(Q, NSD - NDim + 1, 1 - pfa)

def Kelly_DistributedIndependentSameRadars_pfa(Q, NSDi, NDimi, threshold):
    P_fa = 0
    for q in range(Q):
      P_fa += (NSDi-NDimi+1)**q / math.factorial(q) * (np.log(threshold)**q)
    P_fa *= threshold ** (-(NSDi-NDimi+1))
    return P_fa

def array_detector_Rao(x,R,S):
  Rinv = np.linalg.pinv(R+array_detector_Hermitian(x)@x)
  v = array_detector_ABC(array_detector_Hermitian(S),Rinv,x)
  A = array_detector_ABC(array_detector_Hermitian(S),Rinv,S)
  A = np.linalg.pinv(A)
  t = array_detector_ABC(array_detector_Hermitian(v),A,v)[0,0]
  return np.abs(t)

def array_detector_MMED(R):
  eigenvalues = np.linalg.eigvals(R)
  return np.abs(np.max(eigenvalues)/np.min(eigenvalues))

def array_detector_MED(x,R):
  eigenvalues = np.linalg.eigvals(R)
  e = array_detector_Hermitian(x)@x
  return np.abs( e[0,0] / np.min(eigenvalues))

def array_detector_RankOne_SingleShot(X):
  R = X @ array_detector_Hermitian(X)
  eigenvalues = np.linalg.eigvals(R)
  return np.abs( np.max(eigenvalues) / np.trace(R))

def array_detector_SCM_N(X):
  return X @ array_detector_Hermitian(X)

def array_detector_cos2(S,Sp,Rinv):
  A = array_detector_ABC(array_detector_Hermitian(S),Rinv,S)
  B = array_detector_ABC(array_detector_Hermitian(S),Rinv,Sp)
  BhAinvB = array_detector_ABC(array_detector_Hermitian(B),np.linalg.pinv(A),B)
  C = array_detector_ABC(array_detector_Hermitian(Sp),Rinv,Sp)
  ones = np.ones((S.shape[1],1))
  num = array_detector_Hermitian(ones) @ BhAinvB @ ones
  denum = array_detector_Hermitian(ones) @ C @ ones 
  return np.abs(num[0,0]/denum[0,0])

def array_detector_SINR(S,alpha,Rinv):
  A = array_detector_ABC(array_detector_Hermitian(S),Rinv,S)
  SINR = array_detector_ABC(array_detector_Hermitian(alpha),A,alpha)
  return np.abs(SINR[0,0])

def array_detector_AMFDeemphasis(x,R,S,eps_AMFD):
  Rinv = np.linalg.pinv(R+eps_AMFD*array_detector_Hermitian(x)@x)
  v = array_detector_ABC(array_detector_Hermitian(S),Rinv,x)
  A = array_detector_ABC(array_detector_Hermitian(S),Rinv,S)
  A = np.linalg.pinv(A)
  t = array_detector_ABC(array_detector_Hermitian(v),A,v)[0,0]
  return np.abs(t)

def array_detector_Kalson(x,Rinv,S,eps_Kalson):
  return array_detector_MF(x,Rinv,S)/(1+eps_Kalson*array_detector_ED(x,Rinv))

def array_detector_SD(x,Rinv,H): # [50, 51]
  return array_detector_Kelly(x,Rinv,H)

def array_detector_ABORT(x,Rinv,S):
  return (1+array_detector_MF(x,Rinv,S))/(2+array_detector_ED(x,Rinv))

def array_detector_WABORT(x,Rinv,S):
  t = (1-array_detector_Kelly(x,Rinv,S))**2
  A = array_detector_ABC(array_detector_Hermitian(S),Rinv,S)
  ones = np.ones((S.shape[1],1))
  a = np.abs(denum = array_detector_Hermitian(ones) @ A @ ones)[0,0] # Not sure
  return 1 / ((1+a)*t)

def array_detector_CAD(x,Rinv,S,eps_CAD):
  uv = array_detector_ED(x,Rinv) - array_detector_ED(x,Rinv)*(1+eps_CAD**2) # check [41, 58]
  u = 1 if uv >= 0 else 0
  t = array_detector_ED(x,Rinv) - 1/(1-eps_CAD**2)*(np.sqrt(array_detector_ED(x,Rinv)-array_detector_MF(x,Rinv,S))-eps_CAD*np.sqrt(array_detector_MF(x,Rinv,S)))**2 * u  
  return t


def array_detector_CARD(x,Rinv,S,eps_CARD):
  uv = eps_CARD * np.sqrt(array_detector_MF(x,Rinv,S))-np.sqrt(array_detector_ED(x,Rinv)-array_detector_MF(x,Rinv,S))
  u = 1 if uv >= 0 else -1
  return u * uv**2

def array_detector_2SROB(x,Rinv,S,N,K):
  p = array_detector_ED(x,Rinv)-array_detector_MF(x,Rinv,S)
  THR = N/K  # K > 2N
  if p>THR:
    return (THR/p)**THR * np.exp(-THR+array_detector_ED(x,Rinv))
  else:
    return np.exp(array_detector_MF(x,Rinv,S))

def array_detector_1SROB(x,Rinv,S,zeta):
  e = array_detector_ED(x,Rinv)
  p = e - array_detector_MF(x,Rinv,S)
  g = 1 + p
  if p >= 1/(zeta-1):
    Delta = (zeta-1)**(1/zeta) / (1-1/zeta)
    g = (1+Delta) * ( p ** (1/zeta) )
  return (1+e)/g

def array_detector_ROB(x,Rinv,S,zetaeps):
  p = array_detector_ED(x,Rinv)-array_detector_MF(x,Rinv,S)
  xh2 = array_detector_ED(x,Rinv)
  THR = 1/(zetaeps-1)
  if p>THR:
    return ( (1+xh2) * (1-1/zetaeps) ) / ( ((zetaeps-1)*p)**(1/zetaeps) )
  else:
    return (1+xh2)/(1+p)
