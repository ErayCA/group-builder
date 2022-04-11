import { useState } from 'react';
import Card from './ui/Card';
import StudentList from './StudentList';

function Group(props) {

  const [viewStudentsClicked, setViewStudentsClicked] = useState(false);
  const { groupData } = props;

  function viewStudentsHandler() {
    setViewStudentsClicked(true);
  }

  return(
    <Card>
      <div>
        <h4>{groupData.groupname}</h4>
        {(viewStudentsClicked) ? <StudentList groupId={groupData.id}/> : null}
      </div>
      <div className='actions'>
        <button className='view' onClick={viewStudentsHandler}>View Students</button>
      </div>
    </Card>
  );
}

export default Group;