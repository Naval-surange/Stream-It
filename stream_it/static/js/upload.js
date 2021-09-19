window.onload = function () {
  let selected_series = document.getElementById("series");
  let selected_season = document.getElementById("season");
  selected_series.onchange = function () {
    series = selected_series.value;
    fetch("/getSeasons/" + series).then(function (response) {
      response.json().then(function (data) {
        let optionHTML = "";
        for (let season of data.seasons) {
          optionHTML +=
            '<option value="' + season.id + '">' + season.number + "</option>";
        }
        selected_season.innerHTML = optionHTML;
      });
    });
  };
};
