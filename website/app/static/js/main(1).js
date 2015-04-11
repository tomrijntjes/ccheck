(function($){
	$(function(){
		
		// ==================== start under footer ==================== //
		
			var xz=0;
			$("div.box1").hover(function(){
				if(xz==0){
					$(this).children("div.box_img").animate({"right":"-300px"},300);
					xz++;
				}else{
					$(this).children("div.box_img").animate({"right":0},300);
					xz--;
				}
				return false;
			});
		
		// ==================== end under footer ==================== //
		
		// ==================== start scroll ==================== //
		
			$('.scroll').click(function(){
				$('html, body').animate({scrollTop : 0},800);
				return false;
			});
			
		// ==================== end scroll ==================== //
		
		// ==================== start accordion ==================== //
		
		var ele = $("ul.accordion");
		var all_divs = ele.find("div");
		var all_anchor = ele.children("li").children("a");
		all_divs.slideUp();
		$("div.vraag ul.accordion:nth-child(2) li:first-child a").addClass("active").next().slideDown();
		
		all_anchor.click(function(){
		if($(this).next().is(":hidden")){
			all_divs.slideUp();
			all_anchor.removeClass("active");
			$(this).addClass("active").next().slideDown();
		}else{
			$(this).removeClass("active").next().slideUp();
		};
		return false;
		});
		
		// ==================== end accordion ==================== //
		
          // ==================== start options ==================== //
		
			var msie6 = jQuery.browser == 'msie' && jQuery.browser.version < 7;
				if (!msie6) {
				var top = jQuery('#options').offset().top - parseFloat(jQuery('#options').css('margin-top').replace(/auto/, 0));
				jQuery(window).scroll(function (event) {
				var y = jQuery(this).scrollTop();
				if (y >= top) {
				jQuery('#options').addClass('fixed');
				} else {
				jQuery('#options').removeClass('fixed');
				}
				});
			};
		
		// ==================== end options ==================== //
        
		// ==================== start map ==================== //
		//
//			$("#map").goMap({ 
//				zoom:10,
//				maptype: 'ROADMAP',
//				mapTypeControl: true, 
//				mapTypeControlOptions: { 
//					position: 'RIGHT', 
//					style: 'HORIZONTAL_BAR' 
//				}, 
//				markers: [{  
//					latitude: 51.657515, 
//					longitude: 5.293153, 
//					title: 'marker title 1' 
//                   
//				},{
//				     latitude: 51.863003, 
//					longitude: 5.771790, 
//					title: 'marker title 2' 
//				}
//                ]
//                
//			});
//				$.goMap.createMarker({
//					address: 'Kantoor Vught Kerkstraat 76 5261 CS Vught,Kantoor Beuningen Dorpssingel 12 6641 BE Beuningen' 
//			});
//			
		// ==================== end map ==================== //
		
      
	});
})(jQuery)