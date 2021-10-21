import './Card.scss';

const Card: React.FC = (props) => {
    return (
        <div className="card">
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
        </div>
    );
};

export default Card;