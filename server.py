from flask import Flask, request, render_template
app = Flask(__name__)
file_path = "./sensor_data.csv"
port_num = 19011
#aaaa

@app.route('/', methods = ['GET'])
def get_html():
    return render_template('./index.html')

@app.route('/lux', methods = ['POST'])
def update_lux():
    time = request.form["time"]
    lux = request.form["lux"]
    line = ""
    try:
        f = open(file_path, 'w+')
        for row in f:
            line = row
        if len(line) == 0:
            count = 0
        else:
            count = int(line.split(',')[2])

        #f.write(time + "," + lux)
        #if int(lux) > 10:
            #count += 1
            
        f.write(time + "," + lux + "," + str(count))
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