import React from 'react';
import {
    Collapse,
    Navbar,
    NavbarToggler,
    NavbarBrand,
    Nav,
    NavItem,
    NavLink
} from 'reactstrap';
import constants from "../../constants";
import {Link} from "react-router-dom";

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

    render() {
        return (
            <div className="mb-1">
                <Navbar color="light" light expand="md">
                    <NavbarBrand>
                        <img src={constants.mhcLogo} width="30" height="30" alt="MHC Scoreboard">
                        </img>
                        MHC Scoreboard
                    </NavbarBrand>
                    <NavbarToggler onClick={this.toggle}/>
                    <Collapse isOpen={this.state.isOpen} navbar>
                        <Nav className="ml-auto" navbar>
                            <NavItem>
                                <NavLink tag={Link} to="/hurling">Hurling Scoreboard</NavLink>
                            </NavItem>
                            <NavItem>
                                <NavLink tag={Link} to="/games">Past Games</NavLink>
                            </NavItem>
                            <NavItem>
                                <NavLink tag={Link} to="scoreboard">Basic Scoreboard</NavLink>
                            </NavItem>
                        </Nav>
                    </Collapse>
                </Navbar>
            </div>
        );
    }
}
