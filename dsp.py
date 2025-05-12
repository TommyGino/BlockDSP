import numpy as np

def extract_features(samples, sample_rate_hz, channels, params):
    threshold = params.get('threshold', 20000)
    signal = np.array(samples)

    peaks = np.sum(np.abs(signal) > threshold)
    max_amp = np.max(np.abs(signal))
    mean = np.mean(signal)
    stddev = np.std(signal)

    return {
        'features': [peaks, max_amp, mean, stddev],
        'output_config': {
            'type': 'flat',
            'shape': [4]
        }
    }
