import numpy as np
import matplotlib.pyplot as plt
from rtlsdr import RtlSdr

# RTL-SDR 객체 생성
sdr = RtlSdr()

# SDR 설정
sdr.sample_rate = 2.4e6          # 샘플링 속도 (예: 2.4 MHz)
sdr.center_freq = 100e6           # 중심 주파수 (예: 100 MHz)
sdr.freq_correction = 60          # 주파수 보정 (ppm 단위)
sdr.gain = 'auto'                 # 이득 설정

# 데이터 수신
samples = sdr.read_samples(256*1024)

# SDR 객체 해제
sdr.close()

# FFT 수행
fft_data = np.abs(np.fft.fftshift(np.fft.fft(samples)))
freqs = np.fft.fftshift(np.fft.fftfreq(len(samples), 1/sdr.sample_rate)) + sdr.center_freq

# 스펙트럼 시각화
plt.figure(figsize=(10, 6))
plt.plot(freqs, 10*np.log10(fft_data))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power (dB)')
plt.title('RTL-SDR Spectrum')
plt.show()
