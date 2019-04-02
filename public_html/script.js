$.fn.mosGame = function(options){
	return this.each(function(){
		var basic = {
			start : function(){
				$box = $("#box");
				$mos = $("#mos");
				$mos2 = $("#mos2");
				$mos3 = $("#mos3");
				$mos4 = $("#mos4");
				$mos5 = $("#mos5");
				$mos6 = $("#mos6");
				$mos7 = $("#mos7");
				$play = $("#play");
				$scoreBox = $("#scoreBox> strong");
				w = $box.width()-100;
				h = $box.height()-120;
				score = 0;
			},
			startTheMogi : function(){
				$play.on("click", function(){
					basic.gameStart();
					basic.clickMos();
					$('audio#mogi')[0].play()
				});
			},

			gameStart : function(){
				timer1 = setInterval(function(){
					var x = parseInt(Math.random()*w);
					var y = parseInt(Math.random()*h);
					var x2 = parseInt(Math.random()*w);
					var y2 = parseInt(Math.random()*h);
					var x6 = parseInt(Math.random()*w);
					var y6 = parseInt(Math.random()*h);
		
					$mos.animate({
						"left":x,
						"top":y
					});
					$mos2.animate({
						"left":x2,
						"top":y2
					});
					$mos6.animate({
						"left":x2,
						"top":y2
					});
				}, 800);
				
				timer2 = setInterval(function(){
					var x5 = parseInt(Math.random()*w);
					var y5 = parseInt(Math.random()*h);
					var x7 = parseInt(Math.random()*w);
					var y7 = parseInt(Math.random()*h);
					$mos5.animate({
						"left":x5,
						"top":y5
					});
					$mos7.animate({
						"left":x7,
						"top":y7
					});
				}, 500);
				
				timer3 = setInterval(function(){
					var x3 = parseInt(Math.random()*w);
					var y3 = parseInt(Math.random()*h);
					var x4 = parseInt(Math.random()*w);
					var y4 = parseInt(Math.random()*h);
					$mos3.animate({
						"left":x3,
						"top":y3
					});
					$mos4.animate({
						"left":x4,
						"top":y4
					});
				}, 1000);

				setTimeout(function(){
					if(timer1 != 0){
						clearInterval(timer1);
					}
					if(timer2 != 0){
						clearInterval(timer2);
					}
					if(timer3 != 0){
						clearInterval(timer3);
					}
					var lefter = parseInt(7-score)
					basic.clickMos();
					if (score==7){
						alert("You catched all the mosquitos. Now you can sleep in your bed!");
					}
					if (score!=7){
						alert("Still " +lefter+" mosquitos left in your room. You can try again!");
						location.reload();
					} 
					score = 0 ;
					$mos.off("click");
					$mos2.off("click");
					$mos3.off("click");
					$mos4.off("click");
					$mos5.off("click");
					$mos6.off("click");
					$mos7.off("click");
					$play.off("click");

				}, 16600);
			},
			clickMos : function(){
				$mos.on("click", function(){
					$mos.fadeOut(100)
					score += 1;
					$scoreBox.html(score);
					$('audio#pop')[0].play()
				});
				$mos2.on("click", function(){
					$mos2.fadeOut(100)
					score += 1;
					$scoreBox.html(score);
					$('audio#pop')[0].play()
				});
				$mos3.on("click", function(){
					$mos3.fadeOut(100)
					score += 1;
					$scoreBox.html(score);
					$('audio#pop')[0].play()
				});
				$mos4.on("click", function(){
					$mos4.fadeOut(100)
					score += 1;
					$scoreBox.html(score);
					$('audio#pop')[0].play()
				});
				$mos5.on("click", function(){
					$mos5.fadeOut(100)
					score += 1;
					$scoreBox.html(score);
					$('audio#pop')[0].play()
				});
				$mos6.on("click", function(){
					$mos6.fadeOut(100)
					score += 1;
					$scoreBox.html(score);
					$('audio#pop')[0].play()
				});
				$mos7.on("click", function(){
					$mos7.fadeOut(100)
					score += 1;
					$scoreBox.html(score);
					$('audio#pop')[0].play()
				});
				$scoreBox.html(score);
			}
		}
		basic.start();
		basic.startTheMogi();
	});
}
$(function(){
	$("#mosGame").mosGame();
});



 
