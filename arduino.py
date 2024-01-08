import serial

import csv



# Replace '/dev/cu.usbmodemXXX' with your Arduino port

arduino_port = '/dev/cu.usbmodemXXX'

baud_rate = 9600



try:

    ser = serial.Serial(arduino_port, baud_rate)

except serial.SerialException as e:

    print(f"Error opening serial port: {e}")

    exit()



csv_file_path = 'arduino_data.csv'



with open(csv_file_path, 'w', newline='') as csvfile:

    csv_writer = csv.writer(csvfile)



    # Write header if needed

    # csv_writer.writerow(['Column1', 'Column2', 'Column3', ...])



    try:

        while True:

            try:

                data = ser.readline().decode().strip()

                print(data)  # Optional: print to terminal for verification



                # Split data and write to CSV

                csv_writer.writerow(data.split(','))



            except KeyboardInterrupt:

                break



    except serial.SerialException as e:

        print(f"Serial error: {e}")



    except Exception as e:

        print(f"Error: {e}")



finally:

    if ser.is_open:

        ser.close()