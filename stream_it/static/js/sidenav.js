let bakcol1 = "#272829";
let bakcol2 = "#43455c";
let bakcol3 = "#707793";
let textcol1 = "#3bba9c";
let textcol2 = "#FFFFFF";

function toggleNav() {
  if (document.getElementById("mySidenav").style.width == "250px") {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("main").style.marginLeft = "0";
    document.body.style.backgroundColor = bakcol1;
  } else {
    document.getElementById("mySidenav").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
  }
}
/* Set the width of the side navigation to 0 and the left margin of the page content to 0, and the background color of body to white */
function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
  document.getElementById("main").style.marginLeft = "0";
  document.body.style.backgroundColor = bakcol1;
}
