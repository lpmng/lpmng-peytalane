import React, { Component } from 'react';
import logo from './logo.svg';
import Users from './Users';
import Nav from './Nav';
import SquareStats from './SquareStats';



class App extends Component {
  render() {
    return (
      <main className="App">
        <Nav/>
        <section>
        <SquareStats title="Annonymous users" number="5" total="25" theme="turquoise"/>
        <SquareStats title="Real users" number="20" total="25" theme="violet"/>
        <SquareStats title="Stats random" number="264" total="500" theme="orange"/>
        <Users/>

        </section>

      </main>
    );
  }
}

export default App;
