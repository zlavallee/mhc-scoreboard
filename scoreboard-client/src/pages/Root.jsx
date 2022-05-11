import React from 'react';
import Container from "reactstrap/es/Container";
import TopNav from "../components/shared/TopNav";
import {Route, Switch} from "react-router";
import HurlingScoreboard from "./HurlingScoreboard";
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
                        <Route path="/" component={HurlingScoreboard}/>
                        <Route component={PageNotFound}/>
                    </Switch>
                </Container>
            </div>
        );
    }
}
