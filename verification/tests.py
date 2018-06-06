init_code = """
if not "Figure" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Figure'?")

Figure = USER_GLOBAL['Figure']
"""

run_test = """
RET['code_result'] = {}
"""


def prepare_test(test="", answer=None, middle_code="\n", show_code=None):
    if show_code is None:
        show_code = middle_code + test
    if not test:
        return_code = "\nRET['code_result'] = ''"
        answer = ''
    else:
        return_code = run_test.format(test)
    return {"test_code": {"python-3": init_code + middle_code + return_code},
            "show": {"python-3": show_code},
            "answer": answer}


TESTS = {
    "Figures": [
        prepare_test(test="Figure('circle', 1).perimeter()",
                     answer=6.28),
        prepare_test(test="Figure('circle', 10).area()",
                     answer=314.16),
        prepare_test(test="Figure('circle', 100).volume()",
                     answer=0),
        
        prepare_test(test="Figure('triangle', 3.3, 3.3, 3.3).perimeter()",
                     answer=9.9),
        prepare_test(test="Figure('triangle', 3, 4, 5).area()",
                     answer=6),
        prepare_test(test="Figure('triangle', 10, 6, 7).volume()",
                     answer=0),

        prepare_test(test="Figure('rectangle', 2, 4).perimeter()",
                     answer=12),
        prepare_test(test="Figure('rectangle', 5, 5).area()",
                     answer=25),
        prepare_test(test="Figure('rectangle', 25, 10).volume()",
                     answer=0),

        prepare_test(test="Figure('pentagon', 10).perimeter()",
                     answer=50),
        prepare_test(test="Figure('pentagon', 10).area()",
                     answer=172.05),
        prepare_test(test="Figure('pentagon', 25).volume()",
                     answer=0),

        prepare_test(test="Figure('hexagon', 20).perimeter()",
                     answer=120),
        prepare_test(test="Figure('hexagon', 10).area()",
                     answer=259.81),
        prepare_test(test="Figure('hexagon', 8).volume()",
                     answer=0),

        prepare_test(test="Figure('cube', 10).perimeter()",
                     answer=120),
        prepare_test(test="Figure('cube', 10).area()",
                     answer=600),
        prepare_test(test="Figure('cube', 10).volume()",
                     answer=1000)
    ]

}
