import React, {useState, useEffect} from "react";
import CenterHeader from "../shared/CenterHeader";
import {Col, Row} from "reactstrap";
import LargeNumberInput from "../shared/LargeNumberInput";
import {calculateMinutes, calculateSeconds} from "../../lib/utils";

export default function HurlingTimer(props) {

    const [timer, updateTimer] = useState({
        totalSeconds: props.timer.value,
        stopped: props.timer.stopped,
        seconds: calculateSeconds(props.timer.value),
        minutes: calculateMinutes(props.timer.value)
    });

    const incrementSecond = () => {
        const newTotalSeconds = timer.totalSeconds + 1;
        updateTimer({
            totalSeconds: newTotalSeconds,
            stopped: timer.stopped,
            seconds: calculateSeconds(newTotalSeconds),
            minutes: calculateMinutes(newTotalSeconds)
        })
    };

    const id = setInterval(incrementSecond, 1000);

    useEffect(() => {
        return () => {
            clearInterval(id)
        }
    });

    return (
        <div className="raised-box">
            <CenterHeader name="Clock"/>
            <Row className="justify-content-center">
                <Col xs="6" md="4" lg="2">
                    <LargeNumberInput label="Minutes" count={timer.minutes}/>
                </Col>
                <Col xs="6" md="4" lg="2">
                    <LargeNumberInput label="Seconds" count={timer.seconds}/>
                </Col>
            </Row>
        </div>
    )
}
