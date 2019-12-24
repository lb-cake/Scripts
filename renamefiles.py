import os
# import sys

src_directory = '/Users/wparks/Sites/ToDoAddSVGs/'
prepend_str = 'icon-'


def main():

    for filename in os.listdir(src_directory):
        src = src_directory + filename
        dst = src_directory + prepend_str + filename
        os.rename(src, dst)

    print('Modified ' + str(len(os.listdir(src_directory))) + ' files')


if __name__ == '__main__':
    main()
