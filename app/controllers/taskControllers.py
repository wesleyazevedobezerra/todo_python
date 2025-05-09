from flask import Blueprint, request, jsonify
from app.services import taskAppService

task_bp = Blueprint('task_bp', __name__)

@task_bp.route('', methods=['GET'])
def get_tasks():
    tasks = taskAppService.get_all_tasks()
    return jsonify([dict(task) for task in tasks])

@task_bp.route('/<int:id>', methods=['GET'])
def get_task(id):
    task = taskAppService.get_task_by_id(id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    return jsonify(dict(task))

@task_bp.route('', methods=['POST'])
def create():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description', '')
    if not title:
        return jsonify({'error': 'Title is required'}), 400
    task_id = taskAppService.create_task(title, description)
    return jsonify({'id': task_id, 'title': title, 'description': description}), 201

@task_bp.route('/<int:id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    task = taskAppService.get_task_by_id(id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    taskAppService.update_task(id, data.get('title'), data.get('description', ''))
    return jsonify({'id': id, 'title': data.get('title'), 'description': data.get('description', '')})

@task_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    task = taskAppService.get_task_by_id(id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    taskAppService.delete_task(id)
    return jsonify({'message': 'Task deleted'})
