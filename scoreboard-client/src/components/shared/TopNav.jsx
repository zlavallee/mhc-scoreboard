import React from 'react';
import {
    Navbar,
    NavbarToggler,
    NavbarBrand
} from 'reactstrap';
import constants from "../../constants";

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
                </Navbar>
            </div>
        );
    }
}
