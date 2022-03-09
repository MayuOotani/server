from flask import Flask, request, render_template
app = Flask(__name__)
file_path = "./sensor_data.csv"
port_num = 19011

@app.route('/', methods = ['GET'])
def get_html():
    return render_template('./index.html')

@app.route('/lux', methods = ['POST'])
def update_lux():
    time = request.form["time"]
    lux = request.form["lux"]
    line = "hoge"
    try:
        f = open(file_path, 'r')
        for row in f:
            line = row
        #print(line)
        log = line.split(',')
        today = time.split(',')[0]
        if line == "hoge" or log[0] != today:
            second = 0
            counter = 0
        else:
            second = int(log[3])
            counter = int(log[4])
        if int(lux) > 10:
            second += 1
            if int(log[2]) <= 10 or counter == 0:
                counter += 1
    except Exception as e:
        f = open(file_path, 'w')
        f.close()
    finally:
        f.close()

    try:
        f = open(file_path, 'w')
        #f.write(time + "," + lux)
        f.write(time + "," + lux + "," + str(second) + "," + str(counter))
        return "succeeded to write"
    except Exception as e:
        print(e)
        return "failed to write"
    finally:
        f.close()

@app.route('/lux', methods = ['GET'])
def get_lux():
    try:
        f = open(file_path, 'r')
        for row in f:
            lux = row
    except Exception as e:
        print(e)
    finally:
        f.close()
    return lux

if __name__ == '__main__':
    app.run(debug = True, host= '0.0.0.0', port = port_num)