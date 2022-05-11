const apiBase = 'localhost:5000/api/v1.0'
const constants = {
    mhcLogo: './mhc-logo.png',
    api: {
        scoreboard: `${apiBase}/scoreboard`,
        timer: `${apiBase}/timer`,
        timerStart: `${apiBase}/timer/start`,
        timerStop: `${apiBase}/timer/stop`
    }
};

export default constants;
