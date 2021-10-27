import React, { useContext, useEffect, useState } from 'react';
import { CardListStyleContext } from '../../../utils/contexts';
import Card from '../../Cards/Card';
import './SearchResult.scss';

interface SearchResultProps {

}

const SearchResultList: React.FC<SearchResultProps> = (props) => {
    const [resultCards, setResultCards] = useState<Array<React.ReactElement>>([
        <Card horizontal={true} />,
        <Card horizontal={true} />,
        <Card horizontal={true} />,
        <Card horizontal={true} />,
        <Card horizontal={true} />,
        <Card horizontal={true} />,
        <Card horizontal={true} />,
        <Card horizontal={true} />,
        <Card horizontal={true} />,
        <Card horizontal={true} />
    ]);
    const { resultStyleList } = useContext(CardListStyleContext);

    useEffect(() => {
        console.log('Result list style toggled!', resultStyleList);
    }, [resultStyleList]);

    return (
        <div className="search-result-list">
            { resultCards }
        </div>
    );
};

export default SearchResultList;