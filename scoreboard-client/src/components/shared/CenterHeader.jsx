import React from 'react'

const style = {
    textAlign: 'center'
};

export default function CenterHeader(props) {
    switch (props.importance) {
        case 'h1':
            return (<h1 style={style}>{props.name}</h1>);
        case 'h2':
            return (<h2 style={style}>{props.name}</h2>);
        case 'h3':
            return (<h3 style={style}>{props.name}</h3>);
        case 'h4':
            return (<h4 style={style}>{props.name}</h4>);
        case 'h5':
            return (<h5 style={style}>{props.name}</h5>);
        case 'h6':
            return (<h6 style={style}>{props.name}</h6>);
        default:
            return (<h1 style={style}>{props.name}</h1>);
    }
}
