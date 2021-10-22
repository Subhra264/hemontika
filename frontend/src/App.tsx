import './App.scss';
import './utils/font-awesome';
import { Switch, Route } from 'react-router-dom';
import LogIn from './components/LogIn/LogIn';
import SignUp from './components/SignUp/SignUp';
import Card from './components/Cards/Card';
import useViewport from './hooks/useViewport';
import SubMenuBar from './components/SubMenuBar/SubMenuBar';
import MenuBar from './components/MenuBar/MenuBar';
import ProtectedRoute from './components/ProtectedRoute';
import PublishRouter from './components/Publish/PublishRouter';

function App() {
  const { isMobile, width } = useViewport();
  console.log('Inside App, isMobile', isMobile);
  console.log('Inside App, width', width);

  return (
    <div className={`App ${isMobile? 'mobile' : ''}`}>
      <MenuBar />
      <SubMenuBar />
      <Switch>
        <Route path='/log-in'>
          <LogIn />
        </Route>
        <Route path='/sign-up'>
          <SignUp />
        </Route>
        <ProtectedRoute path='/publish'>
          <PublishRouter />
        </ProtectedRoute>
      </Switch>
    </div>
  );
}

export default App;
