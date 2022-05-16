import React from 'react';
import {
  Navbar,
  NavbarToggler,
  NavbarBrand,
  Nav,
  NavItem,
  Button
} from 'reactstrap';
import constants from "../../constants";
import scoreboard from "../../lib/api";

export default class TopNav extends React.Component {
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

  newGame() {
    scoreboard.reset().then(() => {
      window.location.reload()
    })
  }

  clearScoreboard() {
    scoreboard.clear().then(() => {
      window.location.reload()
    })
  }

  render() {
    return (
        <div className="mb-1">
          <Navbar color="light" light expand="md">
            <NavbarBrand>
              <img src={constants.mhcLogo} width="30" height="30"
                   alt="MHC Scoreboard">
              </img>
              MHC Scoreboard
            </NavbarBrand>
            <NavbarToggler onClick={this.toggle}/>
            <Nav className="mr-auto" navbar>
              <NavItem className="mr-2">
                <Button color="warning" title="Reset scoreboard for new game." onClick={this.newGame}>New Game</Button>
              </NavItem>
              <NavItem>
                <Button color="danger" title="Clear scoreboard of all values" onClick={this.clearScoreboard}>Clear Scoreboard</Button>
              </NavItem>
            </Nav>
          </Navbar>
        </div>
    );
  }
}
