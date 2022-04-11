function Modal(props) {

  function confirmHandler() {
    props.onConfirm();
  }

  return (
  <div className='modal'>
    <p>Project created.</p>
    <button onClick={confirmHandler} >OK</button>
  </div>
  );
}

export default Modal;