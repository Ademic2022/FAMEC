window.onload = function(){
    const sidebar = document.querySelector(".sidebar");
    const closeBtn = document.querySelector("#btn");
    const searchBtn = document.querySelector(".bx-search")

    $('.ui.dropdown').dropdown();

    $('.message .close').on('click', function() {
        $(this)
          .closest('.message')
          .transition('fade');
    });

    $(function(){
        $("#new_task").click(function(){
            $(".new_task").modal('show');
        });
        $(".new_task").modal({
            closable: true
        });
    });

    closeBtn.addEventListener("click",function(){
        sidebar.classList.toggle("open")
        menuBtnChange()
    })

    searchBtn.addEventListener("click",function(){
        sidebar.classList.toggle("open")
        menuBtnChange()
    })

    function menuBtnChange(){
        if(sidebar.classList.contains("open")){
            closeBtn.classList.replace("bx-menu","bx-menu-alt-right")
        }else{
            closeBtn.classList.replace("bx-menu-alt-right","bx-menu")
        }
    }
}