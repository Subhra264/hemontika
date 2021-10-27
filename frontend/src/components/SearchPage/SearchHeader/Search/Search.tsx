import './Search.scss';
import { ReactComponent as SearchIcon } from '../../../../assets/imgs/icon_search.svg';

const Search: React.FC = (props) => {
    return (
        <div className="search">
            <form>
                <input type='text' placeholder='Search' className='search-input' />
                <button type='submit' ><SearchIcon /></button>
            </form>
        </div>
    );
};

export default Search;