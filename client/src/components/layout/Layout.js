import Sidebar from './Sidebar';
import classes from './Layout.module.css';

function Layout(props) {
  return (
    <div>
      <Sidebar />
      <main className={classes.main}>{props.children}</main>
    </div>
  );
}

export default Layout;