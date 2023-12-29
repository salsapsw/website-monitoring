// All variables are stored here
const dashboardCard = {
  temperatureValue: document.querySelector("#temperature-value .card-text"),
  currentValue: document.querySelector("#current-value .card-text"),
  accelvibXValue: document.querySelector("#accelvibX-value .card-text"),
  accelvibYValue: document.querySelector("#accelvibY-value .card-text"),
  accelvibZValue: document.querySelector("#accelvibZ-value .card-text"),
};

async function updateRealTimeClock() {
  const realTimeClockElement = document.getElementById("real-time-clock");
  const currentDate = new Date();
  const options = {
    weekday: "long",
    year: "numeric",
    month: "long",
    day: "numeric",
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
  };
  const formattedDateTime = currentDate.toLocaleDateString(undefined, options);
  realTimeClockElement.innerText = formattedDateTime;
  // console.log(formattedDateTime);
}
setInterval(updateRealTimeClock, 1000);

getDashboardData();
async function getDashboardData() {
  let prevSecond = null;

  async function updateTime() {
    const nowSecond = new Date().getSeconds();
    if (nowSecond == 0) {
      prevSecond = prevSecond - 60;
    }
    if (nowSecond - prevSecond >= 5) {
      await getSensorData();
      await getDataOnlineOffline();
      await getTotalOnlineOfflineWeek();
      prevSecond = nowSecond;
    }
  }
  async function getSensorData() {
    try {
      const response = await fetch("/get-dashboard-data/");
      const data = await response.json();
      const sensorValue = data["sensorValue"];

      if (sensorValue.currentValue !== 0.0) {
        document.getElementById("status").textContent = "Sensor is online";
      } else {
        document.getElementById("status").textContent = "Sensor is offline";
      }

      for (const key in sensorValue) {
        if (sensorValue.hasOwnProperty(key)) {
          const value = sensorValue[key];
          dashboardCard[key].textContent = value;
          // console.log(`${key}: ${dashboardCard[key].textContent}`);
        }
      }
      const warningCondition = data["warningCondition"];
      if (warningCondition == null) {
        return;
      }
      const currentValueCard = document.getElementById("current-value");
      const temperatureValueCard = document.getElementById("temperature-value");
      const accelvibXValueCard = document.getElementById("accelvibX-value");
      const accelvibYValueCard = document.getElementById("accelvibY-value");
      const accelvibZValueCard = document.getElementById("accelvibZ-value");

      if (!warningCondition["warningTemperature"]) {
        temperatureValueCard.classList.remove("sensor-alert");
      } else {
        temperatureValueCard.classList.add("sensor-alert");
      }

      if (!warningCondition["warningCurrent"]) {
        currentValueCard.classList.remove("sensor-alert");
      } else {
        currentValueCard.classList.add("sensor-alert");
      }

      if (!warningCondition["warningaccelvibx"]) {
        accelvibXValueCard.classList.remove("sensor-alert");
      } else {
        accelvibXValueCard.classList.add("sensor-alert");
      }

      if (!warningCondition["warningaccelviby"]) {
        accelvibYValueCard.classList.remove("sensor-alert");
      } else {
        accelvibYValueCard.classList.add("sensor-alert");
      }

      if (!warningCondition["warningaccelvibz"]) {
        accelvibZValueCard.classList.remove("sensor-alert");
      } else {
        accelvibZValueCard.classList.add("sensor-alert");
      }
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  }
  async function getDataOnlineOffline() {
    try {
      const response = await fetch("/get-data-online-offline/");
      const data = await response.json();
      const totalWaktuOnlineHours = data.total_waktu_online_hours;
      const totalWaktuOnlineMinutes = data.total_waktu_online_minutes;
      const totalWaktuOfflineHours = data.total_waktu_offline_hours;
      const totalWaktuOfflineMinutes = data.total_waktu_offline_minutes;

      document.getElementById("totalWaktuOnlineHours").textContent = `Online: ${totalWaktuOnlineHours} hours`;
      document.getElementById("totalWaktuOnlineMinutes").textContent = `${totalWaktuOnlineMinutes} minutes`;
      document.getElementById("totalWaktuOfflineHours").textContent = `Offline: ${totalWaktuOfflineHours} hours`;
      document.getElementById("totalWaktuOfflineMinutes").textContent = `${totalWaktuOfflineMinutes} minutes`;
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  }

  function getTotalOnlineOfflineWeek() {
    fetch("/get-data-online-offline-week/") // Ganti dengan URL yang sesuai
      .then((response) => response.json())
      .then((data) => {
        const totalOnlineElement = document.getElementById("totalOnlineWeek");
        const totalOfflineElement = document.getElementById("totalOfflineWeek");

        const onlineHours = data.total_waktu_online_hours;
        const onlineMinutes = data.total_waktu_online_minutes;

        const offlineHours = data.total_waktu_offline_hours;
        const offlineMinutes = data.total_waktu_offline_minutes;

        totalOnlineElement.textContent = `${onlineHours} hours ${onlineMinutes} minutes`;
        totalOfflineElement.textContent = `${offlineHours} hours ${offlineMinutes} minutes`;
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  }

  setInterval(updateTime, 500);
}
