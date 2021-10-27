import React from 'react';

interface ViewportDefault {
    width: null | number;
    height: null | number;
}

interface CardListStyleDefault {
    resultStyleList: null | boolean;
    setResultStyleList: null | React.Dispatch<React.SetStateAction<boolean>>;
}

const viewportDefault: ViewportDefault = {
    width: null,
    height: null
};

const cardListStyleDefault: CardListStyleDefault = {
    resultStyleList: false,
    setResultStyleList: null
};

export const ViewportContext = React.createContext(viewportDefault);
export const CardListStyleContext = React.createContext(cardListStyleDefault);