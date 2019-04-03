#!/usr/bin/env bash
export PATH=/HWNAS12/RAD/luyang/SOFTWARE/miniconda3/envs/python3/bin:$PATH
python2 ../report.py pacb.html.txt ./
cd Reports/
python3 /HWNAS12/RAD/luyang/SOFTWARE/webpage2html/webpage2html.py -s report.html > pabc_reports.html
