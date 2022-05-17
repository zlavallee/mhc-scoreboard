
//TODO: Do this properly
const apiBase = 'http://localhost:5000/api/v1.0'
// const apiBase = '/api/v1.0'

const constants = {
  mhcLogo: './mhc-logo.png',
  api: {
    scoreboard: `${apiBase}/scoreboard`,
    timer: `${apiBase}/timer`,
    timerStart: `${apiBase}/timer/start`,
    timerStop: `${apiBase}/timer/stop`,
    clear: `${apiBase}/clear`,
    reset: `${apiBase}/reset`,
    status: `${apiBase}/status`
  }
};

export default constants;
