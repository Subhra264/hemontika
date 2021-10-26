

interface SearchOptionsProps {
    resultListHorStyle: boolean;
}

const SearchOptions: React.FC<SearchOptionsProps> = (props) => {
    return (
        <div className="search-options">
            <div className="toggle-result-list-style">
                T
            </div>
        </div>
    );
};

export default SearchOptions;