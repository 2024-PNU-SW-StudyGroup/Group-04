from flask import Flask, render_template, request, jsonify
import serial
import os

app = Flask(__name__)

# Serial port configuration for LTE module
SERIAL_PORT = '/dev/ttyUSB0'  # Change this to your LTE module's serial port
BAUD_RATE = 9600  # Adjust baud rate to match CanSat settings
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)

# Send command to CanSat
@app.route('/send_command', methods=['POST'])
def send_command():
    command = request.form['command']
    ser.write(command.encode())  # Send command via serial port
    return jsonify({'status': 'Command Sent', 'command': command})

# Get status from CanSat
@app.route('/get_status', methods=['GET'])
def get_status():
    ser.write(b'STATUS')  # Send status request command
    status = ser.readline().decode().strip()  # Read response from CanSat
    return jsonify({'status': status})

# Main control panel page
@app.route('/')
def index():
    return render_template('control_panel.html')

if __name__ == '__main__':
    # Ensure the serial connection is open
    if not ser.is_open:
        ser.open()
    
    app.run(host='0.0.0.0', port=5000)
