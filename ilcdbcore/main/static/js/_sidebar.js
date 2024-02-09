$(".custom-menu > ul > li").click(function (e) {
  // remove active from already active
  $(this).siblings().removeClass("custom-active");

  // add active to clicked
  $(this).toggleClass("custom-active");

  // if has sub menu open it
  $(this).find("ul").slideToggle();

  // close other sub menu
  $(this).siblings().find("ul").slideUp();

  // remove active class of sub menu
  $(this).siblings().find("ul").find("li").removeClass("custom-active");
});

$(".custom-menu-btn").click(function(){
    $(".custom-sidebar").toggleClass("custom-active");
});
