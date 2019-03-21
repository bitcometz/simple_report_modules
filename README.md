
主要的作用是解析给定的html.txt 来生成html
默认目录层级为2级

可以根据例子中的asm.html.txt 来设置报告的内容
这样产品经理都可以设置好报告的内容，不需要修改程序, 运行程序即可得到相关的网页报告


通过最前面的标记不同的元素: T0:代表栏目的开始，一段文字(P0:)，一个图片(F0)，图片图注(F1)，表格(S0)，表格说明(S1)

其中的一些例子：

T0:"Nanopore 测序简介"
P0:"Nanopore 测序即纳米孔测序，其原理是：纳米孔蛋白  作为生物传感器，插入由合成聚合物形成的膜中。此外，核酸分子会与马达蛋白（Motor Proted...................(一段的内容为一行，以双引号结束)"

F0:"static/image/p1.png","图 1 Nanopore 测序原理"

T0:"Nanopore 原始数据统计"

P0:"对Nanopore 测序得到的原始数据采用软件NanoPlot 进行质控过滤异常值，我们对 下机得到的reads 统计结果见表1，质控后的reads 的统计结果见

S0:"data/wtdbg.table1.xls","表1 Nanopore原始测序数据统计"

S0:"data/wtdbg.table2.xls","表2 Nanopore用于组装数据统计"

T0:"BUSCO 评估"

P0:"BUSCO（Benchmarking Universal Single-Copy Orthologs：http://busco.ezlab.org/）评 估是使用单拷贝直系同源基因库，结合tblastn、augustu

S0:"data/busco.table1.xls","表4 BUSCO评估结果"

S1:"(1)Species：XX 物种；","(2)D：Complete Duplicated BUSCOs; F：Fragmented BUSCOs; M：Missing BUSCOs; n：Total BUSCO groups searched.:"

NOTE
相关的表动的图片和表格放在输出目录的data上，因为报告生成的时候需要载入这些图片表格

最终的结果会放在Reports文件夹下

华为云的例子路径如下：
/HWNAS12/RAD/zhangjinbo/01.release/00.reports/00.examples

下载本页的内容 ，请点击右上角的绿色框(Clone or Download)
