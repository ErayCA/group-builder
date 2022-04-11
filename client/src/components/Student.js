import CompactCard from './ui/CompactCard';

function Student(props) {

  const { studentData } = props;

  return(
    <CompactCard>
      <div>
        {studentData.firstname} {studentData.surname}
      </div>
      <div>
        {studentData.email}
      </div>
    </CompactCard>
  );
}

export default Student;