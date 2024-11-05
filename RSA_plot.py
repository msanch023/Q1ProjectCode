# %% imports
import h5py
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
from scipy.stats import skew

def rsa(waveform, tp0):
    x = np.arange(waveform.shape[0])

    plt.figure(figsize=(12, 6))
    plt.plot(x, waveform, label='Charge')

    end = np.where(waveform == np.max(waveform))[0][0]

    interp_range = np.arange(tp0, end + 1, 1)
    interp = interpolate.interp1d(x, waveform, kind = 'linear')
    interp_vals = interp(interp_range)

    plt.plot(interp_range, interp_vals, 'r--', label = 'Rising Edge (Interpolated)')

    x10 = tp0 + 0.10 * (end - tp0)
    x50 = tp0 + 0.50 * (end - tp0)
    x999 = tp0 + 0.999 * (end - tp0)
    y10 = interp(x10)
    y50 = interp(x50)
    y999 = interp(x999)

    plt.plot(x10, y10, 'ro', label='10% Total charge')
    plt.plot(x50, y50, 'go', label='50% Total charge')
    plt.plot(x999, y999, 'bo', label='99% Total charge')

    skewness = skew(interp_vals)

    plt.xlabel('Time (Nanoseconds)')
    plt.ylabel('Amplitude (Analog to Digital Converter Units)')
    plt.legend()
    plt.show()

    return skewness
    
# %%
with h5py.File('/Users/marcosanchez/Library/Mobile Documents/com~apple~CloudDocs/FA24/DSC 180A/MJD_Train_0.hdf5', 'r') as f:

    raw_waveform = np.array(f['raw_waveform'])
    index = np.random.choice(raw_waveform.shape[0])

    start = f['tp0'][index]


    rsa(raw_waveform[index], start)
