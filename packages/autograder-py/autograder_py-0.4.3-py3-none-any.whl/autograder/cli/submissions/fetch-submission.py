import sys

import autograder.api.submissions.fetchsubmission
import autograder.cli.submissions.common

def run(arguments):
    result = autograder.api.submissions.fetchsubmission.send(arguments, exit_on_error = True)

    if (not result['found-user']):
        print("No matching user found.")
        return 1

    if (not result['found-submission']):
        print("No matching submission found.")
        return 2

    autograder.cli.submissions.common.output_grading_result(
        result['grading-result'], arguments.out_dir)

    return 0

def main():
    return run(_get_parser().parse_args())

def _get_parser():
    parser = autograder.api.submissions.fetchsubmission._get_parser()

    parser.add_argument('-o', '--out-dir', dest = 'out_dir',
        action = 'store', type = str, default = '.',
        help = ('Where to create a new directory that contains the submission information.'
            + ' An existing subdirectory will be removed.'
            + ' Defaults to the current directory.'))

    return parser

if (__name__ == '__main__'):
    sys.exit(main())
