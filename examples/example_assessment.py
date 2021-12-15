import teepy

exam = teepy.begin(n_forms = 0, n_inds = 1)

exam.HTML('''<div style="text-align: center;">
<h1>COURSE NAME</h1><br>
<h2>Quiz/Exam ##</h2><br>
<h3>DATE</h3><br><br>
<h3>Form Number: ''' + exam.form_number() + '''</h3><br><br>
<h4>Printed Name: ________________________________________ </h4>
</div>''')
exam.new_page()

exam.HTML('<h3><b><u>A question with no displayed point value</u></b></h3>')
exam.problem('failure_to_answer_question', 0, pts_incorrect = -2,
             display_worth = False)

exam.HTML('<h3><b><u>A single answer question</u></b></h3>')
exam.problem('single_answer_question', 5)

exam.HTML('<h3><b><u>A multiple answer question</u></b></h3>')
exam.problem('multiple_answer_question', 5)

exam.HTML('<h3><b><u>An open-ended question</u></b></h3>')
exam.problem('open_ended_question', 5, min_height = 0.75)

exam.HTML('<h3><b><u>A question with given variables</u></b></h3>')
exam.problem('question_with_givens', 5)

exam.HTML('<h3><b><u>A question with units</u></b></h3>')
exam.problem('question_with_units', 5)

exam.generate(output_dir = '.')