import React from 'react'
import Button from "reactstrap/es/Button";

export default function SaveButton(props) {

    const style = {
        position: 'fixed',
        bottom: '20px',
        right: '20px',
        width: '100px'
    };

    return (
        <Button style={style} color="primary">
            Save Game
        </Button>
    )
}
