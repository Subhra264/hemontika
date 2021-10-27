import Search from './Search/Search';
import SearchOptions from './SearchOptions/SearchOptions';
import './SearchHeader.scss';

const SearchHeader: React.FC = (props) => {
    return (
        <div className="search-container">
            <Search />
            <SearchOptions />
        </div>
    );
};

export default SearchHeader;