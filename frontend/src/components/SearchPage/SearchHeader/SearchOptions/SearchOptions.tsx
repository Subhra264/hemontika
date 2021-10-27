import { useContext } from 'react';
import { CardListStyleContext } from '../../../../utils/contexts';
import Filters from '../Filters/Filters';
import { ReactComponent as ListIcon } from '../../../../assets/imgs/icon_list.svg';
import { ReactComponent as GalleryIcon } from '../../../../assets/imgs/icon_gallery.svg';
import './SearchOptions.scss';

const SearchOptions: React.FC = (props) => {
    const { resultStyleList, setResultStyleList } = useContext(CardListStyleContext);

    const toggleListStyle = () => {
        if (setResultStyleList) setResultStyleList(prevListStyle => !prevListStyle);
    };

    return (
        <div className="search-options">
            <Filters />
            <div className="search-options-icon toggle-result-list-style" onClick={toggleListStyle}>
                {
                    resultStyleList? 
                        <ListIcon />
                    : 
                        <GalleryIcon />
                }
            </div>
        </div>
    );
};

export default SearchOptions;