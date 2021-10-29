import './App.scss';
import './utils/font-awesome';
import { Switch, Route } from 'react-router-dom';
import LogIn from './components/LogIn/LogIn';
import SignUp from './components/SignUp/SignUp';
import useViewport from './hooks/useViewport';
import SubMenuBar from './components/SubMenuBar/SubMenuBar';
import MenuBar from './components/MenuBar/MenuBar';
import ProtectedRoute from './components/ProtectedRoute';
import PublishRouter from './components/Publish/PublishRouter';
import SearchPage from './components/SearchPage/SearchPage';
import SlidingCardList from './components/SlidingCardList/SlidingCardList';
import ResponsiveWrapper from './components/ResponsiveWrapper/ResponsiveWrapper';

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
        <Route path='/home'>
          <SearchPage />
        </Route>
        <Route path='/popular'>
          <ResponsiveWrapper>
            <SlidingCardList title='Stories'/>
            <SlidingCardList title='Poems' />
            <SlidingCardList title='Novels' />
            <SlidingCardList title='Books' />
            <SlidingCardList title='Arts' />
            <SlidingCardList title='Musics' />
          </ResponsiveWrapper>
        </Route>
        <ProtectedRoute path='/publish'>
          <PublishRouter />
        </ProtectedRoute>
      </Switch>
    </div>
  );
}

export default App;
