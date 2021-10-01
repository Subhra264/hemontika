import './MenuBar.scss';
import { ReactComponent as MenuIconContainer } from '../../assets/imgs/svg_menu_container.svg';
import React, { useState } from 'react';

const MenuBar: React.FC = (props): JSX.Element => {
    const [showMenu, setShowMenu] = useState(false);

    const switchShowMenu: React.MouseEventHandler = (ev: React.MouseEvent) => {
        setShowMenu(showMenu => !showMenu);
    };

    return (
        <div className="menu-bar-container">
            <div className="menu-icon-container">
                <MenuIconContainer  />
                <div className={`menu-icon ${showMenu? 'active' : ''}`} onClick={switchShowMenu}>
                    <div className="bar"></div>
                </div>
            </div>
        </div>
    );
};

export default MenuBar;