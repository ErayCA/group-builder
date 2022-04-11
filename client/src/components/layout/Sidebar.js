import React from 'react';
import { slide as Menu} from 'react-burger-menu';
import { Link } from 'react-router-dom';

import './Sidebar.css'

function Sidebar() {
  return (
    <nav>
      <Menu>
        <Link to='/'>Home</Link>
        <Link to='/projects'>Projects</Link>
        <Link to='/groups'>Groups</Link>
        <Link to='/students'>Students</Link>
      </Menu>
    </nav>
  );
}

export default Sidebar;