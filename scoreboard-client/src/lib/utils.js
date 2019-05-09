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
    return totalSeconds % 60;
};

export const calculateMinutes = (totalSeconds) => {
    return Math.floor(totalSeconds / 60);
};
