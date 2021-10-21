import { ViewportContext } from '../../utils/contexts';
import { useState, useEffect } from 'react';

const ViewportProvider: React.FC = ({ children }) => {
    const [width, setWidth] = useState<null | number>(null);
    const [height, setHeight] = useState<null | number>(null);

    useEffect(() => {
        console.log('Viewport provider...');

        const handleResizeWindow = () => {
            console.log('Called handleResizeWindow...');
            setWidth(window.innerWidth);
            setHeight(window.innerHeight);
        };

        handleResizeWindow();
        window.addEventListener('resize', handleResizeWindow);

        return () => window.removeEventListener('resize', handleResizeWindow);
    }, []);

    return (
        <ViewportContext.Provider value={{ width, height }} >
            {children}
        </ViewportContext.Provider>
    );
};

export default ViewportProvider;