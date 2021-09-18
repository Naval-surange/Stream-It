function myFunction() {
  var dots = document.getElementById("dots");
  var moreText = document.getElementById("more");
  var btnText = document.getElementById("myBtn");

  if (dots.style.display === "none") {
    dots.style.display = "inline";
    btnText.innerHTML = "Read More ▼";
    moreText.style.display = "none";
  } else {
    dots.style.display = "none";
    // dots.style.visibility = "hidden";
    btnText.innerHTML = "Read less ▲";
    moreText.style.display = "inline";
  }
}

function update(sNo,ses_data) {

  id = "right" + sNo.toString()

  toshow = document.getElementById(id)
  current = document.getElementsByClassName('visible')[0]

  current.classList.remove("visible")
  current.classList.add("hidden")
  
  toshow.classList.add("visible")
  toshow.classList.remove("hidden")

}


