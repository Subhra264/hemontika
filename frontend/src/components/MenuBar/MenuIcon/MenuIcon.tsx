import { ReactComponent as MenuIconContainer } from '../../../assets/imgs/svg_menu_container.svg';
import Menu from '../Menu/Menu';
import './MenuIcon.scss';

interface MenuIconProps {
    showMenu: boolean;
    switchShowMenu: React.MouseEventHandler;
}

const MenuIcon: React.FC<MenuIconProps> = (props) => {
    return (
        <div className="menu-icon-container-wrapper">
            <div className="menu-icon-container">
                <MenuIconContainer />
                <div className={`menu-icon ${props.showMenu? 'active' : ''}`} onClick={props.switchShowMenu}>
                    <div className="bar"></div>
                </div>
            </div>
            <Menu />
        </div>
    );
};

export default MenuIcon;