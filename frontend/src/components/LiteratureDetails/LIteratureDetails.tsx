import ResponsiveWrapper from '../ResponsiveWrapper/ResponsiveWrapper';
import { ReactComponent as StarIcon } from '../../assets/imgs/icon_star.svg';
import { ReactComponent as DownloadIcon } from '../../assets/imgs/icon_download.svg';
import { ReactComponent as ShareIcon } from '../../assets/imgs/icon_share.svg';
import './LiteratureDetails.scss';

const LiteratureDetails: React.FC = (props) => {
    return (
        <ResponsiveWrapper >
            <div className="literature-details">
                <div className="details-img">

                </div>
                <div className="details-content">
                    <div className="details-title">
                        Greatest Name in the WORLD
                    </div>
                    <div className="details-author">
                        <div className="author-pic"></div>
                        <div className="author-name">Abhradeep Chakraborty</div>
                    </div>
                    <div className="details-impressions">
                        <div className="impression details-rating">
                            <div className="rating-stars">4.3</div>
                            <div className="rating-star-icon"><StarIcon /></div>
                        </div>
                        <div className="impression read-time">6 min. read</div>
                        <div className="impression views">12 views</div>
                    </div>
                    <div className="details-published-on">
                        published on - 25th December, 2020
                    </div>
                    <div className="details-tags">
                        tags: 
                        <div className="details-tag">horror</div>
                        <div className="details-tag">horror</div>
                        <div className="details-tag">horror</div>
                    </div>
                    <div className="details-summary">
                        <div className="details-summary-heading">
                            Summary
                            <div className="heading-underline"></div>
                        </div>
                        <div className="details-summary-content">
                            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quibusdam natus aliquam tempore assumenda? Accusamus aut, expedita iure ipsam similique quae, labore commodi ipsa, tenetur possimus doloribus totam amet tempore consequuntur.
                        </div>
                    </div>
                    <div className="details-buttons">
                        <button className="start-reading">Start Reading</button>
                        <div className="details-button-icons">
                            {/* <div className="details-button"> */}
                                <DownloadIcon />
                            {/* </div> */}
                            {/* <div className="details-button"> */}
                                <ShareIcon />
                            {/* </div> */}
                        </div>
                    </div>
                    {/* <div className="details-comments">
                        <div className="comments-header">
                            .
                        </div>
                    </div> */}
                </div>
            </div>
        </ResponsiveWrapper>
    );
};

export default LiteratureDetails;