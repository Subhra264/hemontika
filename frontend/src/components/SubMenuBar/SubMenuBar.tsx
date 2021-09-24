import { useRef } from 'react';
import { Link } from 'react-router-dom';
import { ReactComponent as WriteIcon } from '../../assets/imgs/icon_write.svg';
import { ReactComponent as ExploreIcon } from '../../assets/imgs/icon_explore.svg';
import { ReactComponent as HomeIcon } from '../../assets/imgs/icon_home.svg';
import { ReactComponent as PopularIcon } from '../../assets/imgs/icon_trending.svg';
import { ReactComponent as ProfileIcon } from '../../assets/imgs/icon_profile.svg';
import './SubMenuBar.scss';

interface SubMenuItemProps {
    icon: JSX.Element
    label: string;
    linkTo: string;
}

const SubMenuItem: React.FC<SubMenuItemProps> = (props) => {
    return (
        <div className="sub-menu-item">
            <Link to={props.linkTo}>
                <div className="sub-menu-item-icon">
                    {props.icon}
                </div>
                <div className="sub-menu-item-label">
                    {props.label}
                </div>
            </Link>
        </div>
    );
};

const SubMenuBar: React.FC = (props) => {
    const menuItems = useRef([
        { linkTo: '/write', label: 'Write', icon: <WriteIcon /> },
        { linkTo: '/explore', label: 'Explore', icon: <ExploreIcon /> },
        { linkTo: '/home', label: 'Home', icon: <HomeIcon /> },
        { linkTo: '/popular', label: 'Popular', icon: <PopularIcon /> },
        { linkTo: '/profile', label: 'Profile', icon: <ProfileIcon /> }
    ]);

    return (
        <div className="sub-menu-bar">
            <div className="sub-menu-switch"></div>
            <div className="sub-menu-items">
                {
                    menuItems.current.map((menuItem) => (
                        <SubMenuItem {...menuItem} />
                    ))
                }
            </div>
        </div>
    );
};

export default SubMenuBar;