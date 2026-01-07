from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required
from ..models import Student
from .. import db

student_bp = Blueprint('student', __name__)

@student_bp.route('/dashboard')
@login_required
def dashboard():
    students = Student.query.all()
    return render_template('students.html', students=students)

@student_bp.route('/add_student', methods=['POST'])
@login_required
def add_student():
    name = request.form['name']
    email = request.form['email']
    age = request.form['age']
    student = Student(name=name, email=email, age=age)
    db.session.add(student)
    db.session.commit()
    return redirect(url_for('student.dashboard'))

@student_bp.route('/update_student/<int:id>', methods=['POST'])
@login_required
def update_student(id):
    student = Student.query.get_or_404(id)
    student.name = request.form['name']
    student.email = request.form['email']
    student.age = request.form['age']
    db.session.commit()
    return redirect(url_for('student.dashboard'))

@student_bp.route('/delete_student/<int:id>')
@login_required
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for('student.dashboard'))
