from unittest import TestCase, mock
import io
from io import StringIO
import sys


def stub_stdin(testcase_inst, inputs):
    stdin = sys.stdin

    def cleanup():
        sys.stdin = stdin

    testcase_inst.addCleanup(cleanup)
    sys.stdin = StringIO(inputs)


class Test(TestCase):

    @mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_calculator_basic_addition(self, mock_stdout):
        stub_stdin(self, """1
+
2
exit""")
        from syntax_and_algorithm import task_2_simple_calculator

        task_2_simple_calculator.main()
        self.assertEqual(
            "Total:3",
            mock_stdout.getvalue().strip().replace(" ", "").replace(">", "").strip(),
            msg="The calculator should print out Total: 3"
        )

    @mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_calculator_multiplying_multiple_numbers(self, mock_stdout):
        stub_stdin(self, """1
*
2
*
3
*
4
exit""")
        from syntax_and_algorithm import task_2_simple_calculator

        task_2_simple_calculator.main()
        self.assertEqual(
            """Total:2
Total:6
Total:24""",
            mock_stdout.getvalue().strip().replace(" ", "").replace(">", "").strip()
        )

    @mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_calculator_resetting(self, mock_stdout):
        stub_stdin(self, """1
*
2
10
20
*
2
exit""")
        from syntax_and_algorithm import task_2_simple_calculator

        task_2_simple_calculator.main()
        self.assertEqual(
            """Total:2
Total:40""",
            mock_stdout.getvalue().strip().replace(" ", "").replace(">", "").strip()
        )