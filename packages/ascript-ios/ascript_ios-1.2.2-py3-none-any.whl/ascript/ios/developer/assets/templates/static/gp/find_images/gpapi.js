var gp;
var main;
var api;
var curren_path;
// var imgs = []
var task = {
    params: "",
    data: {
        imgs: []
    }
}

var module_img_list = []

// 当插件被加载后,此方法处于 document.ready后触发
function on_load(p_gp, gpapi) {
    gp = p_gp
    // main = window.parent;
    // api = main.gpapi;
    api = gpapi;

    var rect = api.image.get_rect()
    show_img(rect)

    $("#img_add_submit").click(function () {
        var img_name = $("#img_name").val().trim()
        var img_gppath = "res/img/" + img_name
        var gpfile = api.strack.file(img_gppath)
        api.file.copy(curren_path, gpfile.path)

        add_part_img(img_name, img_gppath)
        $("#find_img_rect").val("")
        mk_code()
    })

    $("#find_imgs_test").click(function () {
        test_find()
    })

    $("#find_imgs_submit").click(function () {
        submit_find();
    })

    $(".close_res").click(function () {
        // alert("1")
        $(".find_res_con").hide()
        api.marks.rect.clear()
    })

    $("#findimg_model,#ori_select,#findimg_mode").on("change", function () {
        mk_code()
    })

    $("#find_img_diff").blur(function(){
        mk_code()
    })

    $("#findimg_modules").on("change", function () {
        get_image_list()
    })

    $("#findimg_save_to_module").click(function () {
        var module_name = $("#findimg_modules option:selected").text()
        // 排查是否有重复的图片,如果有,提示覆盖,否则取消保存
        var aimglist = []
        task.data.imgs.forEach((img, index) => {
            module_img_list.forEach((aimg, index) => {
                if (img.name == aimg.name) {
                    aimglist.push(img.name)
                }
            })
        })

        if (aimglist.length > 0) {
            var userResponse = confirm(`以下图片名称已存在于工程中\n${aimglist.join(",")}\n是否覆盖?`)
            if (userResponse) {

            } else {
                return
            }
        }


        task.data.imgs.forEach(img => {
            var gpfile = api.strack.file(img.path)
            var target = `${api.file.path.model}${module_name}/res/img/${img.name}`
            // var target = api.strack.res(`/res/img/${img.name}`)
            // alert(target)
            api.file.copy(gpfile.path, target, function () {
                api.sys.alert("保存成功")
            })
        });
    })

    api.module.get_all(function (data) {
        $("#findimg_modules").empty();
        // if(data.data.length<1){
        //     $("#model_create").click();
        //     return;
        // }
        data.data.forEach((e, index) => {
            var item = $(`<option value="1">${e.name}</option>`);
            $("#findimg_modules").append(item);
            if (index == 0) {
                get_image_list()
            }
        });
    })

    $("#findimg_code").dblclick(function () {
        var val = $("#findimg_code").val();
        copy(val)
        api.sys.alert("复制:" + val)
    })

    $.contextMenu({
        selector: "#findimg_code",
        trigger: 'right',
        // define the elements of the menu
        items: {
            copy_params: {
                name: "复制参数", callback: function (key, opt) {
                    var c_params = make_single_params()
                    copy(c_params)
                    api.sys.alert("复制:"+c_params)
                    // , opt.$trigger.text()
                    //   alert(opt.$trigger.attr("i"))
                    // opt.$trigger.remove()
    
                }
            },
            copy_all: {
                name: "复制全部", callback: function (key, opt) {
                    var val = $("#findimg_code").val();
                    copy(val)
                    api.sys.alert("复制:"+val)
                    // , opt.$trigger.text()
                    //   alert(opt.$trigger.attr("i"))
                    // opt.$trigger.remove()
    
                }
            },
        }
        // there's more, have a look at the demos and docs...
    });
}

