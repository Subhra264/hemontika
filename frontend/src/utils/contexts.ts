import React from 'react';

interface ViewportDefault {
    width: null | number;
    height: null | number;
}

const viewportDefault: ViewportDefault = {
    width: null,
    height: null
};

export const ViewportContext = React.createContext(viewportDefault);