export const calculateScore = (score) => {
    return score.goals * 3 + score.points
};

export const createFullScore = (score) => {
    return {
        ...score,
        total: calculateScore(score)
    }
};
