import { useContext } from 'react';
import { ViewportContext } from '../utils/contexts';

export default function useViewport () {
    const { width, height } = useContext(ViewportContext);
    const isMobile: boolean = width? width <= 720 : false;

    return { width, height, isMobile };
}