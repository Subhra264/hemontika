import { Link } from 'react-router-dom';
import ResponsiveWrapper from '../../ResponsiveWrapper/ResponsiveWrapper';
import './Publish.scss';

const Publish: React.FC = (props) => {
    return (
        <ResponsiveWrapper className="publish">
            <div>
                <h2>Continue Editing</h2>
                <div className="pending-works">
                    <div className="pending-work">
                        <span className="pending-work-title">
                            <Link to='/abc'>Title</Link>
                        </span>
                        <span className="pending-work-type">
                            Story
                        </span>
                    </div>
                    <div className="pending-work">
                        <span className="pending-work-title">
                            <Link to='/abc'>Title</Link>
                        </span>
                        <span className="pending-work-type">
                            Story
                        </span>
                    </div>
                    <div className="pending-work">
                        <span className="pending-work-title">
                            <Link to='/abc'>Title</Link>
                        </span>
                        <span className="pending-work-type">
                            Story
                        </span>
                    </div>
                    <div className="pending-work">
                        <span className="pending-work-title">
                            <Link to='/abc'>Title</Link>
                        </span>
                        <span className="pending-work-type">
                            Story
                        </span>
                    </div>
                    <div className="pending-work">
                        <span className="pending-work-title">
                            <Link to='/abc'>Title</Link>
                        </span>
                        <span className="pending-work-type">
                            Story
                        </span>
                    </div>
                </div>
            </div>
            <div>
                <h2>Publish New</h2>
                <div className="publish-new-options">
                    <div className="publish-new-option">
                        <Link to='/new-poem'>Write a Poem</Link>
                    </div>
                </div>
            </div>
        </ResponsiveWrapper>
    );
};

export default Publish;