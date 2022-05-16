import React, {useState, useEffect} from 'react';
import {Row} from "reactstrap";
import Col from "reactstrap/es/Col";
import HurlingTeam from "../components/hurling/HurlingTeam";
import '../index.scss'
import scoreboard from "../lib/api";
import Quarter from "../components/hurling/Quarter";
import {createFullScore, getOrDefault} from "../lib/utils";
import AppAlert from "../components/shared/AppAlert";
import HurlingTimer from "../components/hurling/HurlingTimer";

//TODO: Fix the string to int conversion
export default function HurlingScoreboard(props) {

  const alertLevels = getOrDefault(props.alertLevels, ['danger'])
  const emptyScore = {
    goals: 0,
    points: 0
  };

  const [homeScore, updateHomeScore] = useState(emptyScore);
  const [visitorScore, updateVisitorScore] = useState(emptyScore);
  const [quarter, updateQuarter] = useState(0);
  const [alert, setAlert] = useState(null);
  const [status, setStatus] = useState(null)
  const [loading, setLoading] = useState(false)

  useEffect(() => {
    console.log('Getting status')
    setLoading(true)
    scoreboard.status().then(statusData => {
      console.log('Setting status: ', statusData.status)
      setLoading(false)
      setStatus(statusData.status)
    })
  }, []);

  useEffect(() => {
    if (isInitialized()) {
      fetchState().then()
    }

  }, [status])

  const isInitialized = () => {
    return status === 'INITIALIZED'
  }

  const fetchState = async () => {
    setLoading(true)
    const result = await scoreboard.getState();

    console.log("Result:", result);

    updateQuarter(result.quarter);
    updateHomeScore(result.home);
    updateVisitorScore(result.visitor);
    setLoading(false)
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
      setLoading(true)
      await scoreboard.setState(scoreboardObject);
      setLoading(false)
      createAlert({
        message: "Scoreboard updated successfully",
        color: "success"
      });
    } catch (err) {
      console.error("Error while setting scoreboard state");
      console.error(err);
      createAlert({
        message: "Error while setting scoreboard state. You touched it last, that means you broke it. Either fix it or blame someone else.",
        color:
            "danger"
      })
    }
  };

  const createAlert = (alertData) => {
    if (alertLevels.indexOf(alertData.color) > -1) {
      setAlert(alertData)
      if (alertData.color !== 'danger') {
        setTimeout(() => {
          setAlert(null)
        }, 2000)
      }
    }
  }

  return (
      <div>
        {alert && <Row>
          <Col className="col-centered">
            <AppAlert message={alert.message} color={alert.color}
                      onDismiss={() => setAlert(null)}/>
          </Col>
        </Row>}
        {isInitialized() && <Row>
          <Col xs="12" md="6" lg="8" xl="8">
            <HurlingTimer/>
          </Col>
          <Col xs="12" md="6" lg="4" xl="4" className="mt-3 mb-3 col-centered">
            <Quarter onQuarterChange={onQuarterChange} quarter={quarter}
                     edit={!loading}/>
          </Col>
        </Row>}
        {isInitialized() && <Row>
          <Col sm="12" lg="6" className="mt-3">
            <HurlingTeam name="Home" score={homeScore}
                         onScoreChange={onHomeScoreChange} edit={!loading}/>
          </Col>
          <Col sm="12" lg="6" className="mt-3">
            <HurlingTeam name="Visitor" score={visitorScore}
                         onScoreChange={onVisitorScoreChange} edit={!loading}/>
          </Col>
        </Row>}
        {!isInitialized() &&
            <Row className="justify-content-center">
              <Col xs="12" md="8" lg="6" className="h6">
                Scoreboard is cleared. Click 'New Game' when ready. After a game
                is complete click 'Clear Scoreboard' to help extend battery
                life.
              </Col>
            </Row>}
      </div>
  )
}
