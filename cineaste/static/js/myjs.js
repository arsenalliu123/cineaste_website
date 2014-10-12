$(document).ready(function(){
	//Image hover
	$(".hover_img").live('mouseover',function(){
			var info=$(this).find("img");
			info.stop().animate({opacity:0.2},300);
		}
	);
	$(".hover_img").live('mouseout',function(){
			var info=$(this).find("img");
			info.stop().animate({opacity:1},300);
		}
	);
	$("button").click(function(){
        var uid = $("input").val();
        if(uid!=""){
          window.location.href=uid;
        }
      });
    $("input").keyup(function(event){
        var uid = $("input").val();
        if(event.keyCode == 13){
          $("button").click();
        }
        if(uid!=""){
          $("button").removeAttr("disabled");
        }
        else{
          $("button").attr("disabled","disabled");
        }
        });
});
