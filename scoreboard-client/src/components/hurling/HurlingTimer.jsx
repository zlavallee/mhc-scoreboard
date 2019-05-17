import React, {useState, useEffect, useRef} from "react";
import CenterHeader from "../shared/CenterHeader";
import {Col, Row} from "reactstrap";
import {calculateMilliSeconds, calculateMinutes, calculateSeconds} from "../../lib/utils";
import Button from "reactstrap/es/Button";
import LargeNumberInput from "../shared/LargeNumberInput";

export default function HurlingTimer(props) {

    const intervalIncrement = 100;
    const intervalRef = useRef();
    const [timer, updateTimer] = useState({
        totalMilliSeconds: 0,
        running: false,
        seconds: 0,
        minutes: 0
    });
    const [edit, updateEdit] = useState(false);


    const onClickEdit = () => {
        updateEdit(true);
    };

    const onClickSave = () => {
        updateEdit(false);
    };

    const onClickStop = () => {
        updateTimer({
            ...timer,
            running: false
        })
    };

    const onClickStart = () => {
        updateTimer({
            ...timer,
            running: true
        })
    };

    const onClickReset = () => {
        updateTotal(0, 0)
    };

    const incrementMilliSecond = () => {
        if (timer.running) {
            const newTotalMilliSeconds = timer.totalMilliSeconds + intervalIncrement;
            const seconds = calculateSeconds(newTotalMilliSeconds);
            const minutes = calculateMinutes(newTotalMilliSeconds);
            console.log(`Incrementing seconds: ${minutes}:${seconds}`);
            console.log(`Previous Millis: ${timer.totalMilliSeconds}, New Millis: ${newTotalMilliSeconds}`)

            updateTimer({
                totalMilliSeconds: newTotalMilliSeconds,
                running: timer.running,
                seconds: calculateSeconds(newTotalMilliSeconds),
                minutes: calculateMinutes(newTotalMilliSeconds)
            })
        }
    };

    const updateTotal = (minutes, seconds) => {
        updateTimer({
            ...timer,
            totalMilliSeconds: calculateMilliSeconds(minutes, seconds),
            minutes, seconds
        })
    };

    const onChangeSeconds = (seconds) => {
        updateTotal(timer.minutes, seconds)
    };

    const onChangeMinutes = (minutes) => {
        updateTotal(minutes, timer.seconds)
    };

    const startInterval = () => {
        console.log('Setting interval...');
        intervalRef.current = setInterval(incrementMilliSecond, intervalIncrement);
    };

    const removeInterval = () => {
        const interval = intervalRef.current;
        if (!!interval) {
            clearInterval(interval)
        }
    };

    useEffect(() => {
        console.log('Component mount');
        if (timer.running) {
            startInterval();
        }
        return () => {
            console.log('Clearing interval...');
            removeInterval()
        }
    }, [timer]);

    return (
        <div className="raised-box">
            <CenterHeader name="Clock"/>
            <Row className="justify-content-center">
                <Col xs="6" md="6" lg="4" xl="3">
                    {!edit && <LargeNumberInput label="Minutes" count={timer.minutes}/>}
                    {edit &&
                    <LargeNumberInput label="Minutes" count={timer.minutes} edit onCountChange={onChangeMinutes}/>}
                </Col>
                <Col xs="6" md="6" lg="4" xl="3">
                    {!edit && <LargeNumberInput label="Seconds" count={timer.seconds}/>}
                    {edit &&
                    <LargeNumberInput label="Seconds" count={timer.seconds} edit onCountChange={onChangeSeconds}/>}

                </Col>
            </Row>
            <Row className="justify-content-center">
                <Col xs="3" lg="2">
                    {!timer.running && <Button color="success" onClick={onClickStart} disabled={edit}>Start</Button>}
                    {timer.running && <Button color="warning" onClick={onClickStop}>Stop</Button>}

                </Col>
                <Col xs="3" lg="2">
                    <Button color="danger" disabled={timer.running} onClick={onClickReset}>Reset</Button>
                </Col>
                <Col xs="3" lg="2">
                    {!edit && <Button color="info" onClick={onClickEdit} disabled={timer.running}>Edit</Button>}
                    {edit && <Button color="info" onClick={onClickSave}>Save</Button>}
                </Col>
            </Row>
        </div>
    )
}
