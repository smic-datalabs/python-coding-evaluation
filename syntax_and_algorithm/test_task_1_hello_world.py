import io
from unittest import TestCase, mock


class Test(TestCase):
    @mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_print(self, mock_stdout):
        from syntax_and_algorithm import task_1_hello_world
        task_1_hello_world.main()
        self.assertEqual("Hello, world!", mock_stdout.getvalue().strip())
