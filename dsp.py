import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/run', methods=['POST'])
def run_block():
    data = request.get_json()
    samples = data.get('samples', [])
    sample_rate_hz = data.get('sampleRate', 16000)
    channels = data.get('channels', 1)
    params = data.get('parameters', {})

    threshold = params.get('threshold', 20000)
    signal = np.array(samples)

    peaks = int(np.sum(np.abs(signal) > threshold))
    max_amp = float(np.max(np.abs(signal)))
    mean = float(np.mean(signal))
    stddev = float(np.std(signal))

    return jsonify({
        'features': [peaks, max_amp, mean, stddev],
        'outputConfig': {
            'type': 'flat',
            'shape': [4]
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4446)
