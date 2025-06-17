from flask import Flask, render_template_string, request
import subprocess

app = Flask(__name__)

html = '''
<!DOCTYPE html>
<html>
<head><title>Pi Waker</title></head>
<body>
  <h1>Wake-on-LAN Sender</h1>
  <form method="post">
    MAC Address: <input type="text" name="mac" placeholder="AA:BB:CC:DD:EE:FF" required>
    <button type="submit">Wake</button>
  </form>
  <p>{{ message }}</p>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    if request.method == 'POST':
        mac = request.form.get('mac')
        # 呼叫系統指令 wakeonlan
        try:
            subprocess.run(['wakeonlan', mac], check=True)
            message = f'Sent WOL packet to {mac}'
        except Exception as e:
            message = f'Error: {e}'
    return render_template_string(html, message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
