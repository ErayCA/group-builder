import { useState, useEffect } from 'react';
import Group from '../components/Group';

function GroupsRoute() {

  const [isLoading, setIsLoading] = useState(true);
  const [loadedGroups, setLoadedGroups] = useState([]);

  useEffect(() => {

    setIsLoading(true);

    fetch(
      ('http://localhost:8080/group/')
    ).then((response) => {
      return response.json();
    }).then((data) => {

      const groups = [];

      for (const key in data) {
        groups.push({
          id: key, ...data[key]
        })
      }

      setIsLoading(false);
      setLoadedGroups(groups[0]);
    });
    
  }, []);

  if (isLoading) {
    return (
      <section>
        <p>Loading...</p>
      </section>
    );
  }

  let newGroups = Object.values(loadedGroups);
  newGroups.pop(); // Remove the "data" element

  return(
    <div>
      <h2>Groups</h2>
      <section>
        <h3>Active Groups</h3>
        {newGroups.map((groupData) => {
          return (
            <Group groupData={groupData} />
          )    
        })}
      </section>
    </div>
  );
}

export default GroupsRoute;