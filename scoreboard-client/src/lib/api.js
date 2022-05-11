import axios from 'axios';
import constants from "../constants";

class ScoreboardApi {
  config = {
    headers: {
      'Content-Type': 'application/json',
    }
  };

  getState = async () => {
    console.log("Getting scoreboard state from backend");
    const {data} = await axios.get(constants.api.scoreboard, this.config);

    return data;
  };

  setState = async (scoreboard) => {
    console.log('Setting scoreboard state: ', scoreboard);

    const {data} = await axios.post(constants.api.scoreboard, scoreboard,
        this.config);
    return data
  };

  getTimer = async () => {
    console.log("Getting scoreboard timer state from backend")
    const {data} = await axios.get(constants.api.timer, this.config)
    return data
  }

  setTimer = async (timer) => {
    console.log("Setting scoreboard timer state from backend")
    const {data} = await axios.post(constants.api.timer, timer, this.config)
    return data
  }

  startTimer = async () => {
    console.log("Starting scoreboard timer from backend")
    const {data} = await axios.post(constants.api.timerStart)
    return data
  }

  stopTimer = async () => {
    console.log("Stopping scoreboard timer from backend")
    const {data} = await axios.post(constants.api.timerStop)
    return data
  }

}

const scoreboard = new ScoreboardApi();

export default scoreboard;
