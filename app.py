from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process_frame():
    if 'stream' not in request.files:
        return jsonify({'success': False}), 400

    frame_data = request.files['stream'].read()
    
    # Aquí puedes procesar el frame (por ejemplo, aplicar filtros, compresión, etc.)
    
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10001)