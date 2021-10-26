import { useState } from 'react';
import { CardListStyleContext } from '../../utils/contexts';
import ResponsiveWrapper from '../ResponsiveWrapper/ResponsiveWrapper';
import SearchHeader from './SearchHeader/SearchHeader';
import SearchResultList from './SearchResultList/SearchResultList';

const SearchPage: React.FC = (props) => {
    const [resultListHorStyle, setResultListHorStyle] = useState(false);

    return (
        <ResponsiveWrapper>
            <CardListStyleContext.Provider
                value={{
                    resultListHorStyle,
                    setResultListHorStyle
                }}
            >
                <h2>All Posts</h2>
                <SearchHeader resultListHorStyle={resultListHorStyle} />
                <SearchResultList resultListHorStyle={resultListHorStyle} />
            </CardListStyleContext.Provider>
        </ResponsiveWrapper>
    );
};

export default SearchPage;