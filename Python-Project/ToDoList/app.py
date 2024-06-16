# Import the Flask module and other necessary modules (e.g., request, redirect, url_for)
from flask import Flask, render_template, request, redirect, url_for

# Create a Flask application instance
app = Flask(__name__)

# Create a list to store to-do items (this will act as our in-memory database for now)
todo_list = []

# Define the route for the home page
@app.route('/')
def home():
    # Function to render the home page template and display the to-do list
    return render_template('index.html', todo_list=todo_list)

# Define the route for adding a new to-do item (use POST method)
@app.route('/add', methods=['POST'])
def add_item():
    # Function to handle the form submission and add the new item to the list
    new_item = request.form['item']
    todo_list.append(new_item)
    return redirect(url_for('home'))

# Define the route for deleting a to-do item (use GET method with item index as a parameter)
@app.route('/delete/<int:index>', methods=['GET'])
def delete_item(index):
    # Function to delete the item from the list based on the index
    if 0 <= index < len(todo_list):
        del todo_list[index]
    return redirect(url_for('home'))

# Run the Flask application
if __name__ == '__main__':
    # Make sure to enable debug mode for development
    app.run(debug=True)

# Hint: Use app.run(debug=True) to run the application with debug mode enabled
