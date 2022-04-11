import Card from './ui/Card';

function Project(props) {

  const { projectData } = props;

  return(
    <Card>
      <div>
        <h4>{projectData.projectname}</h4>
      </div>
    </Card>
  );
}

export default Project;