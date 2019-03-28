# -*- coding: UTF-8 -*-
import os

def set4head(title_name):

    txt = '''
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<!-- Meta, title, CSS, favicons, etc. -->
<meta name="renderer" content="webkit">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="">
<meta name="keywords" content="">
<meta name="author" content="Mark Otto, Jacob Thornton, and Bootstrap contributors">
<meta name="author" content="徐彪 &lt;xubiaosunny@163.com&gt;">

<title>{title_name}</title>
<!-- Bootstrap core CSS -->
<!-- 新 Bootstrap 核心 CSS 文件 -->
<link rel="stylesheet" href="static/css/bootstrap.min.css">
<!-- 可选的Bootstrap主题文件（一般不用引入） -->
<!--<link rel="stylesheet" href="static/css/bootstrap-theme.min.css">-->
<!-- Optional Bootstrap Theme -->
<!--<link href="data:text/css;charset=utf-8," data-href="static/css/bootstrap-theme.min.css" rel="stylesheet" id="bs-theme-stylesheet">-->
<!-- Documentation extras -->
<link href="./static/css/docs.min.css" rel="stylesheet">
<link href="https://cdn.bootcss.com/docsearch.js/2.2.0/docsearch.css" rel="stylesheet">
<link href="./static/css/mydoc.css" rel="stylesheet">
<link rel="stylesheet" type="text/css" href="static/css/jquery.ad-gallery.css">
<link rel="stylesheet" type="text/css" href="static/css/font-awesome/css/font-awesome.min.css">

<!--For js>
<!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
<!--[if lt IE 9]>
<script src="http://cdn.bootcss.com/html5shiv/3.7.0/html5shiv.js"></script>
<script src="http://cdn.bootcss.com/respond.js/1.4.2/respond.min.js"></script>


<!-- Favicons -->
<link rel="apple-touch-icon" href="">
<link rel="icon" href="">
<style type="text/css"></style>

<!-- For Slide effect -->
<link rel="stylesheet" href="static/css/base.css">
<link rel="stylesheet" href="static/css/bootstrap.min.css">

<link rel="stylesheet" href="static/css/blueimp-gallery.min.css">
<link rel="stylesheet" href="static/css/bootstrap-image-gallery.min.css">

<script type="application/javascript" src="static/js/jquery.js"></script>
<script type="application/javascript" src="static/js/jquery.albumSlider.min.js"></script>
<script type="application/javascript" src="static/js/jquery.blueimp-gallery.min.js"></script>
<script type="application/javascript" src="static/js/bootstrap.min.js"></script>
<script type="application/javascript" src="static/js/bootstrap-image-gallery.min.js"></script>





    '''.format(title_name=title_name)

    txt +='''

    <script>
        function displaySubMenu(li) {
            var subMenu = li.getElementsByTagName("ul")[0];
            subMenu.style.display = "block";
        }

        function hideSubMenu(li) {
            var subMenu = li.getElementsByTagName("ul")[0];
            subMenu.style.display = "none";
        }

        $(function () {
            //纵向，默认，移动间隔2
            $('div.albumSlider').albumSlider();
            //横向设置
            $('div.albumSlider-h').albumSlider({direction: 'h', step: 3});
        });

        $(window).resize(function () {
            $.getScript("data/repeat.js");
        });
        
        $(document).ready(function(){
	        $("#cover").css("height",$(window).height());//封面高度为屏幕高度
	    // $("img").attr("crossorigin","*");
    });
        
    </script>

    <style media="print">
        .noprint {
            DISPLAY: none;
        }
    </style>

</head>
'''

    return txt

def add_title(name, title, numS):
    # <a name="Nanopore Sequencing Mechanism"></a>
    # <h3>Nanopore测序原理</h3>
    txt = '''
    <a name=\"{name}\"></a>
    <h{numS}>{title}</h{numS}>    
'''.format(name=name, title=title, numS=numS)
    return txt

def add_paragraph(paragraph):
    # <p class="paragraph">诺禾致源引入的基于Nangies测序成本低、测序周期短等特点。</p>
    txt = '''
    <p class=\"paragraph\">{paragraph}</p>
'''.format(paragraph=paragraph)
    return txt

def add_paragraphs(paragraphs):
    txt = ''
    for i in paragraphs:
        txt += add_paragraph(i) + '\n'
    return txt