// 当iframe 再次被打开后
function on_reload(p_gp) {
    gp = p_gp
    if (gp.data.data.imgs.length > 0) {
        // alert("有数据")
        task = gp.data
        $("#image_list").empty();
        gp.data.data.imgs.forEach((img, index) => {
            add_part_img_dom(img.path, img.name)
        });

        if (gp.data.data.rect) {
            $("#find_img_rect").val(gp.data.data.rect)
        }

        if (gp.data.data.diff) {
            $("#find_img_diff").val(gp.data.data.diff)
        }

        if (gp.data.data.mode) {
            $("#ori_select").val(gp.data.data.mode)
        }

        if (gp.data.data.maxcnt) {
            $("#findimg_model").val(gp.data.data.maxcnt)
        }

    }
}

function on_wipe(){
    // $(".img_item_des").attr("src",this.attr("src"))
    $('.img_item_des').each(function() {  
        var img = $(this);  
        var src = img.attr('src');  
        img.attr('src', ''); // 先设置为空字符串，以清除可能的缓存  
        img.attr('src', src); // 再设置为原来的src，触发重新加载  
    });
}

// 当主图范围变化后
function on_rect(rect) {
    show_img(rect)
    $("#find_img_rect").val(rect)
    mk_code()
}

// 当 调用 main_window.gpapi.strack.add() 后得到数据接口,返回后调用此方法
function on_data(data) {
    $("#find_colors_test_loading").hide()
        $(".find_res_con").show()
       if (data.data.length < 1) {
                alert("没找到任何结果")
                $(".find_res").empty()
                $("#res_no").text(`共找到:${res.data.data.length}个匹配图`)
                return
            }

            $(".find_res").empty()

            // alert(mydata.data[0]["rectangle"][0]+mydata.data[0]["rectangle"][1])
            data.data.forEach((p, index) => {
                var rect = [p["rectangle"][0][0], p["rectangle"][0][1], p["rectangle"][3][0], p["rectangle"][3][1]]
                api.marks.rect.add(index + 1, rect)

                var res_item = $("#find_res_item").clone()
                res_item.appendTo(".find_res")
                res_item.find(".find_res_item_no").text(index + 1)
                res_item.find(".find_res_item_diff").text(Math.floor(Number(p["confidence"]) * 100) / 100)
                res_item.find(".find_res_item_rect").text(`[${rect}]`)
            });

            $("#res_no").text(`共找到:${data.data.length}个匹配图`)
}

// 当在 主图上,按下按键后,调用此方法
function on_color(key, color) {

}
// ------------- add part img
function show_img(rect) {
    if (rect && rect.length > 0) {
        api.image.crop(function (data) {
            // alert(api.file.url(data))
            $("#img_des").attr("src", api.file.url(data))
            $("#img_name").val(auto_create_imgname())
            curren_path = data;
        }, rect,)
    }
}

function auto_create_imgname() {
    var mk_name_success = false
    var ima_no = task.data.imgs.length + 1
    var prename = ""
    while (!mk_name_success) {
        prename = ima_no + ".png"
        var has_same = false;
        module_img_list.forEach((e, index) => {
            if (e.name == prename) {
                ima_no = ima_no + 1
                has_same = true
                return
            }
        })

        task.data.imgs.forEach((img, index) => {
            if (img.name == prename) {
                ima_no = ima_no + 1
                has_same = true;
                return;
            }
        });

        if (!has_same) {
            mk_name_success = true;
        }
    }
    return prename
}

function add_part_img(img_name, img_path) {

    // if (!curren_path) {
    //     alert("请先‘鼠标括选’要找的图")
    //     return;
    // }

    // if (img_name.length < 1) {
    //     alert("缺少图片名称")
    //     return;
    // }

    var has_same = false;

    task.data.imgs.forEach((img, index) => {
        if (img.name == img_name) {
            has_same = true;
            return;
        }
    });

    if (has_same) {
        alert("已经存在相同的名称")
        return;
    }

    task.data.imgs.push({
        path: img_path,
        name: img_name
    })



    add_part_img_dom(img_path, img_name);
}

