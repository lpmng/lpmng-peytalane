import React, { Component } from 'react';

class ExtendInput extends Component {
  constructor(props) {
    console.log(props);
    super(props);
    this.state = {
      value: this.props.type === 'checkbox' ? (this.props.checked || false) : (this.props.value || '')
    };
  }

  handleChange(event) {
    const target = event.target;
    const name = target.name;
    const value = this.props.type === 'checkbox' ? target.checked : target.value;
    this.setState({value})
    this.props.onChange(name, value)
  }

  render() {
    return (
      <label>
        {this.props.label}
        <input type={this.props.type} onChange={this.handleChange.bind(this)} name={this.props.name} value={this.state.value}/>
      </label>
    );
  }
}

export default ExtendInput;
