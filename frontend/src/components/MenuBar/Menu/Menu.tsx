import { Link } from 'react-router-dom';
import './Menu.scss';

interface MenuProps {
    showMenu: boolean;
}

const Menu: React.FC<MenuProps> = (props) => {
    return (
        <div className={`menu ${props.showMenu? '' : 'hide-menu'}`}>
            <div className="menu-links">
                <div className="menu-link">
                    <Link to='/home'>Home</Link>
                </div>
                <div className="menu-link">
                    <Link to='/about'>About</Link>
                </div>
                <div className="menu-link">
                    <Link to='/privacy-policy'>Privacy Policy</Link>
                </div>
                <div className="menu-link">
                    <Link to='/t-and-c'>Terms and Conditions</Link>
                </div>
            </div>

            <div className="menu-buttons">
                <button>Log In</button>
                <button>Sign Up</button>
            </div>
        </div>
    );
};

export default Menu;