function add_part_img_dom(img_path, img_name) {
    var gpfile = api.strack.file(img_path);

    var idom = $("#image_list_item").clone();

    var timestamp = new Date().getTime();  

    idom.find(".img_item_des").attr("src", gpfile.url+ '&cache=' + timestamp);

    idom.find(".img_item_des").click(function () {
        api.image.show(gpfile.path)
        
        $(this).attr("src", gpfile.url);
    })

    idom.find(".img_item_des_name").text(img_name);

    idom.find(".img_item_des_name").attr("p",img_path)

    idom.find(".img_item_des_name").click(function () {
        // alert("1")
        var name = $(this).text();
        var get_name = false;

        var c_img_path = $(this).attr("p")

        var user_res = prompt(`修改名称 ${name}`, name);
        if (user_res) {
            var has_same = false;
            var fix_pos = -1;
            task.data.imgs.forEach((element, index) => {
                if (element.name == user_res) {
                    alert("存在相同");
                    has_same = true;
                    return;
                }

                if (element.path == c_img_path) {
                    fix_pos = index;
                }
            });

            if (!has_same) {
                if (fix_pos > -1) {
                    task.data.imgs[fix_pos].name = user_res;
                    var gpfile = api.strack.file(task.data.imgs[fix_pos].path);
                    task.data.imgs[fix_pos].path = "res/img/" + user_res
                    $(this).attr("p",task.data.imgs[fix_pos].path)
                    api.file.rname(gpfile.path, user_res, function (res) {
                        // alert(JSON.stringify(res));
                    });

                    $(this).text(user_res);
                } else {
                    alert("没有找到对应名称的条目");
                }

                get_name = true;

            }
        } else {
            get_name = true;
        }
    });

    idom.find(".img_item_des_del").click(function () {
        idom.remove();
        var delindex = -1;
        task.data.imgs.forEach((img, index) => {
            if (img.name == img_name) {
                delindex = index;
                return;
            }
        });

        if (delindex > -1) {
            task.data.imgs.splice(delindex, 1);
        }

        var img_gppath = "res/img/" + img_name
        var gpfile = api.strack.file(img_gppath)
        api.file.delete(gpfile.path)

    });

    idom.appendTo("#image_list");
}

function make_data() {

    task.data["rect"] = undefined
    task.data["diff"] = undefined
    task.data["mode"] = undefined

    task.params = "";

    var img_paths = "["
    task.data.imgs.forEach(img => {
        img_paths = img_paths + `R.rel(__file__,"res/img/${img.name}"),`
    });
    img_paths = img_paths + "]"

    task.params = task.params + img_paths

    var rect_str = $("#find_img_rect").val().trim()
    if (rect_str.length > 0) {
        task.params = task.params + `,rect= (${rect_str}) `
        task.data["rect"] = rect_str
    }

    var diff_str = $("#find_img_diff").val().trim()
    if (diff_str.length > 0 && diff_str != "0.5") {
        task.params = task.params + `,confidence= ${diff_str}`
        task.data["diff"] = diff_str
    }

    var mode = $("#ori_select").val()
    if (mode != 1) {
        // data.push(`$rgb= True`)
        task.params = task.params + `,rgb= True`
        task.data["mode"] = mode
    }

    var maxcnt = $("#findimg_model").val()
    if (maxcnt != 0) {
        // data.push(`$rgb= True`)
        task.params = task.params + `,num= ${maxcnt}`
        task.data["maxcnt"] = maxcnt
    }

    var mode = $("#findimg_mode").val()
    if (mode != 0) {
        // data.push(`$rgb= True`)
        task.params = task.params + `,mode= ${mode}`
        task.data["mode"] = mode
    }

    return task
}

function make_single_params() {

    var params = ""

    task.data["rect"] = undefined
    task.data["diff"] = undefined
    task.data["mode"] = undefined

    params = "";

    var img_paths = "["
    task.data.imgs.forEach(img => {
        img_paths = img_paths + `R.img("${img.name}"),`
    });
    img_paths = img_paths + "]"

    params = params + img_paths

    var rect_str = $("#find_img_rect").val().trim()
    if (rect_str.length > 0) {
        params = params + `,rect= [${rect_str}] `
    }

    var diff_str = $("#find_img_diff").val().trim()
    if (diff_str.length > 0 && diff_str != "0.5") {
        params = params + `,confidence= ${diff_str}`
    }

    var mode = $("#ori_select").val()
    if (mode != 1) {
        // data.push(`$rgb= True`)
        params = params + `,rgb= True`
    }

    return params
}

