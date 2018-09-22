from flask import Flask, render_template, request, jsonify
from func.get_data_by_ipblock import get_data_by_ipblock

app = Flask(__name__)


@app.route('/')
def route_get_hostnames():
    return render_template('index.html')

@app.route('/api/get_by_ipblock')
def route_get_by_ipblock():
    ip_block = request.args.get('block')

    if ip_block:
        # TODO: Check if valid CIDR block range
        data = get_data_by_ipblock(ip_block)

        return jsonify(data)
    else:
        # If IP block not set, return error
        return jsonify({'err': True,
                        'msg': "IP block not set"})


if __name__ == '__main__':
    app.run()
