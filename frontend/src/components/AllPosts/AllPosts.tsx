import ResponsiveWrapper from '../ResponsiveWrapper/ResponsiveWrapper';
import AllPostsList from './AllPostsList/AllPostsList';

const AllPosts: React.FC = (props) => {
    return (
        <ResponsiveWrapper>
            <h2>All Posts</h2>
            <AllPostsList />
        </ResponsiveWrapper>
    );
};

export default AllPosts;