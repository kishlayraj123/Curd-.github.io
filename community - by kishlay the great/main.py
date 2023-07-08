from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Create some initial data
opinions = []

# Home page - Show all opinions
@app.route('/')
def home():
    return render_template('opinions.html', opinions=opinions)

# Page to add a new opinion
@app.route('/add_opinion', methods=['GET', 'POST'])
def add_opinion():
    if request.method == 'POST':
        opinion = request.form['opinion']
        opinions.append({'opinion': opinion, 'comments': []})
        return redirect('/')
    return render_template('add_opinion.html')

# Page to view an opinion and add a comment
@app.route('/opinion/<int:index>', methods=['GET', 'POST'])
def view_opinion(index):
    if index >= len(opinions):
        return redirect('/')
    
    opinion = opinions[index]

    if request.method == 'POST':
        comment = request.form['comment']
        opinion['comments'].append(comment)
        return redirect('/opinion/{}'.format(index))

    return render_template('view_opinion.html', opinion=opinion)

if __name__ == '__main__':
    app.run(debug=True, port=9866)
