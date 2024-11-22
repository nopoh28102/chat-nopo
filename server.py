# coding: utf-8
import os
from flask import Flask, request, send_from_directory, render_template
import example.messenger
from example.fbpage import page

app = Flask(__name__)

# تعريف CONFIG
CONFIG = {
    'FACEBOOK_TOKEN': 'EAAPQug1lS68BOxj78t9mOgEM2mUx2y9bshljZAaP9bg6whu4zOLNNYpESg0QjZAcx9NuD2jyKSVgHTxOrM9QvTdfvwKqyZBvgos0HMWGGIy8FVlqVG70nkNcDfgQjGz2C2f0i9VR6s18iSZCXWG8OE6bEVnQZC1CyDmVLPcpCJFcJiZC34y2I5rfmyBOevIJL9LZBxxqcg87GU52faD',
    'VERIFY_TOKEN': 'verify_simsimbot',
    'SERVER_URL': 'https://chat-nopo-production.up.railway.app'
}

# Endpoint للتحقق من صحة Webhook
@app.route('/webhook', methods=['GET'])
def validate():
    if request.args.get('hub.mode', '') == 'subscribe' and \
            request.args.get('hub.verify_token', '') == CONFIG['VERIFY_TOKEN']:
        print("Validating webhook")
        return request.args.get('hub.challenge', '')
    else:
        return 'Failed validation. Make sure the validation tokens match.'

# Endpoint لاستقبال الـ POST من الفيسبوك
@app.route('/webhook', methods=['POST'])
def webhook():
    payload = request.get_data(as_text=True)
    print(payload)  # يمكنك مسح هذا الخط لاحقًا إذا كنت لا تحتاج إليه في الإنتاج
    page.handle_webhook(payload)
    return "ok"

# Endpoint للـ OAuth authorization
@app.route('/authorize', methods=['GET'])
def authorize():
    account_linking_token = request.args.get('account_linking_token', '')
    redirect_uri = request.args.get('redirect_uri', '')

    auth_code = '1073922437368751'  # يجب أن يكون هذا الرمز معتمدًا على التطبيق الخاص بك
    redirect_uri_success = redirect_uri + "&authorization_code=" + auth_code

    return render_template('authorize.html', data={
        'account_linking_token': account_linking_token,
        'redirect_uri': redirect_uri,
        'redirect_uri_success': redirect_uri_success
    })

# خدمة الملفات الثابتة (مثل الصور أو الملفات)
@app.route('/assets/<path:path>')
def assets(path):
    return send_from_directory('assets', path)

# تشغيل التطبيق
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)
