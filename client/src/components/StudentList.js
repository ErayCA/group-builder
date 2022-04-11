import { useState, useEffect } from 'react';
import Student from './Student';

function StudentList(props) {

  const [isLoading, setIsLoading] = useState(true);
  const [loadedStudents, setLoadedStudents] = useState([]);
  const { groupId } = props;

  useEffect(() => {

    setIsLoading(true);

    fetch(
      ('http://localhost:8080/group/studentList/' + groupId)
    ).then((response) => {
      return response.json();
    }).then((data) => {

        const students = [];

        for (const key in data) {
            students.push({
                id: key, ...data[key]
            })
        }
        
        setIsLoading(false);
        setLoadedStudents(students[0]);

    });
  }, []);

  if (isLoading) {
    return (
      <section>
        <p>Loading...</p>
      </section>
      );
  }
      
  let newStudents = Object.values(loadedStudents);
  newStudents.pop(); // Remove the "data" element

  return(
    <section>
        <div>
          {(newStudents).map((studentData) => {
            return (
              <div>
                <Student studentData={studentData} />
                <br />
              </div>
            )    
          })}
        </div>
    </section>
  );
}

export default StudentList;