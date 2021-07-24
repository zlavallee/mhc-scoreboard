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

    setState = (scoreboard) => {
        console.log('Setting scoreboard state: ', scoreboard);

        return axios.post(constants.api.scoreboard, scoreboard, this.config);
    };

    getTimer = async () => {
        console.log("Getting scoreboard timer state from backend")
        return axios.get(constants.api.timer, this.config)
    }

    setTimer = async (timer) => {
        console.log("Setting scoreboard timer state from backend")
        return axios.post(constants.api.timer, timer, this.config)
    }

    startTimer = async () => {
        console.log("Starting scoreboard timer from backend")
        return axios.post(constants.api.timerStart)
    }

    stopTimer = async () => {
        console.log("Stopping scoreboard timer from backend")
        return axios.post(constants.api.timerStop)
    }

    saveGame = (homeTeam, visitorTeam, scoreboard) => {

    };
}

const scoreboard = new ScoreboardApi();

export default scoreboard;
