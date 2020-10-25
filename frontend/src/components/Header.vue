<template>
  <div class="header">
    <button type="button" id="backButton" class="header-button tooltip">
      <img src="../assets/right-arrow-45x45.png" alt="Back"/><span
      class="tooltiptext-r enabled-tooltip">Back</span>
    </button>
    <button type="button" id="tooltipButton" class="header-button">
      Disable tooltips
    </button>
    <button type="button" id="lastButton" class="header-button">
      Last button
    </button>
  </div>
</template>

<script>
export default {
  name: 'Header',
};
</script>

<style scoped>

.header {
  background-color: #300058;
  color: white;
  height: 100px;
  width: 100%;
}

.header-button {
  float: left;
  margin-top: 17px;
  height: 65px;

  background-color: rgba(0, 0, 0, 0);
  color: white;
  outline: none;
  border-radius: 4px;
  border: 1px solid rgba(255, 255, 255, 0);

  font-size: 19px;
  padding: 0 15px;
}

.header-button:hover {
  background-color: rgba(0, 0, 0, 0.2);
}

.header-button:active:hover {
  border-color: rgba(255, 255, 255, 0.2);
  background-color: rgba(0, 0, 0, 0.2);
}

#tooltipButton {
  margin-left: 30px;
}

#lastButton {
  float: right;
  margin-right: 17px;
}

@keyframes tooltipdelay {
  0% {
    opacity: 0;
  }
  35% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}

.tooltip .tooltiptext-l, .tooltip .tooltiptext-r {
  visibility: hidden;
  background-color: #444444ee;
  color: #ffffff;
  text-align: center;
  border-radius: 6px;
  padding: 5px 20px;
  position: absolute;
  z-index: 1;
  opacity: 0;
  font-size: 16px;
  display: none;
}

.tooltiptext-l {
  margin-left: -10px;
  margin-top: 15px;
}

.tooltiptext-r {
  margin-left: 20px;
  margin-top: 15px;
}

.tooltip:hover .tooltiptext-l.enabled-tooltip, .tooltip:hover .tooltiptext-r.enabled-tooltip {
  visibility: visible;
  animation: tooltipdelay 0.6s 1;
  opacity: 1;
  display: block;
}

</style>
