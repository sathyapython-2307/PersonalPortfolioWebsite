from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

projects_data = [
    {"id": 1, "name": "CozyHome - Interior Design", "description": "A simple and elegant interior design landing page using HTML, CSS, and JavaScript.", "link": "https://sathya-735.github.io/cozyhome/index.html", "tags": ["html", "css", "javascript"]},
    {"id": 2, "name": "Zara Cars", "description": "A car rental website built using React, Bootstrap, and routing with responsive design.", "link": "https://zara-theta-ten.vercel.app/", "tags": ["react", "bootstrap"]},
    {"id": 3, "name": "Fertix - Agri Ecommerce", "description": "A complete frontend e-commerce app for agriculture products with cart, wishlist, and checkout functionality.", "link": "https://fertix-git-main-sathyas-projects-9d486476.vercel.app/", "tags": ["react", "ecommerce"]},
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    tag = request.args.get('tag')
    if tag:
        filtered_projects = [p for p in projects_data if tag.lower() in [t.lower() for t in p['tags']]]
    else:
        filtered_projects = projects_data
    return render_template('projects.html', projects=filtered_projects, current_tag=tag)

@app.route('/project/<int:project_id>')
def project_detail(project_id):
    project = next((p for p in projects_data if p['id'] == project_id), None)
    if project:
        return render_template('project_detail.html', project=project)
    return redirect(url_for('projects'))

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        full_name = request.form['fullName']
        email = request.form['email']
        phone_number = request.form['phoneNumber']
        subject = request.form['subject']
        message = request.form['message']
        flash('Your message has been sent successfully!', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)