def add_figure(path, name):
    txt = '''
		<div class="content_img"><img src="{path}" width="450"></div>
		<h6>{name}</h6>

'''.format(path=path, name=name)
    return txt


def add_figures(name, lists):
    txt = ''

    arr = lists[0].split(":")
    txt += '''
    <div class="albumSlider">
    <div class="fullview"> <img src="{default_figure}" alt="CNTRL1.IS" title="{sample}" /></div>
    <div class="slider">
    <div class="button movebackward" title="Up roll"></div>
    <div class="imglistwrap"><ul class="imglist">
'''.format(default_figure=arr[0].strip('\"'), sample=arr[1].strip('\"'))

    index = 0
    for i in lists:
        index = index + 1
        arr = i.split(":")
        txt += '''
        
        <li><a id="{href}" href='{href}' title="{sample}" data-gallery="#error"><img alt="{sample}" src="{file}" /></a></li>

'''.format(href=arr[0].strip('\"'), num=index, file=arr[0].strip('\"'), sample=arr[1].strip('\"'))

    txt += '''
    </ul>
    </div>
    <div class="button moveforward" title="Down roll"></div>
    </div>
    </div>
'''
    txt += '''
        <p class=\"name_fig\" style=\"clear:both\">{name}</p>    
    '''.format(name=name.strip('\"'))

    return txt


def add_blockquote(quotes):
    txt = '<blockquote>\n'
    for i in quotes:
        txt += i + "<br />\n"

    txt += '</blockquote>'
    return txt

def add_table(table): #table是一个元组：（名称，列表） 列表第一个元素为表头
    if table[1]:
        table_list = table[1]
        #out = 'Table&nbsp.&nbsp' + table[0] + '<br/>'
        #out += '<table class="tf2">'
        out = '''
        <h6>{table_name}</h6>
        <div class="content_table" >
		<table class="table table-bordered table-striped table-hover" >
        '''.format(table_name=table[0])

        for i in range(len(table_list)):

            # for head
            if i == 0:

                out += '''<thead><tr>\n'''
                for item in table_list[i]:
                    out += '''<th style="text-align :center">{item}</th>'''.format(item=item)

                out += '''</tr></thead>\n'''

            else:
                out += '''<tbody><tr>\n'''
                for item in table_list[i]:
                    out += '''<td style="text-align :center">{item}</td>'''.format(item=item)
                out += '''</tr></tbody>\n'''
                #for item in table_list[i]:
                #    if isinstance(item,list):
                #        out += '<td rowspan=' + str(item[1]) + '>' + item[0] + '</td>'
                #    else:
                #        out += '<td>'+ item + '</td>'
            #out += '</tr>'


        out += '</table>\n</div>\n'
    else:
        out = ""
    return out

def readTable(file):

    list1 = []
    flag1 = 1
    with open(file) as fo:
        for line in fo:
            line.strip('\n')
            if line != '':
                listT = line.split("\t")
                list1.append(listT)
    return list1

def addNote(lists):
    txt = ''
    txt += '''
    <p class="premark"><b>Note ： </b>
'''
    for i in lists:
        txt += i + '\n'

    txt += '''
    </p>
'''
    return txt

def add_table_note(line):
    txt = '''
<p align="left">{line}<p/>    
    '''.format(line=line)
    return txt


def add_blank_line(num):
    txt = ''
    for i in range(0, num):
        txt += '''
        <br />
'''
    return txt

def page_start(note, logo):
    txt = ''
    txt += '''
    <!--------------------------------------{note}----------------------------------------->
    <div id="page">
        <p class="head"><a href="#home" title = "返回首页"><img class="logo" align="left" src="{logo}" /></a>
        <a name="项目流程">Novogene Co., Ltd</a>
        <hr/>
        </p><br/>

    '''.format(note=note,logo=logo)
    return txt

def page_end():
    txt = ''
    txt += '''
        </div>
        <div id="page">
    </div>
'''
    return txt

