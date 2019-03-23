import React from 'react'
import {Jumbotron} from "reactstrap";

export default function PageNotFound() {
    return (
        <Jumbotron>
            <h1 className="display-3">Page Not Found</h1>
            <p className="lead">I don't know how you got here, but please leave. Don't let the door hit you on the way out.</p>
        </Jumbotron>
    )
}
