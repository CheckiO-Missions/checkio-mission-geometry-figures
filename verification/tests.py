init_code = """
if not "Parameters" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Parameters'?")
Parameters = USER_GLOBAL['Parameters']

if not "Circle" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Circle'?")
Circle = USER_GLOBAL['Circle']

if not "Triangle" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Triangle'?")
Triangle = USER_GLOBAL['Triangle']

if not "Square" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Square'?")
Square = USER_GLOBAL['Square']

if not "Pentagon" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Pentagon'?")
Pentagon = USER_GLOBAL['Pentagon']

if not "Hexagon" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Hexagon'?")
Hexagon = USER_GLOBAL['Hexagon']

if not "Cube" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Cube'?")
Cube = USER_GLOBAL['Cube']
"""

run_test = """
RET['code_result'] = {}
"""


def prepare_test(test="", answer=None, middle_code="", show_code=None):
    if show_code is None:
        show_code = middle_code + "\n" + test
    if not test:
        return_code = "\nRET['code_result'] = ''"
        answer = ''
    else:
        return_code = run_test.format(test)
    return {"test_code": {"python-3": init_code + middle_code + return_code},
            "show": {"python-3": show_code},
            "answer": answer}


TESTS = {
    "Circle": [
        prepare_test(middle_code = '''figure = Parameters(10)
figure.choose_figure(Circle())''',
                     test="figure.perimeter()",
                     answer=6.28),
        prepare_test(middle_code = '''figure = Parameters(10)
figure.choose_figure(Circle())''',
                     test="figure.area()",
                     answer=314.16),
        prepare_test(middle_code = '''figure = Parameters(100)
figure.choose_figure(Circle())''',
                     test="figure.volume()",
                     answer=0)],
    "Triangle": [        
        prepare_test(middle_code = '''figure = Parameters(3.3)
figure.choose_figure(Triangle())''',
                     test="figure.perimeter()",
                     answer=9.9),
        prepare_test(middle_code = '''figure = Parameters(5)
figure.choose_figure(Triangle())''',
                     test="figure.area()",
                     answer=10.83),
        prepare_test(middle_code = '''figure = Parameters(10)
figure.choose_figure(Triangle())''',
                     test="figure.volume()",
                     answer=0)],
    "Square": [
        prepare_test(middle_code = '''figure = Parameters(3)
figure.choose_figure(Square())''',
                     test="figure.perimeter()",
                     answer=12),
        prepare_test(middle_code = '''figure = Parameters(5)
figure.choose_figure(Square())''',
                     test="figure.area()",
                     answer=25),
        prepare_test(middle_code = '''figure = Parameters(2.5)
figure.choose_figure(Square())''',
                     test="figure.volume()",
                     answer=0)],
    "Pentagon": [
        prepare_test(middle_code = '''figure = Parameters(10)
figure.choose_figure(Pentagon())''',
                     test="figure.perimeter()",
                     answer=50),
        prepare_test(middle_code = '''figure = Parameters(10)
figure.choose_figure(Pentagon())''',
                     test="figure.area()",
                     answer=172.05),
        prepare_test(middle_code = '''figure = Parameters(25)
figure.choose_figure(Pentagon())''',
                     test="figure.volume()",
                     answer=0)],
    "Hexagon": [
        prepare_test(middle_code = '''figure = Parameters(20)
figure.choose_figure(Hexagon())''',
                     test="figure.perimeter()",
                     answer=120),
        prepare_test(middle_code = '''figure = Parameters(10)
figure.choose_figure(Hexagon())''',
                     test="figure.area()",
                     answer=259.81),
        prepare_test(middle_code = '''figure = Parameters(8.88)
figure.choose_figure(Hexagon())''',
                     test="figure.volume()",
                     answer=0)],
    "Cube": [
        prepare_test(middle_code = '''figure = Parameters(10)
figure.choose_figure(Cube())''',
                     test="figure.perimeter()",
                     answer=120),
        prepare_test(middle_code = '''figure = Parameters(10)
figure.choose_figure(Cube())''',
                     test="figure.area()",
                     answer=600),
        prepare_test(middle_code = '''figure = Parameters(10)
figure.choose_figure(Cube())''',
                     test="figure.volume()",
                     answer=1000)
    ]

}
