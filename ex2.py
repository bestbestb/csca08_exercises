# Global variables. Feel free to play around with these
# but please return them to their original values before you submit.
a0_weight = 5
a1_weight = 7
a2_weight = 8
term_tests_weight = 20
exam_weight = 45
exercises_weight = 10
quizzes_weight = 5
a0_max_mark = 25
a1_max_mark = 50
a2_max_mark = 100
term_tests_max_mark = 50
exam_max_mark = 100
exercises_max_mark = 10
quizzes_max_mark = 5
exam_pass_mark = 40
overall_pass_mark = 50

def get_max(component_name):
    '''(str) -> float
    Given the name of a course component (component_name),
    return the maximum mark for that component. This is used to allow the GUI
    to display the "out of" text beside each input field.
    REQ: component_name must be one of: a0,a1,a2,exerises,midterm,exam
    >>> get_max('a0')
    25
    >>> get_max('exam')
    100
    REQ: component_name in {'a0', 'a1', 'a2', 'exercises', 'term tests',
    'quizzes', 'exam'}
    '''
    # DO NOT EDIT THIS FUNCTION. This function exists to allow the GUI access
    # to some of the global variables. You can safely ignore this function
    # for the purposes of E2.
    if(component_name == 'a0'):
        result = a0_max_mark
    elif(component_name == 'a1'):
        result = a1_max_mark
    elif(component_name == 'a2'):
        result = a2_max_mark
    elif(component_name == 'exercises'):
        result = exercises_max_mark
    elif(component_name == 'term tests'):
        result = term_tests_max_mark
    elif(component_name == 'quizzes'):
        result = quizzes_max_mark
    else:
        result = exam_max_mark

    return result


def percentage(raw_mark, max_mark):
    ''' (float, float) -> float
    Return the percentage mark on a piece of work that received a mark of
    raw_mark where the maximum possible mark of max_mark.
    >>> percentage(15, 20)
    75.0
    >>> percentage(4.5, 4.5)
    100.0
    REQ: raw_mark >=0
    REQ: max_mark > 0
    REQ: raw_max <= max_mark
    '''
   
    return raw_mark / max_mark * 100


def contribution(raw_mark, max_mark, weight):
    ''' (float, float, float) -> float
    Given a piece of work where the student earned raw_mark marks out of a
    maximum of max_marks marks possible, return the number of marks it
    contributes to the final course mark if this piece of work is worth weight
    marks in the course marking scheme.
    >>> raw_contribution(13.5, 15, 10)
    9.0
    REQ: raw_mark >=0
    REQ: max_mark > 0
    REQ: weight >= 0
    '''
    return raw_mark/max_mark*weight



def term_work_mark(a0_raw_mark, a1_raw_mark, a2_raw_mark, exercises_raw_mark, quizzes_raw_mark,term_tests_raw_mark):
    a0=contribution(a0_raw_mark,a0_max_mark,a0_weight)
    a1=contribution(a1_raw_mark,a1_max_mark,a1_weight)
    a2=contribution(a2_raw_mark,a2_max_mark,a2_weight)
    exercises=contribution(exercises_raw_mark,exercises_max_mark,exercises_weight)
    term_tests=contribution(term_tests_raw_mark,term_tests_max_mark,term_tests_weight)
    quizzes=contribution(quizzes_raw_mark,quizzes_max_mark,quizzes_weight)    
    
   
    return (a0+a1+a2+exercises+term_tests+quizzes)
    
    
def final_mark(a0_raw_mark, a1_raw_mark, a2_raw_mark, exercises_raw_mark, quizzes_raw_mark,term_tests_raw_mark, exam_raw_mark):
    term_work=term_work_mark(a0_raw_mark, a1_raw_mark, a2_raw_mark, exercises_raw_mark, quizzes_raw_mark,term_tests_raw_mark)
    exam=contribution(exam_raw_mark,exam_max_mark,exam_weight)
    result=term_work+exam
    return result  


def is_pass(a0_raw_mark, a1_raw_mark, a2_raw_mark, exercises_raw_mark, quizzes_raw_mark, term_tests_raw_mark,exam_raw_mark):
    a0=contribution(a0_raw_mark,a0_max_mark,a0_weight)
    a1=contribution(a1_raw_mark,a1_max_mark,a1_weight)
    a2=contribution(a2_raw_mark,a2_max_mark,a2_weight)
    exercises=contribution(exercises_raw_mark,exercises_max_mark,exercises_weight)
    term_tests=contribution(term_tests_raw_mark,term_tests_max_mark,term_tests_weight)
    quizzes=contribution(quizzes_raw_mark,quizzes_max_mark,quizzes_weight)
    exam=contribution(exam_raw_mark,exam_max_mark,exam_weight)
    if ((exam_raw_mark/exam_max_mark*100)>=40) and ((a0+a1+a2+exercises+term_tests+quizzes+exam)>=50):
        return True
    else:
        return False
    
        
   