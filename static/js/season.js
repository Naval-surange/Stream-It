function myFunction() {
  var dots = document.getElementById("dots");
  var moreText = document.getElementById("more");
  var btnText = document.getElementById("myBtn");
  var card = document.getElementById("card-body");
  if (dots.style.display === "none") {
    dots.style.display = "inline";
    btnText.innerHTML = "Read More ▼";
    moreText.style.display = "none";
  } else {
    dots.style.display = "none";
    btnText.innerHTML = "Read less ▲";
    moreText.style.display = "inline";
  }
}

function update(sNo, data) {
  sNos = sNo.toString();
  img_i = document.getElementsByClassName("opaque")[0];

  img_i.classList.remove("opaque");

  img_f = document.getElementById("season" + sNo.toString());

  img_f.classList.add("opaque");

  desc = document.getElementById("seasonDesc");

  desc.innerHTML = `
                   <div class="sNo">
                      Season ${sNo}
                   </div>
                   Number of epsodes : ${data["seasons"][sNos]["No episodes"]}
                   <div class="sDesc">
                      ${data["seasons"][sNos]["desc"]}
                   </div>
                  `;
}

function redirectToEpisodes() {}
