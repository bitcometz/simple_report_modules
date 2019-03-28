# -*- coding: UTF-8 -*-
import os
import sys
import re
# why directly import html_support, because I just want to generate a template html and later used django
import report_modules.html_support as temp



def help():
    print("""

Program: *.py, do ...
         This script is used to change Txt to Html reports


Version: v1.0
Contact: Jinbo Zhang <zhangjinbo@novogene.com>

Usage:   python *.py *.txt work_dir


Hope you have a good day ^_^!

""")
    sys.exit(2)

def parseHtmlTxt(file, coord):

    coord['herfs'] = {}
    coord['bars'] = []
    coord['sects'] = {}
    coord['project_infos'] = {}
    flag4projs = 0
    flag4bars = 0
    flag4paras = 0
    sects_title = ''

    with open(file) as tmf:
        for line in tmf:
            line = line.strip("\n")
            if line != '' and not line.startswith("#"):
                if line == '[pros]':
                    flag4projs = 1
                    flag4bars  = 0
                    flag4paras = 0
                    continue
                elif line == '[bars]':
                    flag4projs = 0
                    flag4bars = 1
                    flag4paras = 0
                    continue
                elif line == '[paras]':
                    flag4paras = 0
                    flag4bars = 0
                    flag4paras = 1
                    continue

                if flag4projs == 1:
                    arr = line.split("=")
                    coord['project_infos'][arr[0]] = arr[1]
                elif flag4bars == 1:
                    arr = line.split(",")
                    tmpList = []
                    if arr[1] != '\"None\"':
                        for ti in range(1, len(arr)):
                            arr[ti] = arr[ti].strip()
                            arr[ti] = arr[ti].strip('\"')
                            tmpList.append(arr[ti])
                    arr2 = arr[0].split("=", 1)
                    arr2[1] = arr2[1].strip('\"')
                    (coord['bars']).append([arr2[0], arr2[1], tmpList])

                elif flag4paras == 1:
                    if line.startswith("T0:"):
                        arr = line.split(":",1)
                        sects_title = arr[1]
                        sects_title = sects_title.strip('\"')
                        coord['sects'][sects_title] = []

                    #elif line.startswith("P0"):
                    else:
                        coord['sects'][sects_title].append(line)



    return 0

def run(htmlTxtFile, work_dir):

    # copy static
    out_file = work_dir+'/report.html'
    src_dir = os.path.split(os.path.realpath(__file__))[0] + '/report_modules/static'
    os.system('cp -r {} {}'.format(src_dir, work_dir))

    coord = {}
    bars = {}
    herfs = {}
    sects = {}
    project_infos = {}

    parseHtmlTxt(htmlTxtFile, coord)
    bars  = coord['bars']
    sects = coord['sects']
    project_infos = coord['project_infos']

    with open(out_file, 'w') as html:

        html.write( temp.start() )

        html.write( temp.head( project_infos['Title_Name'] ) )

        # for the left bar
        html.write( temp.bar(bars, herfs) )
        # for the cover
        html.write( temp.cover(project_infos) )
        # for the main body
        html.write( temp.main_body_start() )

        html.write( temp.sections(bars, herfs, sects) )

        html.write( temp.body_end() )


        html.write( temp.end() )



def main(argv=sys.argv):
    #if len(argv) < 2 or argv[1].startswith('-'):
    #    help()


    #project_info_fofn = argv[1]
    htmlTxtFile = argv[1]
    #htmlTxtFile = 'asm.html.txt'
    work_dir = argv[2]
    #work_dir = './'
    os.chdir(work_dir)
    run(htmlTxtFile, work_dir)

    results_dir = work_dir + '/Reports'
    temp.make_dirs(results_dir)
    os.system("cp -r {}/data {}".format(work_dir, results_dir))
    os.system("cp -r {}/static {}".format(work_dir, results_dir))
    os.system("mv report.html {}".format(results_dir))


if __name__ == "__main__":
    main(sys.argv)

