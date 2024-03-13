from flask import Flask, render_template, request, jsonify
import QnABot, DebugBot

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/AIDebugger')
def AIDebugger():
    return render_template('AIDebugger.html')

@app.route('/Visualizer')
def Visualizer():
    return render_template('Visualizer.html')

@app.route('/TriviaBot')
def TriviaBot():
    return render_template('TriviaBot.html')

@app.route('/MatchTiles')
def MatchTiles():
    return render_template('MatchTiles.html')

@app.route('/debug_msg', methods=['POST'])
def debug_msg():
    data = request.get_json()
    
    if {data.get('mode')} == "hint":
        user_input = f"Go through the code-snippet or doubt description given by user and provide hints about the issues in code to the user. Do not provide full solution. Doubt - {data.get('doubt')}."
    else:
        user_input = f"Go through the code-snippet or doubt description given by user and resolve the doubt by sending corrected version of code. Doubt - {data.get('doubt')}."
 

    # Call OpenAI assistant API and process user input
    ai_response = DebugBot.debugger(user_input)
    print(ai_response)
        
    return jsonify({'response': ai_response})

@app.route('/generate_ques', methods=['POST'])
def generate_ques():
    data = request.get_json()
    
    user_input = f"Generate a looping statement related question in C language of {data.get('level')} level. Restrict the question length to one or two lines and generate new questions everytime."

    # Call OpenAI assistant API and process user input
    ai_response_q = QnABot.generate_qna(user_input)
    print(ai_response_q)
        
    return jsonify({'response': ai_response_q})

@app.route('/verify_answer', methods=['POST'])
def verify_answer():
    data = request.get_json()
    
    user_input = f"Check if the answer mentioned is correct for the mentioned question. Question: {data.get('question')}, Answer: {data.get('answer')}."

    # Call OpenAI assistant API and process user input
    ai_feedback = QnABot.generate_qna(user_input)
    print(ai_feedback)
        
    return jsonify({'response': ai_feedback})


if __name__ == '__main__':
    app.run(debug=True)
