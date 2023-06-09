from flask import Flask, jsonify, request
import requests
import xmltodict
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/offer_feed')
def convert_xml_to_json():
    limit = request.args.get('limit', '')
    offer_type = request.args.get('offer_type', '')
    user_id = "251876"
    key = "118ed57c10f55f426fb8cc2418a137a5"

    url = f"https://www.cpagrip.com/common/offer_feed_rss.php?limit={limit}&offer_type={offer_type}&user_id={user_id}&key={key}&ip=&tracking_id="
    response = requests.get(url)
    xml_data = response.text
    json_data = xmltodict.parse(xml_data)
    return jsonify(json_data)

@app.route('/lead_check')
def lead_check():
    user_id = "251876"
    key = "118ed57c10f55f426fb8cc2418a137a5"
    time = request.args.get('time', '1day')
    check = request.args.get('check', 'ip')
    value = request.args.get('value', '')

    url = f"https://www.cpagrip.com/common/lead_check_rss.php?user_id={user_id}&key={key}&time={time}&check={check}&value={value}"
    response = requests.get(url)
    xml_data = response.text
    json_data = xmltodict.parse(xml_data)
    return jsonify(json_data)

if __name__ == '__main__':
    app.run()#(debug=False,host='0.0.0.0')
