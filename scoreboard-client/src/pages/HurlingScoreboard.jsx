import React, {useState, useEffect} from 'react';
import {Row} from "reactstrap";
import Col from "reactstrap/es/Col";
import HurlingTeam from "../components/hurling/HurlingTeam";
import '../index.scss'
import scoreboard from "../lib/api";
import Quarter from "../components/hurling/Quarter";
import {createFullScore} from "../lib/utils";
import SaveButton from "../components/hurling/SaveButton";
import AppAlert from "../components/shared/AppAlert";
import HurlingTimer from "../components/hurling/HurlingTimer";

export default function HurlingScoreboard() {

    const emptyScore = {
        goals: 0,
        points: 0
    };


    const [homeScore, updateHomeScore] = useState(emptyScore);
    const [visitorScore, updateVisitorScore] = useState(emptyScore);
    const [quarter, updateQuarter] = useState(0);
    const [alert, setAlert] = useState(null);

    useEffect(() => {
        fetchState()
    }, []);

    const fetchState = async () => {
        const result = await scoreboard.getState();

        console.log("Result:", result);

        updateQuarter(result.quarter);
        updateHomeScore(result.home);
        updateVisitorScore(result.visitor);
    };

    const onHomeScoreChange = (score) => {
        console.log('Home Score Changed', score);
        updateHomeScore(score);
        updateScoreboard({
            home: {
                ...createFullScore(score)
            },
            visitor: {
                ...createFullScore(visitorScore)
            },
            quarter: quarter
        });
    };

    const onVisitorScoreChange = (score) => {
        updateVisitorScore(score);
        updateScoreboard({
            home: {
                ...createFullScore(homeScore)
            },
            visitor: {
                ...createFullScore(score)
            },
            quarter: quarter
        });
    };

    const onQuarterChange = (updatedQuarter) => {
        updateQuarter(updatedQuarter);
        updateScoreboard({
            home: {
                ...createFullScore(homeScore)
            },
            visitor: {
                ...createFullScore(visitorScore)
            },
            quarter: updatedQuarter
        });
    };

    const updateScoreboard = async (scoreboardObject) => {
        try {
            const response = await scoreboard.setState(scoreboardObject);
            setAlert({
                message: "Scoreboard updated successfully",
                color: "success"
            });
        } catch (err) {
            console.error("Error while setting scoreboard state");
            console.error(err);
            setAlert({
                message: "Error while setting scoreboard state. You touched it last, that means you broke it. Either fix it or blame someone else.",
                color:
                    "danger"
            })
        }
    };

    return (
        <div>
            {alert && <Row>
                <Col className="col-centered">
                    <AppAlert message={alert.message} color={alert.color} onDismiss={() => setAlert(null)}/>
                </Col>
            </Row>}
            <Row>
                <Col xs="12" md="6" lg="8" xl="8">
                    <HurlingTimer/>
                </Col>
                <Col xs="12" md="6" lg="4" xl="4" className="mt-3 mb-3 col-centered">
                    <Quarter onQuarterChange={onQuarterChange} quarter={quarter}/>
                </Col>
            </Row>
            <Row>
                <Col sm="12" lg="6" className="mt-3">
                    <HurlingTeam name="Home" score={homeScore} onScoreChange={onHomeScoreChange}/>
                </Col>
                <Col sm="12" lg="6" className="mt-3">
                    <HurlingTeam name="Visitor" score={visitorScore} onScoreChange={onVisitorScoreChange}/>
                </Col>
            </Row>
            <SaveButton/>
        </div>
    )
}
