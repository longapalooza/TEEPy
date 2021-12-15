import teepy

exam = teepy.begin(n_forms = 5, n_inds = 3)

section1 = exam.define_section(shuffle = True)
section1.problem('multiple_answer_question', 5)
section1.problem('open_ended_question', 5, min_height = 3)
section1.problem('question_with_givens', 5)
section1.problem('question_with_units', 5)
section1.problem('single_answer_question', 5)

section2 = exam.define_section(shuffle = True)
section2.problem('multiple_answer_question', 5)
section2.problem('open_ended_question', 5, min_height = 3)
section2.problem('question_with_givens', 5)

section3 = exam.define_section(shuffle = False)
section3.problem('question_with_units', 5)
section3.problem('single_answer_question', 5)
section2.section(section3)

exam.HTML('''<div style="text-align: center;">
<h1>COURSE NAME</h1><br>
<h2>Quiz/Exam</h2><br>
<h3>DATE</h3><br><br>
<h3>Form Number: ''' + exam.form_number() + '''</h3><br><br>
<h4>Printed Name: ________________________________________ </h4>
</div>''')
exam.new_page()
exam.new_page()
exam.problem('failure_to_answer_question', 0, pts_incorrect = -2,
             display_worth = False)
exam.section(section1)
exam.new_page()
exam.HTML('''New Section begins here''')
exam.section(section2)
exam.generate()