def add_sections(name, herfs, sects, num):

    txt = ''

    if num == 1:

        txt += '''
                    <h3 id="{herf}" class="page-header">{num} {name}</h3>
        '''.format(name=name, herf=herfs[name][0], num=herfs[name][1])
    elif num == 2:
        txt += '''
                    <h4 id="{herf}">{num} {name}</h4>
        '''.format(name=name, herf=herfs[name][0], num=herfs[name][1])

    if name in sects:
        for ti in range(0, len(sects[name])):
            arr = sects[name][ti].split(":",1)

            if sects[name][ti].startswith("P0"):
                arr[1] = arr[1].strip('\"')
                txt += add_paragraph(arr[1])

            elif sects[name][ti].startswith("F0"):
                arr2 = arr[1].split(",")
                figure_path = arr2[0].strip('\"')
                figure_name = arr2[1].strip('\"')
                txt += add_figure(figure_path, figure_name)

            elif sects[name][ti].startswith("S0"):
                arr2 = arr[1].split(",")
                table_path = arr2[0].strip('\"')
                table_name = arr2[1].strip('\"')
                txt += add_table((table_name, readTable(table_path)))
                txt += add_blank_line(1)

            elif sects[name][ti].startswith("S1"):
                arr2 = arr[1].split(",")
                for si in range(0, len(arr2)):

                    txt += add_table_note(arr2[si].strip('\"'))

            elif sects[name][ti].startswith("MF0"):
                arr3 = arr[1].split(",")
                tmp_list = []
                for i in range(1, len(arr3)):
                    tmp_list.append(arr3[i])
                txt += add_figures(arr3[0], tmp_list)
                txt += add_blank_line(1)


    txt += add_blank_line(2)

    return txt


def start():
    txt = '''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">    
    '''
    return txt


def head(title):
    txt = set4head(title)
    return txt


def bar_start():
    txt = '''
    <body>
    
    <!-- For Slide -->
    <div id="blueimp-gallery" class="blueimp-gallery">
    <div class="slides"></div>
    <h3 class="title"></h3>
    <a class="prev">‹</a>
    <a class="next">›</a>
    <a class="close">×</a>
    <ol class="indicator"></ol>
    <div class="modal fade row">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" aria-hidden="true">&times;</button>
                    <h4 class="modal-title"></h4>
                </div>
                <div class="modal-body next"></div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-default pull-left prev">
                        Previous
                    </button>
                    <button type="button" class="btn btn-primary next">
                        Next
                    </button>
                </div>
            </div>
        </div>
    </div>
</div>

        <a class="sr-only sr-only-focusable" href="#content">Skip to main content</a>
            <!-- Docs page layout -->
        <div class="container bs-docs-container">
            <div class="row">
                <div class="col-md-3" id="left">
                    <div class="bs-docs-sidebar hidden-print hidden-xs hidden-sm affix" role="complementary">

                        <ul class="nav bs-docs-sidenav text-right">
    '''
    return txt


def bar_end():
    txt = '''
                        <div  style="position:relative;left:10%;bottom:-30px;padding-right: 20px;max-width: 230px;">
                            <a href="http://www.novogene.com/"><img src="static/image/novogene_logo.png" width="80%" style="margin-bottom: 20px"></a>
                            <p class="text-left" style="font-size: 12px"><i class="fa fa-phone-square fa-1x" aria-hidden="true"></i>&nbsp;&nbsp;TEL：400-658-1585</p>
                            <p class="text-left" style="font-size: 12px"><i class="fa fa-envelope-open fa-1x" aria-hidden="true"></i>&nbsp;&nbsp;E-mail：<a href="mailto:邮件地址">service@novogene.com</a></p>
                        </div>

				        </ul>

			        </div>
		        </div>
    '''
    return txt


def bar(bar_lists, herfs):
    txt = bar_start()

    for i in range(0, len(bar_lists)):

        herf_index = chr(ord('a') + i)
        num_index = str(i + 1)
        herfs[bar_lists[i][0]] = [herf_index, num_index]

        txt += '''
                        <li>
                            <a href="#{herf_index}" role="active">
                                <img src="{img}">
                                {num_index} {name}
                            </a>        
        '''.format(herf_index=herf_index, num_index=num_index, name=bar_lists[i][0], img=bar_lists[i][1])

        if len(bar_lists[i][2]) != 0:
            txt += '''
						    <ul class="nav">            
            '''
            for ii in range(0, len(bar_lists[i][2])):
                herf_index_sub = herf_index + '_' + str(ii + 1)
                num_index_sub = num_index + '.' + str(ii + 1)
                herfs[bar_lists[i][2][ii]] = [herf_index_sub, num_index_sub]

                txt += '''
                                <li><a href="#{herf_index_sub}">{num_index_sub} {name_sub}</a></li>
                '''.format(herf_index_sub=herf_index_sub, num_index_sub=num_index_sub, name_sub=bar_lists[i][2][ii])

            txt += '''
        					</ul>          
            '''

        txt += '''
					    </li>
        '''

    txt += bar_end()

    return txt


