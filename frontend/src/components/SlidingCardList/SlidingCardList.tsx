import { Link } from "react-router-dom";
import Card from "../Cards/Card";
import './SlidingCardList.scss';

interface SlidingCardListProps {
    title: string;
}

const SlidingCardList: React.FC<SlidingCardListProps> = (props) => {
    return (
        <div className="sliding-card-list">
            <div className="list-title-container">
                <div className="list-title">{props.title}</div>
                <div className="list-more">
                    <Link to='/all-stories'>
                        <div className="link-more-title">
                            more
                        </div>
                        <div className="link-more-icon">
                            &gt;
                        </div>
                    </Link>
                </div>
            </div>
            <div className="card-list">
                <Card />
                <Card />
                <Card />
                <Card />
                <Card />
                <Card />
                <Card />
                <Card />
                <Card />
                <Card />
                <Card />
                <Card />
                <Card />
                <Card />
            </div>
        </div>
    );
};

export default SlidingCardList;