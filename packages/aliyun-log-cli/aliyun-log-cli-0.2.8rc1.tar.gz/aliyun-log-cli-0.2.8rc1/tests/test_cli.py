from .util import run_test
import os

def test_main():
    # files = sys.argv[1:]
    # if not files:
    files = ['cmd_list.txt']
    for file_path in files:
        abs_path = os.path.sep.join([os.path.dirname(__file__), file_path])
        run_test(abs_path)


if __name__ == '__main__':
    test_main()


