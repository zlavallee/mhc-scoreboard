export const calculateScore = (score) => {
  return score.goals * 3 + score.points
};

export const createFullScore = (score) => {
  return {
    ...score,
    total: calculateScore(score)
  }
};

export const calculateSeconds = (totalSeconds) => {
  return Math.floor(totalSeconds / 1000) % 60;
};

export const calculateMinutes = (totalSeconds) => {
  return Math.floor(totalSeconds / (60 * 1000));
};

export const calculateMilliSeconds = (minutes, seconds) => {
  return minutes * 60 * 1000 + seconds * 1000
};

export const epochTimeNs = () => {
  return Date.now() * 1000000
}

export const nsToMillis = (ns) => {
  return Math.round(ns / 1000000)
}

export const getOrDefault = (value, defaultValue) => {
  if (value === undefined || value === null) {
    return defaultValue
  }
  return value
}
