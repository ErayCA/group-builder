import { useState, useRef } from 'react';
import Card from './ui/Card'
import Backdrop from './ui/Backdrop';
import Modal from './ui/Modal';

function NewProjectForm(props) {

  const [modalIsOpen, setModalIsOpen] = useState(false);

  const projectNameInputRef = useRef();
  const managerIDInputRef = useRef();
  const cohortIDInputRef = useRef();

  function submitHandler(event) {

    event.preventDefault();

    const enteredProjectName = projectNameInputRef.current.value;
    const enteredManagerID = managerIDInputRef.current.value;
    const enteredCohortID = cohortIDInputRef.current.value;

    const newProjectData = {

      projectname: enteredProjectName,
      managerID: enteredManagerID,
      cohortID: enteredCohortID

    }

    props.onNewProject(newProjectData);
    setModalIsOpen(true);

  }

  function closeModalHandler() {
    setModalIsOpen(false);
  }

  return (
    <Card>
      <form onSubmit={submitHandler}>
        <div>
          <label htmlFor='name'>Project Name</label>
          <input type='text' required id='projectName' ref={projectNameInputRef} />
        </div>
        <div>
          <label htmlFor='name'>Manager ID</label>
          <input type='text' required id='managerID' ref={managerIDInputRef} />
        </div>
        <div>
          <label htmlFor='name'>Cohort ID</label>
          <input type='text' required id='cohortID' ref={cohortIDInputRef} />
        </div>
        <div>
          <button>Create Project</button>
        </div>
      </form>
      {modalIsOpen ? <Modal onConfirm={closeModalHandler} onCancel={closeModalHandler} /> : null}
      {modalIsOpen ? <Backdrop onCancel={closeModalHandler} /> : null}
    </Card>
  );
}

export default NewProjectForm;