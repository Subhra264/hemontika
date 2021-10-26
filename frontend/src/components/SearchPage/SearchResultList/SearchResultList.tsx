import Card from '../../Cards/Card';
import './SearchResultList.scss';

interface SearchResultListProps {
    resultListHorStyle: boolean;
}

const SearchResultList: React.FC<SearchResultListProps> = (props) => {

    const returnCards = () => {
        for (let i = 0; i < 9; i++) {
            return <Card horizontal={true} />
        }
    };

    return (
        <div className="search-result-list">
            { returnCards() }
        </div>
    );
};

export default SearchResultList;