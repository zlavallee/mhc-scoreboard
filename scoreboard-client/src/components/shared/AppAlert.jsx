import React, {useState} from 'react'
import {Alert} from "reactstrap";

export default function AppAlert(props) {

    const [visible, setVisible] = useState(true);

    const onDismiss = () => {
        setVisible(false);
        props.onDismiss();
    };

    return (
        <div>
            <Alert color={props.color ? props.color : 'danger'} isOpen={visible} toggle={onDismiss}>
                {props.message}
            </Alert>
        </div>

    );
}
