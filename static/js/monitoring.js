//all variables are stored here
const vibrationXPlusMinBtn = {
  upper: {
    min: document.getElementById("vibration-X-upper-min"),
    plus: document.getElementById("vibration-X-upper-plus"),
  },
  lower: {
    min: document.getElementById("vibration-X-lower-min"),
    plus: document.getElementById("vibration-X-lower-plus"),
  },
};
const vibrationYPlusMinBtn = {
  upper: {
    min: document.getElementById("vibration-Y-upper-min"),
    plus: document.getElementById("vibration-Y-upper-plus"),
  },
  lower: {
    min: document.getElementById("vibration-Y-lower-min"),
    plus: document.getElementById("vibration-Y-lower-plus"),
  },
};

const vibrationZPlusMinBtn = {
  upper: {
    min: document.getElementById("vibration-Z-upper-min"),
    plus: document.getElementById("vibration-Z-upper-plus"),
  },
  lower: {
    min: document.getElementById("vibration-Z-lower-min"),
    plus: document.getElementById("vibration-Z-lower-plus"),
  },
};

const currentPlusMinBtn = {
  upper: {
    min: document.getElementById("current-upper-min"),
    plus: document.getElementById("current-upper-plus"),
  },
  lower: {
    min: document.getElementById("current-lower-min"),
    plus: document.getElementById("current-lower-plus"),
  },
};
const temperaturePlusMinBtn = {
  upper: {
    min: document.getElementById("temperature-upper-min"),
    plus: document.getElementById("temperature-upper-plus"),
  },
  lower: {
    min: document.getElementById("temperature-lower-min"),
    plus: document.getElementById("temperature-lower-plus"),
  },
};

const vibrationXUpper = document.getElementById("vibration-X-upper");
const vibrationXLower = document.getElementById("vibration-X-lower");
const vibrationYUpper = document.getElementById("vibration-Y-upper");
const vibrationYLower = document.getElementById("vibration-Y-lower");
const vibrationZUpper = document.getElementById("vibration-Z-upper");
const vibrationZLower = document.getElementById("vibration-Z-lower");
const currentUpper = document.getElementById("current-upper");
const currentLower = document.getElementById("current-lower");
const temperatureUpper = document.getElementById("temperature-upper");
const temperatureLower = document.getElementById("temperature-lower");
const calVibX = document.getElementById("cal-vib-x");
const calVibY = document.getElementById("cal-vib-y");
const calVibZ = document.getElementById("cal-vib-z");

getMonitoringData();

//function to handle click upper and lower button
function handleClickPlusMin(event) {
  const clickedId = event.currentTarget.id;

  function updateVibrationXUpper() {
    vibrationXUpper.textContent = clickedId.startsWith("vibration-X-upper")
      ? clickedId.endsWith("plus")
        ? (parseFloat(vibrationXUpper.textContent) + 0.1).toFixed(2)
        : (parseFloat(vibrationXUpper.textContent) - 0.1).toFixed(2)
      : parseFloat(vibrationXUpper.textContent);
  }
  function updateVibrationXLower() {
    vibrationXLower.textContent = clickedId.startsWith("vibration-X-lower")
      ? clickedId.endsWith("plus")
        ? (parseFloat(vibrationXLower.textContent) + 0.1).toFixed(2)
        : (parseFloat(vibrationXLower.textContent) - 0.1).toFixed(2)
      : parseFloat(vibrationXLower.textContent);
  }

  function updateVibrationYUpper() {
    vibrationYUpper.textContent = clickedId.startsWith("vibration-Y-upper")
      ? clickedId.endsWith("plus")
        ? (parseFloat(vibrationYUpper.textContent) + 0.1).toFixed(2)
        : (parseFloat(vibrationYUpper.textContent) - 0.1).toFixed(2)
      : parseFloat(vibrationYUpper.textContent);
  }
  function updateVibrationYLower() {
    vibrationYLower.textContent = clickedId.startsWith("vibration-Y-lower")
      ? clickedId.endsWith("plus")
        ? (parseFloat(vibrationYLower.textContent) + 0.1).toFixed(2)
        : (parseFloat(vibrationYLower.textContent) - 0.1).toFixed(2)
      : parseFloat(vibrationYLower.textContent);
  }

  function updateVibrationZUpper() {
    vibrationZUpper.textContent = clickedId.startsWith("vibration-Z-upper")
      ? clickedId.endsWith("plus")
        ? (parseFloat(vibrationZUpper.textContent) + 0.1).toFixed(1)
        : (parseFloat(vibrationZUpper.textContent) - 0.1).toFixed(1)
      : parseFloat(vibrationZUpper.textContent);
  }
  function updateVibrationZLower() {
    vibrationZLower.textContent = clickedId.startsWith("vibration-Z-lower")
      ? clickedId.endsWith("plus")
        ? (parseFloat(vibrationZLower.textContent) + 0.1).toFixed(1)
        : (parseFloat(vibrationZLower.textContent) - 0.1).toFixed(1)
      : parseFloat(vibrationZLower.textContent);
  }

  function updateCurrentUpper() {
    currentUpper.textContent = clickedId.startsWith("current-upper")
      ? clickedId.endsWith("plus")
        ? (parseFloat(currentUpper.textContent) + 0.1).toFixed(1)
        : (parseFloat(currentUpper.textContent) - 0.1).toFixed(1)
      : parseFloat(currentUpper.textContent);
  }

  function updateCurrentLower() {
    currentLower.textContent = clickedId.startsWith("current-lower")
      ? clickedId.endsWith("plus")
        ? (parseFloat(currentLower.textContent) + 0.1).toFixed(1)
        : (parseFloat(currentLower.textContent) - 0.1).toFixed(1)
      : parseFloat(currentLower.textContent);
  }

  function updateTemperatureUpper() {
    temperatureUpper.textContent = clickedId.startsWith("temperature-upper")
      ? clickedId.endsWith("plus")
        ? (parseFloat(temperatureUpper.textContent) + 0.5).toFixed(1)
        : (parseFloat(temperatureUpper.textContent) - 0.5).toFixed(1)
      : parseFloat(temperatureUpper.textContent);
  }

  function updateTemperatureLower() {
    temperatureLower.textContent = clickedId.startsWith("temperature-lower")
      ? clickedId.endsWith("plus")
        ? (parseFloat(temperatureLower.textContent) + 0.5).toFixed(1)
        : (parseFloat(temperatureLower.textContent) - 0.5).toFixed(1)
      : parseFloat(temperatureLower.textContent);
  }
  updateVibrationXUpper();
  updateVibrationXLower();
  updateVibrationYUpper();
  updateVibrationYLower();
  updateVibrationZUpper();
  updateVibrationZLower();
  updateCurrentUpper();
  updateCurrentLower();
  updateTemperatureUpper();
  updateTemperatureLower();
  updateData();
}

