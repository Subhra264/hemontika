import './ResponsiveWrapper.scss';

interface ResponsiveWrapperProps {
    className: string;
}

const ResponsiveWrapper: React.FC<ResponsiveWrapperProps> = (props) => {
    return (
        <div className={`responsive-wrapper ${props.className && props.className}`}>
            { props.children }
        </div>
    );
};

export default ResponsiveWrapper;