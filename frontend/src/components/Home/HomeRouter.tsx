import { Switch, Route } from 'react-router-dom';
import LiteratureDetails from '../LiteratureDetails/LiteratureDetails';
import SearchPage from '../SearchPage/SearchPage';

const HomeRouter: React.FC = (props) => {
    return (
        <Switch>
            <Route path='/' exact>

            </Route>
            <Route path='/home'>
                <SearchPage />
            </Route>
            <Route path='/stories'>
                <LiteratureDetails />
            </Route>
        </Switch>
    );
};

export default HomeRouter;