(window.webpackJsonp=window.webpackJsonp||[]).push([[0],{34:function(e,t,n){},53:function(e,t,n){e.exports=n(90)},71:function(e,t,n){},90:function(e,t,n){"use strict";n.r(t);var a=n(0),r=n.n(a),c=n(27),o=n.n(c),l=(n(34),n(15)),s=n(21),i=n(23),u=n(22),m=n(24),g=n(16),b=n(52),d=n(91),h=n(92),E=n(93),f=n(94),p=n(95),O=n(96),v=n(97),j={mhcLogo:"./mhc-logo.png",api:{scoreboard:"/api/v1.0/scoreboard"}},C=n(28),S=function(e){function t(e){var n;return Object(l.a)(this,t),(n=Object(i.a)(this,Object(u.a)(t).call(this,e))).toggle=n.toggle.bind(Object(g.a)(Object(g.a)(n))),n.state={isOpen:!1},n}return Object(m.a)(t,e),Object(s.a)(t,[{key:"toggle",value:function(){this.setState({isOpen:!this.state.isOpen})}},{key:"render",value:function(){return r.a.createElement("div",{className:"mb-1"},r.a.createElement(d.a,{color:"light",light:!0,expand:"md"},r.a.createElement(h.a,null,r.a.createElement("img",{src:j.mhcLogo,width:"30",height:"30",alt:"MHC Scoreboard"}),"MHC Scoreboard"),r.a.createElement(E.a,{onClick:this.toggle}),r.a.createElement(f.a,{isOpen:this.state.isOpen,navbar:!0},r.a.createElement(p.a,{className:"ml-auto",navbar:!0},r.a.createElement(O.a,null,r.a.createElement(v.a,{tag:C.a,to:"/hurling"},"Hurling Scoreboard")),r.a.createElement(O.a,null,r.a.createElement(v.a,{tag:C.a,to:"/games"},"Past Games")),r.a.createElement(O.a,null,r.a.createElement(v.a,{tag:C.a,to:"scoreboard"},"Basic Scoreboard"))))))}}]),t}(r.a.Component),x=n(6),y=n(8),w=n(18),k=n.n(w),N=n(26),M=n(13),q=n(99),G=n(25),H=n(98),I=n(19),B=(n(71),{textAlign:"center"});function P(e){switch(e.importance){case"h1":return r.a.createElement("h1",{style:B},e.name);case"h2":return r.a.createElement("h2",{style:B},e.name);case"h3":return r.a.createElement("h3",{style:B},e.name);case"h4":return r.a.createElement("h4",{style:B},e.name);case"h5":return r.a.createElement("h5",{style:B},e.name);case"h6":return r.a.createElement("h6",{style:B},e.name);default:return r.a.createElement("h1",{style:B},e.name)}}function D(e){var t=function(e){n(e)},n=function(t){e.onCountChange&&e.onCountChange(t)};return r.a.createElement("div",{className:"large-number-wrapper"},e.label&&r.a.createElement(P,{importance:"h3",name:e.label}),r.a.createElement(Q,{onClick:function(){t(e.count+1)},edit:e.edit,label:"+",color:"primary"}),r.a.createElement(H.a,{className:"large-input",bsSize:"lg",type:"number",name:"number",placeholder:"number placeholder",value:e.count,readOnly:!0}),r.a.createElement(Q,{onClick:function(){t(e.count-1)},edit:e.edit,label:"-",color:"dark"}))}function Q(e){return r.a.createElement(I.a,{color:e.color?e.color:"primary",onClick:e.onClick,className:"large-input-button "+(e.edit?"":"hidden")},e.label)}var R=function(e){return 3*e.goals+e.points},J=function(e){return Object(y.a)({},e,{total:R(e)})},L=function(e){return Math.floor(e/1e3)%60},T=function(e){return Math.floor(e/6e4)},W=function(e,t){return 60*e*1e3+1e3*t};function z(e){var t=e.score.goals,n=e.score.points,a=function(t){e.onScoreChange(t)};return r.a.createElement("div",{className:"raised-box"},r.a.createElement(P,{name:e.name}),r.a.createElement(q.a,null,r.a.createElement(G.a,{xs:"6",lg:"4"},r.a.createElement(D,{label:"Goals",count:t,edit:!0,onCountChange:function(t){a(Object(y.a)({},e.score,{goals:t}))}})),r.a.createElement(G.a,{xs:"6",lg:"4"},r.a.createElement(D,{label:"Points",count:n,edit:!0,onCountChange:function(t){a(Object(y.a)({},e.score,{points:t}))}})),r.a.createElement(G.a,{xs:"12",lg:"4"},r.a.createElement(D,{label:"Total",count:R({points:n,goals:t})}))))}var A=n(32),F=n.n(A),V=new function e(){var t=this;Object(l.a)(this,e),this.config={headers:{"Content-Type":"application/json"}},this.getState=Object(N.a)(k.a.mark(function e(){var n,a;return k.a.wrap(function(e){for(;;)switch(e.prev=e.next){case 0:return console.log("Getting scoreboard state from backend"),e.next=3,F.a.get(j.api.scoreboard,t.config);case 3:return n=e.sent,a=n.data,e.abrupt("return",a);case 6:case"end":return e.stop()}},e)})),this.setState=function(e){return console.log("Setting scoreboard state: ",e),F.a.post(j.api.scoreboard,e,t.config)},this.saveGame=function(e,t,n){}};function Y(e){return r.a.createElement("div",{className:"raised-box"},r.a.createElement(P,{name:"Quarter"}),r.a.createElement(D,{count:e.quarter,onCountChange:function(t){e.onQuarterChange(t)},edit:!0}))}function $(e){return r.a.createElement(I.a,{style:{position:"fixed",bottom:"20px",right:"20px",width:"100px"},color:"primary"},"Save Game")}var K=n(101);function U(e){var t=Object(a.useState)(!0),n=Object(M.a)(t,2),c=n[0],o=n[1];return r.a.createElement("div",null,r.a.createElement(K.a,{color:e.color?e.color:"danger",isOpen:c,toggle:function(){o(!1),e.onDismiss()}},e.message))}function X(e){var t=Object(a.useRef)(),n=Object(a.useState)({totalMilliSeconds:0,running:!1,seconds:0,minutes:0}),c=Object(M.a)(n,2),o=c[0],l=c[1],s=Object(a.useState)(!1),i=Object(M.a)(s,2),u=i[0],m=i[1],g=function(){if(o.running){var e=o.totalMilliSeconds+100,t=L(e),n=T(e);console.log("Incrementing seconds: ".concat(n,":").concat(t)),console.log("Previous Millis: ".concat(o.totalMilliSeconds,", New Millis: ").concat(e)),l({totalMilliSeconds:e,running:o.running,seconds:L(e),minutes:T(e)})}},b=function(e,t){l(Object(y.a)({},o,{totalMilliSeconds:W(e,t),minutes:e,seconds:t}))};return Object(a.useEffect)(function(){return console.log("Component mount"),o.running&&(console.log("Setting interval..."),t.current=setInterval(g,100)),function(){console.log("Clearing interval..."),function(){var e=t.current;e&&clearInterval(e)}()}},[o]),r.a.createElement("div",{className:"raised-box"},r.a.createElement(P,{name:"Clock"}),r.a.createElement(q.a,{className:"justify-content-center"},r.a.createElement(G.a,{xs:"6",md:"6",lg:"4",xl:"3"},!u&&r.a.createElement(D,{label:"Minutes",count:o.minutes}),u&&r.a.createElement(D,{label:"Minutes",count:o.minutes,edit:!0,onCountChange:function(e){b(e,o.seconds)}})),r.a.createElement(G.a,{xs:"6",md:"6",lg:"4",xl:"3"},!u&&r.a.createElement(D,{label:"Seconds",count:o.seconds}),u&&r.a.createElement(D,{label:"Seconds",count:o.seconds,edit:!0,onCountChange:function(e){b(o.minutes,e)}}))),r.a.createElement(q.a,{className:"justify-content-center"},r.a.createElement(G.a,{xs:"3",lg:"2"},!o.running&&r.a.createElement(I.a,{color:"success",onClick:function(){l(Object(y.a)({},o,{running:!0}))},disabled:u},"Start"),o.running&&r.a.createElement(I.a,{color:"warning",onClick:function(){l(Object(y.a)({},o,{running:!1}))}},"Stop")),r.a.createElement(G.a,{xs:"3",lg:"2"},r.a.createElement(I.a,{color:"danger",disabled:o.running,onClick:function(){b(0,0)}},"Reset")),r.a.createElement(G.a,{xs:"3",lg:"2"},!u&&r.a.createElement(I.a,{color:"info",onClick:function(){m(!0)},disabled:o.running},"Edit"),u&&r.a.createElement(I.a,{color:"info",onClick:function(){m(!1)}},"Save"))))}function Z(){var e={goals:0,points:0},t=Object(a.useState)(e),n=Object(M.a)(t,2),c=n[0],o=n[1],l=Object(a.useState)(e),s=Object(M.a)(l,2),i=s[0],u=s[1],m=Object(a.useState)(0),g=Object(M.a)(m,2),b=g[0],d=g[1],h=Object(a.useState)({value:0,running:!0}),E=Object(M.a)(h,2),f=E[0],p=(E[1],Object(a.useState)(null)),O=Object(M.a)(p,2),v=O[0],j=O[1];Object(a.useEffect)(function(){C()},[]);var C=function(){var e=Object(N.a)(k.a.mark(function e(){var t;return k.a.wrap(function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,V.getState();case 2:t=e.sent,console.log("Result:",t),d(t.quarter),o(t.home),u(t.visitor);case 7:case"end":return e.stop()}},e)}));return function(){return e.apply(this,arguments)}}(),S=function(){var e=Object(N.a)(k.a.mark(function e(t){return k.a.wrap(function(e){for(;;)switch(e.prev=e.next){case 0:return e.prev=0,e.next=3,V.setState(t);case 3:e.sent,j({message:"Scoreboard updated successfully",color:"success"}),e.next=12;break;case 7:e.prev=7,e.t0=e.catch(0),console.error("Error while setting scoreboard state"),console.error(e.t0),j({message:"Error while setting scoreboard state. You touched it last, that means you broke it. Either fix it or blame someone else.",color:"danger"});case 12:case"end":return e.stop()}},e,null,[[0,7]])}));return function(t){return e.apply(this,arguments)}}();return r.a.createElement("div",null,v&&r.a.createElement(q.a,null,r.a.createElement(G.a,{className:"col-centered"},r.a.createElement(U,{message:v.message,color:v.color,onDismiss:function(){return j(null)}}))),r.a.createElement(q.a,null,r.a.createElement(G.a,{xs:"12",md:"6",lg:"8",xl:"8"},r.a.createElement(X,{timer:f})),r.a.createElement(G.a,{xs:"12",md:"6",lg:"4",xl:"4",className:"mt-3 mb-3 col-centered"},r.a.createElement(Y,{onQuarterChange:function(e){d(e),S({home:Object(y.a)({},J(c)),visitor:Object(y.a)({},J(i)),quarter:e})},quarter:b}))),r.a.createElement(q.a,null,r.a.createElement(G.a,{sm:"12",lg:"6",className:"mt-3"},r.a.createElement(z,{name:"Home",score:c,onScoreChange:function(e){console.log("Home Score Changed",e),S({home:Object(y.a)({},J(e)),visitor:Object(y.a)({},J(i)),quarter:b}),o(e)}})),r.a.createElement(G.a,{sm:"12",lg:"6",className:"mt-3"},r.a.createElement(z,{name:"Visitor",score:i,onScoreChange:function(e){u(e),S({home:Object(y.a)({},J(c)),visitor:Object(y.a)({},J(e)),quarter:b})}}))),r.a.createElement($,null))}function _(){return r.a.createElement("div",null,"Games")}function ee(){return r.a.createElement("div",null,"Basic Scoreboard")}var te=n(100);function ne(){return r.a.createElement(te.a,null,r.a.createElement("h1",{className:"display-3"},"Page Not Found"),r.a.createElement("p",{className:"lead"},"I don't know how you got here, but please leave. Don't let the door hit you on the way out."))}var ae=function(e){function t(e){var n;return Object(l.a)(this,t),(n=Object(i.a)(this,Object(u.a)(t).call(this,e))).toggle=n.toggle.bind(Object(g.a)(Object(g.a)(n))),n.state={isOpen:!1},n}return Object(m.a)(t,e),Object(s.a)(t,[{key:"toggle",value:function(){this.setState({isOpen:!this.state.isOpen})}},{key:"render",value:function(){return r.a.createElement("div",null,r.a.createElement(S,null),r.a.createElement(b.a,{fluid:!0},r.a.createElement(x.d,null,r.a.createElement(x.a,{exact:!0,from:"/",to:"/hurling"}),r.a.createElement(x.b,{path:"/hurling",component:Z}),r.a.createElement(x.b,{path:"/games",component:_}),r.a.createElement(x.b,{path:"/scoreboard",component:ee}),r.a.createElement(x.b,{component:ne}))))}}]),t}(r.a.Component),re=n(10),ce=Object(re.a)(),oe=function(e){function t(){return Object(l.a)(this,t),Object(i.a)(this,Object(u.a)(t).apply(this,arguments))}return Object(m.a)(t,e),Object(s.a)(t,[{key:"render",value:function(){return r.a.createElement(x.c,{history:ce},r.a.createElement(ae,null))}}]),t}(a.Component);Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));o.a.render(r.a.createElement(oe,null),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then(function(e){e.unregister()})}},[[53,1,2]]]);
//# sourceMappingURL=main.56dc64cd.chunk.js.map