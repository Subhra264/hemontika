import { render, RenderOptions } from '@testing-library/react';
import React from 'react';
import { MemoryRouter as Router } from 'react-router-dom';

interface RouterWrappedRenderOptions extends RenderOptions {
    initialEntries?: string[];
}

interface WrappedWithMemRouterProps extends RouterWrappedRenderOptions{
    children?: React.ReactNode;
}

const WrappedWithMemRouter: React.FC<WrappedWithMemRouterProps> = (props) => {
    return (
        <Router initialEntries={props.initialEntries}>
            {props.children}
        </Router>
    );
};

export function renderWrappedWithRouter (ui: React.ReactElement, options: RouterWrappedRenderOptions) {
    const initialEntries = options.initialEntries? options.initialEntries : ['/'];

    render(ui, {
        wrapper: (args) => <WrappedWithMemRouter {...args} initialEntries={initialEntries} />,
        ...options
    });
}