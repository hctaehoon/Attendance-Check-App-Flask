from flask import Flask, render_template , request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
import os
from sqlalchemy import func

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    date = db.Column(db.DateTime, index=True)
    
db.create_all()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit_attendance', methods=['POST'])
def submit_attendance():
    attendance = request.form.getlist('attendance')
    for name in attendance:
        record = Attendance(name=name, date=datetime.utcnow())
        db.session.add(record)
    db.session.commit()
    return render_template("check.html")



@app.route('/attendance_list', methods=['GET'])
def attendance_list():
    today = datetime.today().strftime('%Y-%m-%d')
    month = request.args.get('month', default=today, type=str)
    attendances = Attendance.query.filter(func.strftime('%Y-%m-%d', Attendance.date) == month).order_by(Attendance.date).all()
    monthly_results = db.session.query(Attendance.name, func.count(Attendance.id)).filter(func.strftime('%Y-%m', Attendance.date) == month).group_by(Attendance.name).all()
    monthly_counts = {name: count for name, count in monthly_results}
    return render_template('attendance_list.html', attendances=attendances, monthly_counts=monthly_counts, today=today)





@app.route('/clear_data', methods=['GET'])
def clear_data():
    try:
        num_rows_deleted = db.session.query(Attendance).delete()
        db.session.commit()
        return f"성공적으로 {num_rows_deleted} 개의 데이터를 삭제하였습니다."
    except:
        db.session.rollback()
        return "데이터 삭제에 실패하였습니다."


if __name__ == '__main__':
    app.run(debug=False,port=5000)