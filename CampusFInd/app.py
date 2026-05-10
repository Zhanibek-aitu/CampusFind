from flask import Flask, render_template, request, redirect, url_for
from manager import LostFoundManager
from storage import StorageManager
from item import Item 

app = Flask(__name__)

manager = LostFoundManager()
storage = StorageManager()
manager.items = storage.load_items()

@app.route('/')
def index():
    items_list = manager.list_items()
    return render_template('index.html', items=items_list)

@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        name = request.form['name']
        item_type = request.form['item_type']
        category = request.form['category']
        location = request.form['location']
        description = request.form['description']
        
        new_item = Item(name, item_type, category, location, description)
        
        manager.add_item(new_item)
        storage.save_items(manager.items)
        
        return redirect(url_for('index'))
        
    return render_template('add_item.html')

@app.route('/update/<item_id>', methods=['POST'])
def update_item(item_id):
    new_status = request.form['new_status']
    manager.update_status(item_id, new_status)
    storage.save_items(manager.items)
    return redirect(url_for('index'))

@app.route('/delete/<item_id>', methods=['POST'])
def delete_item(item_id):
    manager.delete_item(item_id)
    storage.save_items(manager.items)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)