from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Đọc câu hỏi từ file JSON
def load_questions(chapter):
    file_path = f'questions/chuong{chapter}.json'
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

@app.route('/')
def index():
    chapters = list(range(2, 14))  # Danh sách chương từ 2 đến 13
    return render_template('index.html', chapters=chapters)

@app.route('/quiz/<int:chapter>/<int:question_idx>', methods=['GET', 'POST'])
def quiz(chapter, question_idx):
    questions = load_questions(chapter)
    total_questions = len(questions)

    if question_idx >= total_questions:
        return redirect(url_for('result', chapter=chapter, total=total_questions))

    question = questions[question_idx]

    # Xác định câu hỏi tiếp theo
    next_question = question_idx + 1 if question_idx + 1 < total_questions else 0  # Chuyển lại câu hỏi đầu tiên nếu hết câu hỏi

    if request.method == 'POST':
        # Nhận câu trả lời từ người dùng
        user_answer = request.form.get('answer')
        correct_answer = question['Ans']
        is_correct = user_answer == correct_answer

        return render_template(
            'quiz_question.html',
            chapter=chapter,
            question=question,
            question_idx=question_idx,
            total_questions=total_questions,
            is_correct=is_correct,
            next_question=next_question  # Truyền next_question vào
        )

    # Xử lý yêu cầu GET
    return render_template(
        'quiz_question.html',
        chapter=chapter,
        question=question,
        question_idx=question_idx,
        total_questions=total_questions,
        next_question=next_question  # Truyền next_question vào
    )

@app.route('/result')
def result():
    chapter = request.args.get('chapter', type=int)
    total = request.args.get('total', type=int)
    return render_template('result.html', chapter=chapter, total=total)

if __name__ == '__main__':
    app.run(debug=True)
