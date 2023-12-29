$(function () {
  $("#datepicker").datepicker({
    dateFormat: "yy-mm-dd",
    onSelect: function (dateText, inst) {
      updateYValue();
    },
  });

  $("#update-chart").click(function () {
    updateYValue();
  });

  $("#temperature-btn").click(function () {
    updateYValue("temperature");
  });

  $("#current-btn").click(function () {
    updateYValue("current");
  });

  $("#vibration-btn").click(function () {
    updateYValue("vibration");
  }); 
});


function updateYValue(selectedY, viewType) {
  var selectedDate = $("#datepicker").val();
  var viewType = $("#view-type").val();
  // var dataType = $("#data-type").val();
  var url = viewType === "daily" ? "get-data-daily/" : "get-data-weekly/";
  var valueFormatString = viewType === "daily" ? "HH:mm" : "DDDD";

  $.ajax({
    type: "GET",
    url: url,
    data: { selected_date: selectedDate },
    success: function (data) {
      drawChart(data, valueFormatString, selectedY);
    },
  });
}

// function updateYValue(selectedY, viewType) {
//   var selectedDate = $("#datepicker").val();
//   var viewType = $("#view-type").val();
//   var url = viewType === "daily" ? "get-data-daily/" : "get-data-weekly/";
//   var valueFormatString = viewType === "daily" ? "HH:mm" : "DDDD";

//   fetch(`${url}?selected_date=${selectedDate}`)
//     .then(response => response.json())
//     .then(data => {
//       drawChart(data, valueFormatString, selectedY);
//     })
//     .catch(error => {
//       console.error('Error fetching data:', error);
//     });
// }

function drawChart(data, valueFormatString, selectedY) {
  try {
    var chart = new CanvasJS.Chart("chartContainer", {
      title: {
        text: selectedY + " Chart",
      },
      axisX: {
        title: "Time",
        valueFormatString: valueFormatString,
        // labels: viewType == "daily" ? dailyLabels : weeklyLabels,
      },
      axisY: {
        title: selectedY,
      },
      toolTip: {
        shared: true,
      },
      legend: {
        cursor: "pointer",
        verticalAlign: "top",
        horizontalAlign: "center",
        dockInsidePlotArea: true,
      },
      data: [
        {
          type: "line",
          name: selectedY,
          // showInLegend: true,
          xValueType: "dateTime",
          xValueFormatString: "DD MMM YYYY, HH:mm:ss",
          dataPoints: data.map(function (item) { 
            return { x: new Date(item.x), y: item["y_" + selectedY] };
          }),
        },
      ],
    });
    setInterval(drawChart, 5000)
    chart.render();
  } catch(error) {
    console.error(error);
  }
}
