import { Link } from "react-router-dom";


const Publish: React.FC = (props) => {
    return (
        <div className="publish">
            <section>
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
                </div>
            </section>
            <section>
                <h2>Publish New</h2>
                
            </section>
        </div>
    );
};

export default Publish;