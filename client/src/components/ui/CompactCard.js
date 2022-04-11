import classes from './CompactCard.module.css';

function CompactCard(props) {
  return (
    <div className={classes.compactcard}>
      {props.children}
    </div>
  );
}

export default CompactCard;