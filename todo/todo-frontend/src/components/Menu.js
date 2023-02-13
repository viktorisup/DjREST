import React from 'react'
import UserList from "./User";

function NavbarItem({name, href}) {
    return (
        <li className="nav-item active">
          <a className="nav-link" to={href}>{name}</a>
        </li>
    )
}


export default function Navbar({navbarItems}) {
    return (
        <nav className="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
            <div className="collapse navbar-collapse" id="navbarCollapse">
              <ul className="navbar-nav mr-auto">
                <li className="nav-item active">
                  {navbarItems.map((item) => <NavbarItem name={item.name} href={item.href} />)}
                </li>
              </ul>
              <form className="form-inline mt-2 mt-md-0">
              </form>
            </div>
          </nav>
    )
}