import './MenuBar.scss';
import React, { useState } from 'react';
import MenuIcon from './MenuIcon/MenuIcon';

const MenuBar: React.FC = (props): JSX.Element => {
    const [showMenu, setShowMenu] = useState(false);

    const switchShowMenu: React.MouseEventHandler = (ev: React.MouseEvent) => {
        setShowMenu(showMenu => !showMenu);
    };

    return (
        <div className="menu-bar-container">
            <div className="menu-bar">
                <div className="menu-logo">LOGO</div>
                <div className="menu-buttons">
                    <button>Log In</button>
                    <button>Sign Up</button>
                </div>
                <MenuIcon showMenu={showMenu} switchShowMenu={switchShowMenu} />
            </div>
        </div>
    );
};

export default MenuBar;