function test_find() {

    if (task.data.imgs.length < 1) {
        alert("请先添加要查找的子图片")
        return;
    }

    api.marks.rect.clear()

    make_data()

    $("#find_colors_test_loading").show()

    api.strack.test(task, function (res) {
        // alert(JSON.stringify(mydata))
        $("#find_colors_test_loading").hide()
        $(".find_res_con").show()
        if (res.code == 1) {
            if (res.data.data.length < 1) {
                alert("没找到任何结果")
                $(".find_res").empty()
                $("#res_no").text(`共找到:${res.data.data.length}个匹配图`)
                return
            }

            $(".find_res").empty()

            // alert(mydata.data[0]["rectangle"][0]+mydata.data[0]["rectangle"][1])
            res.data.data.forEach((p, index) => {
                var rect = [p["rectangle"][0][0], p["rectangle"][0][1], p["rectangle"][3][0], p["rectangle"][3][1]]
                api.marks.rect.add(index + 1, rect)

                var res_item = $("#find_res_item").clone()
                res_item.appendTo(".find_res")
                res_item.find(".find_res_item_no").text(index + 1)
                res_item.find(".find_res_item_diff").text(Math.floor(Number(p["confidence"]) * 100) / 100)
                res_item.find(".find_res_item_rect").text(`[${rect}]`)
            });

            $("#res_no").text(`共找到:${res.data.data.length}个匹配图`)


        } else {
            alert(res.msg)
        }
    })
}

function submit_find() {
    if (task.data.imgs.length < 1) {
        alert("请先添加要查找的子图片")
        return;
    }

    api.marks.rect.clear()

    make_data()

    $("#find_colors_test_loading").show()
    api.strack.add(task)
}

function save_all_img() {
    // alert("1")
    // var module_name = $("#findimg_modules option:selected").text()
    task.data.imgs.forEach(img => {
        var source = img.path
        // var target = `${api.file.path.model}${module_name}/res/img/${img.name}`
        var target = api.strack.res(`/res/img/${img.name}`)
        // alert(target)
        api.file.copy(source, target, function () {
            api.sys.alert("保存成功")
        })
    });
}

function remove_img_item(img_name) {
    var delindex = -1;
    task.data.imgs.forEach((img, index) => {
        if (img.name == img_name) {
            delindex = index;
            return;
        }
    });

    if (delindex > -1) {
        task.data.imgs.splice(delindex, 1);
    }
}

function get_image_list() {
    var module_name = $("#findimg_modules option:selected").text()
    var path = api.file.path.concat([api.file.path.model, `${module_name}/res/img/`])
    // alert(path)
    api.file.dir(path, function (res) {
        if (res.code == 1) {
            // console.log(res.data)
            module_img_list = res.data.childs
            // res.data.forEach((e,index)=>{
            //     var item = $("#imgname-item").clone();
            //     item.appendTo("#img_names")
            // })

            // alert(JSON.stringify(module_img_list,0,2))
            module_img_list.forEach((img, index) => {
                // alert(JSON.stringify(img))
                var item = $("#imgname-item").clone();
                item.text(img.name)
                item.click(function () {
                    // alert($(this).text())
                    $("#img_name").val($(this).text())
                })
                item.appendTo("#img_names")
            });

        } else {
            // alert(res.msg)
        }
    })
}

function mk_code() {
    var method = "find_all_template"

    var val_mode = $("#findimg_model").val();
    var val_num = $("#findimg_mode").val();
    

    if (val_mode == "1") {
        if(val_num=="0"){
            method = "find_template"
        }else if(val_num=="1"){
            method = "find_sift"
        }else{
            method = "find"
        }
    }else{
        if(val_num=="0"){
            method = "find_all_template"
        }else if(val_num=="1"){
            method = "find_all_sift"
        }else{
            method = "find_all"
        }
    }

    var fcode = `FindImages(${make_single_params()}).${method}()`

    $("#findimg_code").val(fcode)

}

function copy(msg){
    // alert(msg)
    var createInput = document.createElement("input");
    createInput.value = msg;
    document.getElementById("gp_con").appendChild(createInput);
    createInput.select();
    document.execCommand("Copy");
    createInput.className = 'createInput';
    createInput.style.display = "none";

    // alert(createInput.value)
}