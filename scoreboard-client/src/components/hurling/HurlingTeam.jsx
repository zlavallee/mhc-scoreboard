import React from 'react'
import {Col, Row} from "reactstrap";
import LargeNumberInput from "../shared/LargeNumberInput";
import {calculateScore} from "../../lib/utils";
import CenterHeader from "../shared/CenterHeader";

export default function HurlingTeam(props) {
    const goals = props.score.goals;
    const points = props.score.points;

    const onGoalsChange = (updatedGoals) => {
        onScoreChange({...props.score, goals: updatedGoals.toString()})
    };

    const onPointsChange = (updatedPoints) => {
        onScoreChange({...props.score, points: updatedPoints.toString()})
    };

    const onScoreChange = (score) => {
        props.onScoreChange(score)
    };

    return (
        <div className="raised-box">
            <CenterHeader name={props.name}/>
            <Row>
                <Col xs="6" lg="4">
                    <LargeNumberInput label="Goals" count={goals} edit onCountChange={onGoalsChange}/>
                </Col>
                <Col xs="6" lg="4">
                    <LargeNumberInput label="Points" count={points} edit onCountChange={onPointsChange}/>
                </Col>
                <Col xs="12" lg="4">
                    <LargeNumberInput label="Total" count={calculateScore({points, goals})}/>
                </Col>
            </Row>
        </div>
    )
}
