import NewProjectForm from '../components/NewProjectForm.js';

function NewProject(props) {
  
  const { projectData } = props;
  const lastProject = projectData.pop();
  const {id: projectID} = lastProject;

  function newProjectHandler(newProjectData) {
    fetch(
      ('http://localhost:8080/project/byID/' + (projectID + 1)),
      {
        method: 'POST',
        body: JSON.stringify(newProjectData),
        headers: {
          'Content-Type': 'application/json'
        }
      }
    );
  }

  return (
    <section>
      <NewProjectForm onNewProject={newProjectHandler} />
    </section>
  );
}

export default NewProject;