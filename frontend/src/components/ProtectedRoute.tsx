import React from 'react';
import { Route, RouteProps } from 'react-router-dom';

const ProtectedRoute: React.FC<RouteProps> = ({ children, ...props }): JSX.Element => {
    return (
        // TODO: Add a Redirect component to the '/log-in' page for unauthenticated users
        <Route {...props}>
            {children}
        </Route>
    );
};

export default ProtectedRoute;