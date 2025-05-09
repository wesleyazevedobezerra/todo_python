from app.models.taskViewModel import get_db

def get_all_tasks():
    db = get_db()
    return db.execute('SELECT * FROM tasks').fetchall()

def get_task_by_id(task_id):
    db = get_db()
    return db.execute('SELECT * FROM tasks WHERE id = ?', (task_id,)).fetchone()

def create_task(title, description):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('INSERT INTO tasks (title, description) VALUES (?, ?)', (title, description))
    db.commit()
    return cursor.lastrowid

def update_task(task_id, title, description):
    db = get_db()
    db.execute('UPDATE tasks SET title = ?, description = ? WHERE id = ?', (title, description, task_id))
    db.commit()

def delete_task(task_id):
    db = get_db()
    db.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    db.commit()
