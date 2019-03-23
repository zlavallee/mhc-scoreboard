import React from 'react';
import Container from "reactstrap/es/Container";
import TopNav from "../components/shared/TopNav";
import {Redirect, Route, Switch} from "react-router";
import HurlingScoreboard from "./HurlingScoreboard";
import Games from "./Games";
import BasicScoreboard from "./BasicScoreboard";
import PageNotFound from "./PageNotFound";

export default class Root extends React.Component {
    constructor(props) {
        super(props);

        this.toggle = this.toggle.bind(this);
        this.state = {
            isOpen: false
        };
    }

    toggle() {
        this.setState({
            isOpen: !this.state.isOpen
        });
    }

    render() {
        return (
            <div>
                <TopNav/>
                <Container fluid>
                    <Switch>
                        <Redirect exact from="/" to="/hurling"/>
                        <Route path="/hurling" component={HurlingScoreboard}/>
                        <Route path="/games" component={Games}/>
                        <Route path="/scoreboard" component={BasicScoreboard}/>
                        <Route component={PageNotFound}/>
                    </Switch>
                </Container>
            </div>
        );
    }
}
