"""
Welcome to the Code for Lab 5 Q2b in PHY407

If you're running the code as organised in the Repo, please run code from the directory Lab5
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read, write
from numpy import empty

PLOT_WAV = True
PLOT_TRANSFORM = True
MAKE_NEW_WAV = False

def main():
    print("----------START----------")
    print("Hi! Welcome to Lab 5 Question 2b!")
    
    # Example code.
    # read the data into two stereo channels
    # sample is the sampling rate, data is the data in each channel,
    # dimensions [2, nsamples]
    sample, data = read('inputs/GraviteaTime.wav')
    # sample is the sampling frequency, 44100 Hz
    # separate into channels
    channel_0 = data[:, 0]
    channel_1 = data[:, 1]
    N_Points = len(channel_0)

    t = np.arange(N_Points) / sample

    if PLOT_WAV:
        # Plot the WAV file.
        # Plot channel 0
        plt.figure(figsize=(10, 4))
        plt.plot(t, channel_0, color='b')
        plt.title('Channel 0')
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.grid(True)
        
        # Plot channel 1
        plt.figure(figsize=(10, 4))
        plt.plot(t, channel_1, color='r')
        plt.title('Channel 1')
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.grid(True)
        
        plt.show()


    # Focus on 20–50 ms segment
    t_min = 0.020  # 20 ms
    t_max = 0.050  # 50 ms
    mask = (t >= t_min) & (t <= t_max)
    t_zoom = t[mask]
    ch0_zoom = channel_0[mask]
    ch1_zoom = channel_1[mask]

    # Perform FFT
    # freq = np.fft.fftfreq(N_Points, d=1/sample)
    fft_ch0 = np.fft.fft(channel_0)
    fft_ch1 = np.fft.fft(channel_1)

    df = sample / N_Points              # distance between bins
    cutoff = 880.0                      # Hz
    cutoff_bin = int(cutoff / df)

    # Initialize a mask of zeros
    filter_mask = np.zeros(N_Points)

    # Keep only low-frequency bins (below cutoff)
    filter_mask[:cutoff_bin] = 1
    filter_mask[-cutoff_bin:] = 1       # keep negative frequencies as needed.

    # Apply mask to FFT data
    fft_ch0_filt = fft_ch0 * filter_mask
    fft_ch1_filt = fft_ch1 * filter_mask

    # Inverse FFT to get filtered time-domain signal
    ch0_filt = np.real(np.fft.ifft(fft_ch0_filt))
    ch1_filt = np.real(np.fft.ifft(fft_ch1_filt))

    if PLOT_TRANSFORM:
        fig, axs = plt.subplots(2, 2, figsize=(12, 6))
        plt.suptitle('Channel 0 & 1: Original vs Filtered')

        # Channel 0 spectrum
        axs[0, 0].plot(np.arange(N_Points), np.abs(fft_ch0), label='Original')
        axs[0, 0].plot(np.arange(N_Points), np.abs(fft_ch0_filt), label='Filtered')
        axs[0, 0].set_title('Channel 0 FFT Amplitude')
        axs[0, 0].set_xlabel('FFT Bin Index')
        axs[0, 0].set_ylabel('Amplitude')
        axs[0, 0].legend()
        axs[0, 0].grid(True)

        # Channel 1 spectrum
        axs[1, 0].plot(np.arange(N_Points)//1, np.abs(fft_ch1), label='Original')
        axs[1, 0].plot(np.arange(N_Points)//1, np.abs(fft_ch1_filt), label='Filtered')
        axs[1, 0].set_title('Channel 1 FFT Amplitude')
        axs[1, 0].set_xlabel('FFT Bin Index')
        axs[1, 0].set_ylabel('Amplitude')
        axs[1, 0].legend()
        axs[1, 0].grid(True)

        # Channel 0 time-domain (zoomed)
        axs[0, 1].plot(t_zoom, ch0_zoom, label='Original')
        axs[0, 1].plot(t_zoom, ch0_filt[mask], label='Filtered')
        axs[0, 1].set_title('Channel 0 Time Series (20–50 ms)')
        axs[0, 1].set_xlabel('Time (s)')
        axs[0, 1].set_ylabel('Amplitude')
        axs[0, 1].legend()
        axs[0, 1].grid(True)

        # Channel 1 time-domain (zoomed)
        axs[1, 1].plot(t_zoom, ch1_zoom, label='Original')
        axs[1, 1].plot(t_zoom, ch1_filt[mask], label='Filtered')
        axs[1, 1].set_title('Channel 1 Time Series (20–50 ms)')
        axs[1, 1].set_xlabel('Time (s)')
        axs[1, 1].set_ylabel('Amplitude')
        axs[1, 1].legend()
        axs[1, 1].grid(True)
        plt.show()

    if MAKE_NEW_WAV:
        # Output new WAV:
        # this creates an empty array data_out with the same shape as "data"
        # (2*N_Points) and the same type as "data" (int16)
        data_out = empty(data.shape, dtype = data.dtype)
        # Fill data_out
        data_out[:, 0] = ch0_filt.astype(data.dtype)
        data_out[:, 1] = ch1_filt.astype(data.dtype)
        # save to new .wav file
        write('GraviteaTime_lpf.wav', sample, data_out)

    print("----------END----------")


if __name__ == "__main__":
    main()