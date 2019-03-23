import CenterHeader from "../shared/CenterHeader";
import React from "react";
import LargeNumberInput from "../shared/LargeNumberInput";

export default function Goals(props) {

    return (
        <div>
            <LargeNumberInput label="Goals" count={props.count}/>
        </div>
    )
}
