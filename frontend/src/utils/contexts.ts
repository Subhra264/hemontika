import React from 'react';

interface ViewportDefault {
    width: null | number;
    height: null | number;
}

interface CardListStyleDefault {
    resultListHorStyle: null | boolean;
    setResultListHorStyle: null | React.Dispatch<React.SetStateAction<boolean>>;
}

const viewportDefault: ViewportDefault = {
    width: null,
    height: null
};

const cardListStyleDefault: CardListStyleDefault = {
    resultListHorStyle: null,
    setResultListHorStyle: null
};

export const ViewportContext = React.createContext(viewportDefault);
export const CardListStyleContext = React.createContext(cardListStyleDefault);