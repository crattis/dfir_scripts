#!python3
'''
Creates folder for the case on the user's desktop to track cases. If
the user wants to store it somewhere other than the desktop, change the
location variable under local_variables.
Requires that the folder Cases already exists at location.
'''

# TODO: Align with sub folders to the Blue Team handbook
# TODO: create this as a stand alone package to import via PIP
# TODO: Maybe... Look at changing keywords to regex replace spaces with
# underscores


# imports
import os
import sys
from time import strftime


def local_variables():
    home = os.path.expanduser('~')
    location = 'Desktop'
    case_folder = 'Cases'
    combine = os.path.join(home, location, case_folder)
    return combine


def test_case_num(folder, case_number):
    for filename in os.listdir(folder):
        if case_number in filename:
            print('Case {} already has a folder'.fortmat(case_number))
            print(filename)
            os.system('pause')
            sys.exit(1)
    return


def main():
    # Get information to crate the case folder
    local_var = local_variables()
    case_num = input('Paste your case number: ')
    test_case_num(local_var, case_num)
    case_title = input('Keywords to summarize case use. Please underscores '
                       'to separate words: ')
    case_time = str(strftime('%Y_%m_%d'))
    case_folder = case_time + '_' + case_num + '_' + case_title
    new_folder = os.path.join(local_var, case_folder)
    # Create the Case folder, live sample subfolder, and case notes
    # txt file
    os.mkdir(new_folder)
    case_notes = case_num + '_case_notes.txt'
    os.chdir(new_folder)
    os.mkdir('live_samples')
    open(case_notes, 'w').close()
    # Opens case folder and case notes file.
    os.startfile(new_folder)
    os.startfile(case_notes)


if __name__ == '__main__':
    main()
