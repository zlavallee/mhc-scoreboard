import React, {useState, useEffect, useRef} from "react";
import CenterHeader from "../shared/CenterHeader";
import {Col, Row} from "reactstrap";
import {
  calculateMilliSeconds,
  calculateMinutes,
  calculateSeconds, epochTimeNs, getOrDefault, nsToMillis
} from "../../lib/utils";
import Button from "reactstrap/es/Button";
import LargeNumberInput from "../shared/LargeNumberInput";
import api from "../../lib/api";

// TODO: Implement timer api
export default function HurlingTimer() {

  const mounted = useRef(true);
  const intervalIncrement = 100;
  const intervalRef = useRef(null);
  const [timer, updateTimer] = useState({
    totalMilliSeconds: 0,
    running: false,
    seconds: 0,
    minutes: 0,
    initialized: false
  });
  const [edit, updateEdit] = useState(false);
  const [initialized, updateInitialized] = useState(false);

  useEffect(() => {
    mounted.current = true;

    if (timer.initialized) {
      return;
    }

    api.getTimer().then(timerState => {
      if (mounted.current) {
        updateTimerFromState(timerState)
      }
    })

    return () => {
      mounted.current = false
    }
  }, [initialized])

  useEffect(() => {
    // console.log('Component mount');
    if (timer.running) {
      startInterval();
    }
    return () => {
      // console.log('Clearing interval...');
      removeInterval()
    }
  }, [timer]);

  const onClickEdit = () => {
    updateEdit(true);
  };

  const onClickSave = async () => {
    updateEdit(false);
    const timerState = await api.setTimer(
        {minutes: timer.minutes, seconds: timer.seconds})
    updateTimerFromState(timerState)
  };

  const onClickStop = async () => {
    const timerState = await api.stopTimer()
    updateTimerFromState(timerState)
  };

  const onClickStart = async () => {
    const timerState = await api.startTimer()
    updateTimerFromState(timerState)
  };

  const onClickReset = async () => {
    const timerState = await api.setTimer({minutes: 0, seconds: 0})
    updateTimerFromState(timerState)
  };

  const startInterval = () => {
    console.log('Setting interval...');
    intervalRef.current = setInterval(incrementMilliSecond, intervalIncrement);
  };

  const incrementMilliSecond = () => {
    if (timer.running) {
      const newTotalMilliSeconds = timer.totalMilliSeconds + intervalIncrement;

      updateTimer({
        ...timer,
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

  const removeInterval = () => {
    const interval = intervalRef.current;
    if (!!interval) {
      clearInterval(interval)
    }
  };

  const updateTimerFromState = (state) => {
    console.debug('Updating timer from state.', state)

    const timerState = new TimerState(state)

    const newTotalMilliSeconds = timerState.calculateTotalMillis()
    const seconds = calculateSeconds(newTotalMilliSeconds);
    const minutes = calculateMinutes(newTotalMilliSeconds);
    const running = timerState.getRunning();
    console.log(`Timer from state: ${minutes}:${seconds}`)
    updateTimer({
      ...timer,
      totalMilliSeconds: newTotalMilliSeconds,
      minutes,
      seconds,
      running
    })
    updateInitialized(true)
  }

  return (
      <div className="raised-box">
        <CenterHeader name="Clock"/>
        <Row className="justify-content-center">
          <Col xs="6" md="6" lg="4" xl="3">
            {!edit && <LargeNumberInput label="Minutes" count={timer.minutes}/>}
            {edit &&
                <LargeNumberInput label="Minutes" count={timer.minutes} edit
                                  onCountChange={onChangeMinutes}/>}
          </Col>
          <Col xs="6" md="6" lg="4" xl="3">
            {!edit && <LargeNumberInput label="Seconds" count={timer.seconds}/>}
            {edit &&
                <LargeNumberInput label="Seconds" count={timer.seconds} edit
                                  onCountChange={onChangeSeconds}/>}

          </Col>
        </Row>
        <Row className="justify-content-center">
          <Col xs="3" lg="2">
            {!timer.running && <Button color="success" onClick={onClickStart}
                                       disabled={edit}>Start</Button>}
            {timer.running && <Button color="warning"
                                      onClick={onClickStop}>Stop</Button>}

          </Col>
          <Col xs="3" lg="2">
            <Button color="danger" disabled={timer.running}
                    onClick={onClickReset}>Reset</Button>
          </Col>
          <Col xs="3" lg="2">
            {!edit && <Button color="info" onClick={onClickEdit}
                              disabled={timer.running}>Edit</Button>}
            {edit && <Button color="info" onClick={onClickSave}>Save</Button>}
          </Col>
        </Row>
      </div>
  )
}

class TimerState {
  constructor(state) {
    this.state = state
  }

  getRunning() {
    return this.state.running
  }

  getOffset() {
    return getOrDefault(this.state.offset, 0)
  }

  getStartTime() {
    return getOrDefault(this.state.start_time, 0)
  }

  calculateTotalMillis() {
    if (!this.getRunning()) {
      return nsToMillis(this.getOffset())
    }
    const totalNs = (epochTimeNs() - this.getStartTime()) + this.getOffset();

    console.debug("Total Ns: ", totalNs)

    const totalMillis = nsToMillis(
        (epochTimeNs() - this.getStartTime()) + this.getOffset());

    console.debug("Total Millis: ", totalMillis)

    return nsToMillis((epochTimeNs() - this.getStartTime()) + this.getOffset());
  }
}
