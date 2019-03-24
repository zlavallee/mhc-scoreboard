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

    saveGame = (homeTeam, visitorTeam, scoreboard) => {

    };
}

const scoreboard = new ScoreboardApi();

export default scoreboard;
