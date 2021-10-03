import React, { useRef, useState } from 'react';
import { Link } from 'react-router-dom';
import { ReactComponent as WriteIcon } from '../../assets/imgs/icon_write.svg';
import { ReactComponent as ExploreIcon } from '../../assets/imgs/icon_explore.svg';
import { ReactComponent as HomeIcon } from '../../assets/imgs/icon_home.svg';
import { ReactComponent as PopularIcon } from '../../assets/imgs/icon_trending.svg';
import { ReactComponent as ProfileIcon } from '../../assets/imgs/icon_profile.svg';
import './SubMenuBar.scss';
import useViewport from '../../hooks/useViewport';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';

interface SubMenuItemProps {
    icon: JSX.Element
    label: string;
    linkTo: string;
}

const SubMenuItem: React.FC<SubMenuItemProps> = (props) => {
    const { isMobile } = useViewport();

    return (
        <div className="sub-menu-item" title={props.label}>
            <Link to={props.linkTo}>
                <div className="sub-menu-item-icon">
                    {props.icon}
                </div>
                {
                    isMobile &&
                        <div className="sub-menu-item-label">
                            {props.label}
                        </div>
                }
            </Link>
        </div>
    );
};

const SubMenuBar: React.FC = (props) => {
    const [showItems, setShowItems] = useState(false);
    const menuItems = useRef([
        { linkTo: '/write', label: 'Write', icon: <WriteIcon /> },
        { linkTo: '/explore', label: 'Explore', icon: <ExploreIcon /> },
        { linkTo: '/home', label: 'Home', icon: <HomeIcon /> },
        { linkTo: '/popular', label: 'Popular', icon: <PopularIcon /> },
        { linkTo: '/profile', label: 'Profile', icon: <ProfileIcon /> }
    ]);

    const switchMenuItems: React.MouseEventHandler = (ev: React.MouseEvent) => {
        setShowItems(showItems => !showItems);
    };

    return (
        <div className="sub-menu-bar">
            <div className="sub-menu-switch" onClick={switchMenuItems}>
                <FontAwesomeIcon icon={`${showItems? 'times' : 'ellipsis-h'}`} height='85%' width='85%'/>
            </div>
            <div className={`sub-menu-items ${showItems? 'show-sub-menu-items' : ''}`}>
                {
                    menuItems.current.map((menuItem) => (
                        <SubMenuItem {...menuItem} key={menuItem.label}/>
                    ))
                }
            </div>
        </div>
    );
};

export default SubMenuBar;