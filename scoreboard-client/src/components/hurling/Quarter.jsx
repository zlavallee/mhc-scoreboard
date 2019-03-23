import React from 'react'
import LargeNumberInput from "../shared/LargeNumberInput";
import CenterHeader from "../shared/CenterHeader";

export default function Quarter(props) {

    const onQuarterChange = (updatedQuarter) => {
        props.onQuarterChange(updatedQuarter)
    };

    return (
        <div className="raised-box">
            <CenterHeader name="Quarter"/>
            <LargeNumberInput count={props.quarter} onCountChange={onQuarterChange} edit/>
        </div>
    )
}
