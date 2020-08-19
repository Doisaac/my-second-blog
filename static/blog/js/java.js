
$(document).ready(function(){
    AOS.init();
    $(window).scroll(function() {
        //ADD CLASS
        if ($(".navbar").offset().top > 50) {
           $(".navbar").addClass("top-nav-collapse");
        } else {
           $(".navbar").removeClass("top-nav-collapse");
        }
     });

     $('.flecha').click(function(){
        $('.move2').toggleClass("down");
        
        $(".flecha").toggleClass("far fa-times-circle",)
       
     
      });
      $('.move3').click(function(){
         $('.move4').toggleClass("down");
      
       });
       $('.move5').click(function(){
         $('.move6').toggleClass("down");
      
       });

       

     });
 

     var scroll = new SmoothScroll('a[href*="#"]', {speed: 1000, offset: 100, speedAsDuration: true});
     