def cover(project_infos):
    txt = '''
		<!--内容部分-->
		<div class="col-md-9" role="main" id="main">
			<!--封面-->

			<p style ="text-align:left;padding-top:2%;padding-left:3%;font-size:15px">Project ID：{Project_ID}
			<br/>
			Report ID：{Report_ID}
			<br/>
			</p>

			<div class="text-center" data-section-name="home" id="cover" >
				<h2 style="padding-top: 12%">Project Name：{Project_Name}</h2>

				<br>
				<br>
				<br>


                <!--<h4 style="padding-top: 10%">合同编号：XXXX<h4/>-->
                <!--padding-top控制中间留白的大小，越大空白越大-->

				<p style ="text-align:center;padding-top:16%;font-size:15px">
				<h4 >Report Date：{Report_Date}</h4>
				<h4>项目负责：北京诺禾致源科技股份有限公司Denovo业务线</h4>
				<!--<hr style="margin-top: 22%; height:1px;border:none;border-top:1px dashed">-->
				</p>
			</div>

    '''.format(**project_infos)
    return txt


def Catalogue(project_infos):
    for k, v in project_infos.items():
        print(k)
        print(v)

    txt = '''
<!---------------------------------------- Catalogue ---------------------------------------------->
<div id="page">
    <p><a name="home"><img class="logo" src="src/images/immovable/logo.png" /></a><h1>Nanopore Sequencing QC Report</h1></p>
    <p class="paragraph">Project ID：{Project_ID}</p>
    <p class="paragraph">Project Name：{Project_Name}</p>
    <p class="paragraph">Report Date：{Report_Date}</p>
    <p class="paragraph">Report ID：{Report_ID}</p>
'''.format(**project_infos)

    txt += '''

    <h2>目录</a></h2>

    <p class="paragraph">

            <dt><a href="#Introduction">项目背景</a></dt>

					<dd><a href="#Nanopore Sequencing Platform">Nanopore测序平台</a></dd>
                    <dd><a href="#Nanopore Sequencing Mechanism">Nanopore测序原理</a></dd>
                    <dd><a href="#Nanopore Sequencing Advantage">Nanopore测序优势</a></dd>

         	<dt><a href="#Sequencing Workflow">建库测序流程</a>

                    <dd><a href="#Total RNA Sample Test">DNA样品检测</a></dd>
                    <dd><a href="#Library Construction">文库构建</a></dd>
                    <dd><a href="#Computer Sequencing">上机测序</a></dd>

            </dt>
			<dt><a href="#Results Presentation">结果展示及说明</a></dt>

                    <dd><a href="#Raw Data Processing">原始数据处理</a></dd>
                    <dd><a href="#Raw Data Summary">Nanopore数据统计</a></dd>

            <br /><br />
    </p>
</div>

'''
    return txt


def body_end():
    txt = '''

		<div class="col-md-2 hidden-print" title="TOP">
		<p><a href="report.html" target="_top">
			<button   type="button" class="btn" style="position: fixed;top: 55px;right: 0.5%" href="report.html" target="_top"><i class="fa fa-arrow-up fa-1x" aria-hidden="true"></i></button>
		</a></p>
		</div>


</div>
</div>
</div>
</div>

</body> 
    '''
    return txt


def main_body_start():
    txt = '''
        			<div class="bs-docs-section" id="content">   
    '''
    return txt


def sections(bar_lists, herfs, sects):
    txt = ''

    for i in range(0, len(bar_lists)):

        txt += add_sections(bar_lists[i][0], herfs, sects, 1)

        if len(bar_lists[2]) != 0:
            for ii in range(0, len(bar_lists[i][2])):
                txt += add_sections(bar_lists[i][2][ii], herfs, sects, 2)

    return txt


def end():
    txt = '''
</html>    
    '''
    return txt

def make_dirs(d):
    if not os.path.isdir(d):
        os.makedirs(d)
    elif not os.path.exists(d):
        print('The path is illegal:{} !!!!!\n'.format(d))
        os._exit(-1)