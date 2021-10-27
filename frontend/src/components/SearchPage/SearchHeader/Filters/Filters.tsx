import { ReactComponent as FilterIcon } from '../../../../assets/imgs/icon_filter.svg';

const Filters: React.FC = (props) => {
    return (
        <div className="search-options-icon filters">
            <FilterIcon />
        </div>
    );
};

export default Filters;