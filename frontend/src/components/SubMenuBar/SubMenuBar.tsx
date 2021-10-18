import React, { useEffect, useRef, useState } from 'react';
import { Link, useLocation } from 'react-router-dom';
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
    active: boolean;
}

const SubMenuItem: React.FC<SubMenuItemProps> = (props) => {
    const { isMobile } = useViewport();

    return (
        <div className={`sub-menu-item ${props.active? 'active' : ''}`} title={props.label}>
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
    const [activeLinkIndex, setActiveLinkIndex] = useState(2);
    const location = useLocation();
    const menuItems = useRef([
        { linkTo: '/write', label: 'Write', icon: <WriteIcon /> },
        { linkTo: '/explore', label: 'Explore', icon: <ExploreIcon /> },
        { linkTo: '/home', label: 'Home', icon: <HomeIcon /> },
        { linkTo: '/popular', label: 'Popular', icon: <PopularIcon /> },
        { linkTo: '/profile', label: 'Profile', icon: <ProfileIcon /> }
    ]);

    const getCurrRouteIndex = (): number => {
        let currentRouteIndex = 2;
        console.log('Location', location);

        for (let i = 0; i < menuItems.current.length; i++) {
            const linkTo = menuItems.current[i].linkTo;
            console.log('getCurrRouteIndex linkTo', linkTo);
            console.log('getCurrRouteIndex location.pathname', location.pathname);
            if (linkTo === location.pathname
                || (linkTo !== '/'
                    && location.pathname.startsWith(linkTo)
                )) {
                currentRouteIndex = i;
                break;
            }
        }
        console.log('getCurrRouteIndex current index', currentRouteIndex);
        return currentRouteIndex;
    };

    useEffect(() => {
        console.log('Inside useEffect SubMenuBar');
        setActiveLinkIndex(getCurrRouteIndex());
    }, [location]);

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
                    menuItems.current.map((menuItem, index) => {
                        let active = false;
                        if (index === activeLinkIndex) {
                            active = true;
                        }
                        return <SubMenuItem {...menuItem} active={active} key={menuItem.label}/>
                    })
                }
            </div>
        </div>
    );
};

export default SubMenuBar;