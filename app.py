from flask import Flask, render_template, request, jsonify, redirect
import QnABot, DebugBot
from flask import Flask
from flask import render_template
from flask import json
from flask import request
import random
import sys
import ast # module to transform a string to a dictionary
import questions

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
'''
@app.route('/MatchTiles')
def MatchTiles():
    return redirect("http://localhost:3000/")'''

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

users = {}

@app.route('/MatchTiles')
def MatchTiles():
    return render_template("indexGame.html"), 200

@app.route("/intro", methods = ["POST"])
def intro():
	post_obj = request.json
	post_obj["board"] = make_board(post_obj["level"])
	users[post_obj["username"]] = post_obj
	return json.dumps(post_obj), 200

@app.route("/card", methods = ["POST"])
def card():
	post_obj = request.json
	choice = post_obj["choice"]
	choice = ast.literal_eval(choice) # converts the str to dict
	client_name = post_obj["username"]
	client = users[client_name]
	client_board = client["board"]
	info = {}
	info["value"] = client_board[int(choice["bigBox"])][int(choice["smallerBox"])]
	info["id"] = choice["id"]
	return json.dumps(info), 200

@app.errorhandler(404)
def page_not_found(err):
	return render_template("404.html"), 400

'''
	Function: make_board
	 Purpose: Creates and returns an array containing a 2-D array of a size provided
			  through the function parameters.
		  in: size 
'''

def make_board(size):
	double = size * size
	pool = []
	pool_two = []
	board = []

	for i in range(int(double / 2)):
		pool.append(i)
		pool_two.append(i)

	larger_pool = []	#Final list of integers on board - 2 of each
	for i in range(double):
		if len(pool) != 0:
			random_draw = pool[random.randint(0, len(pool) - 1)]
			pool.remove(random_draw)
			larger_pool.append(questions.qlist[random_draw])
		elif len(pool) == 1:
			random_draw = pool[0]
			pool.remove(random_draw)
			larger_pool.append(questions.qlist[random_draw])

		if len(pool_two) != 0:
			random_draw = pool_two[random.randint(0, len(pool_two) - 1)]
			pool_two.remove(random_draw)
			larger_pool.append(questions.alist[random_draw])
		elif len(pool_two) == 1:
			random_draw = pool_two[0]
			pool_two.remove(random_draw)
			larger_pool.append(questions.alist[random_draw])
	#print(larger_pool)

	for i in range(size):	
		mini_board = [] #List of each row
		for j in range(size):
			mini_board.append(larger_pool[0])
			larger_pool.remove(larger_pool[0])
		board.append(mini_board)
		#print(mini_board)

	return board

if __name__ == '__main__':
    app.run(debug=True)