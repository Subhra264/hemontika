import React from 'react';
import { Switch, Route } from 'react-router-dom';
import Publish from './Publish/Publish';

const PublishRouter: React.FC = (props) => {
    return (
        <Switch>
            <Route path='/'>
                <Publish />
            </Route>
        </Switch>
    );
};

export default PublishRouter;