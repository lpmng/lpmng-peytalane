import React, { Component } from 'react';
import "./css/SquareStats.css"
class SquareStats extends React.Component {
    render() {
      let class_main = "square-stats "+this.props.theme
      return (
          <div class={class_main}>
            <div class="title">{this.props.title}</div>
            <div class="infos">

                <div class="graph"></div>
                <div class="text">
                    <div class="main-info">{this.props.number}</div>
                    <div class="else">On a total of {this.props.total}</div>
                </div>
            </div>
          </div>
      )
    };
}

export default SquareStats;
