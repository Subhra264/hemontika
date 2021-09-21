import './App.scss';
import { Switch, Route } from 'react-router-dom';
import LogIn from './components/LogIn/LogIn';
import SignUp from './components/SignUp/SignUp';
import Card from './components/Cards/Card';

function App() {
  return (
    <div className="App">
      <Card />
      <Switch>
        <Route path='/log-in'>
          <LogIn />
        </Route>
        <Route path='/sign-up'>
          <SignUp />
        </Route>
      </Switch>
    </div>
  );
}

export default App;
