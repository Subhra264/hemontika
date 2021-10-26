import Search from './Search/Search';
import SearchOptions from './SearchOptions/SearchOptions';

interface SearchHeaderProps {
    resultListHorStyle: boolean;
}

const SearchHeader: React.FC<SearchHeaderProps> = (props) => {
    return (
        <div className="search-container">
            <Search />
            <SearchOptions resultListHorStyle={props.resultListHorStyle} />
        </div>
    );
};

export default SearchHeader;