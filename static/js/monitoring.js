//all variables are stored here
const vibrationPlusMinBtn = {
  upper: {
    min: document.getElementById("vibration-upper-min"),
    plus: document.getElementById("vibration-upper-plus"),
  },
  lower: {
    min: document.getElementById("vibration-lower-min"),
    plus: document.getElementById("vibration-lower-plus"),
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

const vibrationUpper = document.getElementById("vibration-upper");
const vibrationLower = document.getElementById("vibration-lower");
const currentUpper = document.getElementById("current-upper");
const currentLower = document.getElementById("current-lower");
const temperatureUpper = document.getElementById("temperature-upper");
const temperatureLower = document.getElementById("temperature-lower");

getMonitoringData();

//function to handle click upper and lower button
function handleClickPlusMin(event) {
  const clickedId = event.currentTarget.id;

  function updateVibrationUpper() {
    vibrationUpper.textContent = clickedId.startsWith("vibration-upper")
      ? clickedId.endsWith("plus")
        ? (parseFloat(vibrationUpper.textContent) + 0.5).toFixed(1)
        : (parseFloat(vibrationUpper.textContent) - 0.5).toFixed(1)
      : parseFloat(vibrationUpper.textContent);
  }
  function updateVibrationLower() {
    vibrationLower.textContent = clickedId.startsWith("vibration-lower")
      ? clickedId.endsWith("plus")
        ? (parseFloat(vibrationLower.textContent) + 0.5).toFixed(1)
        : (parseFloat(vibrationLower.textContent) - 0.5).toFixed(1)
      : parseFloat(vibrationLower.textContent);
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
  updateVibrationUpper();
  updateVibrationLower();
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
    const cookieValue = document.cookie.match(
      "(^|;)\\s*" + name + "\\s*=\\s*([^;]+)"
    );
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
          vibration_upper: vibrationUpper.textContent,
          vibration_lower: vibrationLower.textContent,
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
