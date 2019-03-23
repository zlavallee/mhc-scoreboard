import React from "react";
import {Button, Input} from "reactstrap";
import './LargeNumberInput.scss'
import CenterHeader from "./CenterHeader";

export default function LargeNumberInput(props) {

    const incrementCount = () => {
        setCount(props.count + 1);
    };

    const decrementCount = () => {
        setCount(props.count - 1);
    };

    const setCount = (count) => {
        emitCountChange(count);
    };

    const emitCountChange = (count) => {
        if (props.onCountChange) {
            props.onCountChange(count);
        }
    };

    return (
        <div className="large-number-wrapper">
            {props.label && <CenterHeader importance="h3" name={props.label}/>}
            <FormButton onClick={incrementCount} edit={props.edit} label="+" color="primary"/>
            <Input
                className="large-input"
                bsSize="lg"
                type="number"
                name="number"
                placeholder="number placeholder"
                value={props.count}
                readOnly
            />
            <FormButton onClick={decrementCount} edit={props.edit} label="-" color="dark"/>
        </div>
    )
}

function FormButton(props) {
    return (
        <Button
            color={props.color ? props.color : 'primary'}
            onClick={props.onClick}
            className={"large-input-button " + (props.edit ? '' : 'hidden')}>
            {props.label}
        </Button>
    )
}
