import { render } from 'react-dom'
import { 
  BrowserRouter,
  Routes,
  Route 
} from 'react-router-dom';

import './index.css';
import App from './App';
import GroupsRoute from "./routes/Groups";
import StudentsRoute from "./routes/Students";
import ProjectsRoute from './routes/Projects';
import Layout from './components/layout/Layout';

const rootElement = document.getElementById('root');
render(
  <BrowserRouter>
    <Layout>
      <Routes>
        <Route path='/' element={<App />}>
          <Route path='groups' element={<GroupsRoute />} />
          <Route path='students' element={<StudentsRoute />} />
          <Route path='projects' element={<ProjectsRoute />} />
        </Route>
      </Routes>
    </Layout>
  </BrowserRouter>,
  rootElement
);