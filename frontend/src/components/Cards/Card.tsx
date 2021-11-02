import { Link } from 'react-router-dom';
import './Card.scss';

interface CardProps {
    // horizontal?: boolean;
}

const Card: React.FC<CardProps> = (props) => {
    return (
        <Link to='/stories/story-id' className="card">
            <div className="card-img">

            </div>
            <div className="card-details">
                <div className="card-title">A Literature</div>
                <div className="card-impression">
                    <div className="card-rating">4.3</div>
                    <div className="card-category">Horror</div>
                </div>
                <div className="card-read-time">6 min read</div>
            </div>
        </Link>
    );
};

export default Card;