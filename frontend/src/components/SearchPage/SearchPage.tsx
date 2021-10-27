import { useState } from 'react';
import { CardListStyleContext } from '../../utils/contexts';
import ResponsiveWrapper from '../ResponsiveWrapper/ResponsiveWrapper';
import SearchHeader from './SearchHeader/SearchHeader';
import SearchResult from './SearchResult/SearchResult';

const SearchPage: React.FC = (props) => {
    const [resultStyleList, setResultStyleList] = useState(false);

    return (
        <ResponsiveWrapper>
            <CardListStyleContext.Provider
                value={{
                    resultStyleList,
                    setResultStyleList
                }}
            >
                <h2>All Posts</h2>
                <SearchHeader />
                <SearchResult  />
            </CardListStyleContext.Provider>
        </ResponsiveWrapper>
    );
};

export default SearchPage;