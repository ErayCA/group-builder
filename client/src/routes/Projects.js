import { useState, useEffect } from 'react';
import Project from '../components/Project.js';
import NewProject from '../components/NewProject.js';

function ProjectsRoute() {
  const [isLoading, setIsLoading] = useState(true);
  const [loadedProjects, setLoadedProjects] = useState([]);

  useEffect(() => {

    setIsLoading(true);

    fetch(
      ('http://localhost:8080/project/')
    ).then((response) => {
      return response.json();
    }).then((data) => {

      const projects = [];

      for (const key in data) {
        projects.push({
          id: key, ...data[key]
        })
      }

      setIsLoading(false);
      setLoadedProjects(projects[0]);
    });
    
  }, []);

  if (isLoading) {
    return (
      <section>
        <p>Loading...</p>
      </section>
    );
  }

  let newProjects = Object.values(loadedProjects);
  newProjects.pop(); // Remove the "data" element

  return (
    <section>
      <h2>Projects</h2>
      <section>
        <h3>Active Projects</h3>
        {newProjects.map((projectData) => {
          return (
            <Project projectData={projectData} />
          )    
        })}
      </section>
      {newProjects.length !== 0 ? <NewProject projectData={newProjects} /> : null }
    </section>
  );
}

export default ProjectsRoute;