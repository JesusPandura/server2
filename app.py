from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process_frame():
    if 'stream' not in request.files:
        return jsonify({'success': False, 'error': 'No stream found'}), 400

    try:
        frame_data = request.files['stream'].read()
        print("Frame recibido")  # Log para verificar la recepción

        # Aquí puedes procesar el frame (por ejemplo, aplicar filtros, compresión, etc.)
        
        # Simulación de procesamiento (puedes agregar tu lógica aquí)
        # processed_frame = process_your_frame(frame_data)

        return jsonify({'success': True})
    except Exception as e:
        print(f"Error procesando el frame: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10001)