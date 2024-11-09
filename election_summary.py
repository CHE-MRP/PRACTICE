from flask import Flask, render_template_string
import io

app = Flask(__name__)

HTML = """
<html>
<body>
  <h2>2024 Presidential Election Summary</h2>
  <button onclick="playNarration()">Play Narration</button>
  <script>
    function playNarration() {
      fetch('/play_narration')
        .then(response => response.text())
        .then(text => console.log(text));
      // Here you would actually play audio but for simplicity, we'll log it
    }
  </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

@app.route('/play_narration')
def play_narration():
    # Capture the output of election_summary as a string
    captured_output = io.StringIO()
    import sys
    sys.stdout = captured_output
    election_summary()  # Your function here
    sys.stdout = sys.__stdout__
    return captured_output.getvalue()

if __name__ == '__main__':
    app.run(debug=True)
