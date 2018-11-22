import React, { Component } from 'react';
import ExtendInput from './Input';
import './css/Users.css';



class UserInfos extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        name: props.name
      };
    }

    render() {
        return (
            <div class="user-infos">
                <div class="username">
                    {this.state.name}
                </div>
            </div>
        )
    }
}

//table that display a list of users
// needed :
// - users : list of users
// - filter : string
// - title : string wich will be display at the begin of the list if the list is not empty
class UserTable extends React.Component {
    render() {
        const filter = this.props.filter

        const rows = []
        console.log(this.props);
        this.props.users.forEach((user) => {
            if(user.name.indexOf(filter) === -1)
            {
                return;
            }

            rows.push(
                <UserInfos name={user.name}/>
            )

        });

        if(rows.length > 0)
            return (

                <div>
                <h4>{this.props.title}</h4>
                {rows}
                </div>
            );
        else
            return (
                    <div>

                    </div>
            );
    };
}

class ListUser extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        filterText: '',
        onlyRealUsers: false,
        usersCore:[
            {name:"toto",age:18},
            {name:"titi",age:18},
        ],
        usersArel:[
            {name:"plouf",age:18},
            {name:"plaf",age:18},
        ]
      };
    }

    handleFilterTextChange(name, value) {
        this.setState({
            filterText : value
        });
    }

    render() {
      return (
        <div class="column">
          <h3>Users List</h3>
          <ExtendInput onChange={this.handleFilterTextChange.bind(this)} type="search" name="searchUsers" placeholder="search a user"/>
          <UserTable
            users = {this.state.usersCore}
            filter = {this.state.filterText}
            onlyRealUsers = {this.state.onlyExistingUsers}
            title="Utilisateurs inscrits"
          />
          <UserTable
            users = {this.state.usersArel}
            filter = {this.state.filterText}
            onlyRealUsers = {this.state.onlyExistingUsers}
            title="Utilisateurs Arel"
          />
        </div>
      );
    }
}


class AddUser extends React.Component {
    render() {
      return (
        <div class="column">
          <h3>Add a new user</h3>
        </div>
      );
    }
}

class Users extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        filterText: '',
        onlyRealUsers: false,
        usersCore:[
            {name:"toto",age:18},
            {name:"titi",age:18},
        ],
        usersArel:[
            {name:"plouf",age:18},
            {name:"plaf",age:18},
        ]
      };
    }
    render() {
        return (
            <div>
                <h2>Users</h2>
                <AddUser/>
                <ListUser />
                <div class="random-image column">
                    <img src="img-test.jpg"/>
                </div>
            </div>
        );
    }
}

export default Users;