// ============================= POST AND GET DATA TO OR FROM DJANGO ===============================
// Funtion to get monitoring data
async function getMonitoringData() {
  try {
    const response = await fetch("/setting/monitoring/get-monitoring-data/");
    if (!response.ok) {
      throw new Error("Gagal mengambil data");
    }
    const data = await response.json();

    // Update Upper and Lower
    for (let key in data["upperAndLower"]) {
      const element = document.getElementById(key);
      if (data["upperAndLower"].hasOwnProperty(key)) {
        element.textContent = data["upperAndLower"][key];
      }
    }
  } catch (error) {
    console.error("Terjadi kesalahan saat mengambil data:", error);
  }
}

async function updateData() {
  // POST data to database

  // Get the csrfToken (THIS IS IMPORTANT! DO NOT DELETE!)
  function getCookie(name) {
    const cookieValue = document.cookie.match("(^|;)\\s*" + name + "\\s*=\\s*([^;]+)");
    return cookieValue ? cookieValue.pop() : "";
  }

  const csrfToken = getCookie("csrftoken");

  try {
    const response = await fetch("post-monitoring-data/", {
      method: "post",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrfToken,
      },
      body: JSON.stringify({
        upperAndLower: {
          vibration_X_upper: vibrationXUpper.textContent,
          vibration_X_lower: vibrationXLower.textContent,
          vibration_Y_upper: vibrationYUpper.textContent,
          vibration_Y_lower: vibrationYLower.textContent,
          vibration_Z_upper: vibrationZUpper.textContent,
          vibration_Z_lower: vibrationZLower.textContent,
          current_upper: currentUpper.textContent,
          current_lower: currentLower.textContent,
          temperature_upper: temperatureUpper.textContent,
          temperature_lower: temperatureLower.textContent,
        },
      }),
    });

    if (!response.ok) {
      throw new Error("Network response was not OK");
    }

    const responseData = await response.json();
    // Handle the response data if needed
  } catch (error) {
    console.log(error);
  }
}

async function handleUpdateCalibration() {
  function getCookie(name) {
    const cookieValue = document.cookie.match("(^|;)\\s*" + name + "\\s*=\\s*([^;]+)");
    return cookieValue ? cookieValue.pop() : "";
  }

  const csrfToken = getCookie("csrftoken");
  try {
    const response = await fetch("post-calibrasi/", {
      method: "post",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrfToken,
      },
      body: JSON.stringify({
        calibration: {
          cal_vibration_X: calVibX.textContent,
          cal_vibration_Y: calVibY.textContent,
          cal_vibration_Z: calVibZ.textContent,
        },
      }),
    });

    if (!response.ok) {
      throw new Error("Network response was not OK");
    }

    const responseData = await response.json();
    // Handle the response data if needed
  } catch (error) {
    console.log(error);
  }
}
