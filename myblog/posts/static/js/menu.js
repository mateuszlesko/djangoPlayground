function openNav() {
    if(window.innerWidth > 600){
      document.getElementById("menuSidenav").style.width = "250px";
      document.getElementById("container").style.marginLeft = "250px";
    }
    else{
      document.getElementById("menuSidenav").style.width = "100%";
      document.getElementById("linkList").style.paddingLeft = "150px";
      document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
    }
      
  }
  
  function closeNav() {
    document.getElementById("menuSidenav").style.width = "0";
    if(window.innerWidth < 600){
      document.getElementById("linkList").style.paddingLeft = "0px";
      document.body.style.backgroundColor = "#e0dede";
    }
  }