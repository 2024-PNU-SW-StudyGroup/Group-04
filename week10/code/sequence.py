import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from rtlsdr import RtlSdr
import threading
import queue

# RTL-SDR 설정
sdr = RtlSdr()
sdr.sample_rate = 2.4e6
sdr.center_freq = 100e6
sdr.freq_correction = 60
sdr.gain = 'auto'

# FFT 설정
fft_size = 1024
window = np.hanning(fft_size)

# 데이터 큐
data_queue = queue.Queue()

# 데이터 수신 스레드
def receive_data():
    while True:
        samples = sdr.read_samples(fft_size)
        data_queue.put(samples)

# 스레드 시작
thread = threading.Thread(target=receive_data, daemon=True)
thread.start()

# 플롯 설정
fig, ax = plt.subplots(figsize=(10, 6))
line, = ax.plot([], [], lw=1)
ax.set_xlim(-sdr.sample_rate/2, sdr.sample_rate/2)
ax.set_ylim(0, 100)
ax.set_xlabel('Frequency (Hz)')
ax.set_ylabel('Power (dB)')
ax.set_title('Real-Time RTL-SDR Spectrum')

def init():
    line.set_data([], [])
    return line,

def update(frame):
    if not data_queue.empty():
        samples = data_queue.get()
        fft_data = np.fft.fftshift(np.fft.fft(samples * window))
        fft_mag = 20 * np.log10(np.abs(fft_data) + 1e-6)
        freqs = np.fft.fftshift(np.fft.fftfreq(len(samples), 1/sdr.sample_rate)) + sdr.center_freq
        line.set_data(freqs - sdr.center_freq, fft_mag)
        ax.set_xlim(-sdr.sample_rate/2, sdr.sample_rate/2)
        ax.set_ylim(np.min(fft_mag), np.max(fft_mag))
    return line,

# 애니메이션 설정
ani = animation.FuncAnimation(fig, update, init_func=init, blit=True, interval=50)

plt.show()

# SDR 객체 해제
sdr.close()
