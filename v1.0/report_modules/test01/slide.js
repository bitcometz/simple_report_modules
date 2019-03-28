/**
 * 幻灯片JS脚本
 */
$(function() {
    var SliderModule = (function() {
        var pb = {};
        pb.el = $('#slider');  //el表达式
        pb.items = {
            panel: pb.el.find('li')  // 获得li集合
        }

        // 变量
        var SliderInterval,
            currentSlider = 0,  //当前幻灯片
            nextSlider = 1,     //下一张
            lengthSlider = pb.items.panel.length;  // 幻灯片集合长度

        // 初始化
        pb.init = function(settings) {
            this.settings = settings || {duration: 8000}
            var output = '';  // 输出的html语言

            // 初始化
            SliderInit();

            for(var i = 0; i < lengthSlider; i++) {
                if (i == 0) {
                    output += '<li class="active"></li>';
                } else {
                    output += '<li></li>';
                }
            }

            // 单击按钮时切换图片
            $('#slider-controls').html(output).on('click', 'li', function (e){
                var $this = $(this);
                if (currentSlider !== $this.index()) {
                    changePanel($this.index());
                };
            });
        }

        // 初始化方法
        var SliderInit = function() {
            SliderInterval = setInterval(pb.startSlider, pb.settings.duration);
        }

        pb.startSlider = function() {
            var panels = pb.items.panel,
                controls = $('#slider-controls li');

            if (nextSlider >= lengthSlider) {
                nextSlider = 0;
                currentSlider = lengthSlider-1;
            }

            // 淡出淡入效果
            controls.removeClass('active').eq(nextSlider).addClass('active');
            panels.eq(currentSlider).fadeOut('slow');
            panels.eq(nextSlider).fadeIn('slow');

            // 设置当前幻灯片
            currentSlider = nextSlider;
            nextSlider += 1;
        }

        // 自动切换幻灯片
        var changePanel = function(id) {
            clearInterval(SliderInterval);
            var panels = pb.items.panel,
                controls = $('#slider-controls li');

            // 幻灯片头尾
            if (id >= lengthSlider) {
                id = 0;
            } else if (id < 0) {
                id = lengthSlider-1;
            }

            // 幻灯片淡出淡入
            controls.removeClass('active').eq(id).addClass('active');
            panels.eq(currentSlider).fadeOut('slow');
            panels.eq(id).fadeIn('slow');

            // 当前幻灯片和下一张
            currentSlider = id;
            nextSlider = id+1;

            //重新初始化
            SliderInit();
        }


        return pb;
    }());
    // 图片切换速度 4000毫秒
    SliderModule.init({duration: 4000});
});