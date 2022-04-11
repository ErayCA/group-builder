import { useState, useEffect } from 'react';
import Student from '../components/Student';

function StudentsRoute() {
    
  const [isLoading, setIsLoading] = useState(true);
  const [loadedStudents, setLoadedStudents] = useState([]);

  useEffect(() => {

    setIsLoading(true);

    fetch(
      ('http://localhost:8080/user/')
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
    <div>
      <h2>Students</h2>
      <section>
        <h3>All Students</h3>
        {newStudents.map((studentData) => {
          return (
            <Student studentData={studentData} />
          )    
        })}
      </section>
    </div>
  );
}

export default StudentsRoute;