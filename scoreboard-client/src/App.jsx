import React, { Component } from 'react';
import Root from "./pages/Root";
import {Router} from "react-router";
import {createBrowserHistory} from "history";

const history = createBrowserHistory()

class App extends Component {
  render() {
    return (
        <Router history={history}>
          <Root/>
        </Router>
    );
  }
}

export default App;
