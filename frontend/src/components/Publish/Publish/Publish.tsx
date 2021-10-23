import { Link } from 'react-router-dom';
import ResponsiveWrapper from '../../ResponsiveWrapper/ResponsiveWrapper';
import './Publish.scss';

const Publish: React.FC = (props) => {
    return (
        <ResponsiveWrapper className="publish">
            <section>
                <h2>
                    <div className="h2-heading">
                        Continue Editing
                    </div>
                </h2>
                <div className="publish-sec-items">
                    <div className="publish-sec-item">
                        <Link to='/abc' className="publish-sec-item-title">
                            Title
                        </Link>
                        <span className="publish-sec-item-type">
                            Story
                        </span>
                    </div>
                    <div className="publish-sec-item">
                        <span className="publish-sec-item-title">
                            <Link to='/abc'>Title</Link>
                        </span>
                        <span className="publish-sec-item-type">
                            Story
                        </span>
                    </div>
                    <div className="publish-sec-item">
                        <span className="publish-sec-item-title">
                            <Link to='/abc'>Title</Link>
                        </span>
                        <span className="publish-sec-item-type">
                            Story
                        </span>
                    </div>
                    <div className="publish-sec-item">
                        <span className="publish-sec-item-title">
                            <Link to='/abc'>Title</Link>
                        </span>
                        <span className="publish-sec-item-type">
                            Story
                        </span>
                    </div>
                    <div className="publish-sec-item">
                        <span className="publish-sec-item-title">
                            <Link to='/abc'>Title</Link>
                        </span>
                        <span className="publish-sec-item-type">
                            Story
                        </span>
                    </div>
                </div>
            </section>
            <section>
                <h2>
                    <div className="h2-heading">
                        Publish New
                    </div>
                </h2>
                <div className="publish-sec-items">
                    <div className="publish-sec-item publish-option">
                        <span className="publish-sec-item-title">
                            {/* <Link to='/new-poem'>Write a Poem</Link> */}
                            Write a Poem
                        </span>
                        <Link to='/new-poem' className="publish-sec-item-type">
                            &gt;
                        </Link>
                    </div>
                    <div className="publish-sec-item publish-option">
                        <span className="publish-sec-item-title">
                            {/* <Link to='/new-poem'>Write a Poem</Link> */}
                            Write a Poem
                        </span>
                        <Link to='/new-poem' className="publish-sec-item-type">
                            &gt;
                        </Link>
                    </div>
                    <div className="publish-sec-item publish-option">
                        <span className="publish-sec-item-title">
                            {/* <Link to='/new-poem'>Write a Poem</Link> */}
                            Write a Poem
                        </span>
                        <Link to='/new-poem' className="publish-sec-item-type">
                            &gt;
                        </Link>
                    </div>
                    <div className="publish-sec-item publish-option">
                        <span className="publish-sec-item-title">
                            {/* <Link to='/new-poem'>Write a Poem</Link> */}
                            Write a Poem
                        </span>
                        <Link to='/new-poem' className="publish-sec-item-type">
                            &gt;
                        </Link>
                    </div>
                </div>
            </section>
        </ResponsiveWrapper>
    );
};

export default Publish;