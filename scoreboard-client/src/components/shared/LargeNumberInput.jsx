import React from "react";
import {Button, Input} from "reactstrap";
import './LargeNumberInput.scss'
import CenterHeader from "./CenterHeader";

export default function LargeNumberInput(props) {


  const getDisplayableCount = () => {
    if (isNaN(props.count)) {
      return 0
    }

    return getCount(props.count)
  }

  const getCount = () => {
    if (isNaN(props.count)) {
      return props.count
    }

    return parseInt(props.count)
  }

  const incrementCount = () => {
    setCount(getCount() + 1);
  };

  const decrementCount = () => {
    setCount(getCount() - 1);
  };

  const onChange = (value) => {
    if (isNaN(value)) {
      return
    }

    setCount(parseInt(value))
  }

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
        <FormButton onClick={incrementCount} edit={props.edit} label="+"
                    color="primary"/>
        <Input
            className="large-input"
            bsSize="lg"
            type="number"
            name="number"
            placeholder="number placeholder"
            value={getDisplayableCount()}
            readOnly={!props.edit}
            onChange={(e) => onChange(e.target.value)}
        />
        <FormButton onClick={decrementCount} edit={props.edit} label="-"
                    color="dark"/>
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
