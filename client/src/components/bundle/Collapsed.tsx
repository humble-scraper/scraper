import styled from "styled-components";
import BundleContentProps from "./BundleContentProps";

const BigAssButton = styled.button``;

const Collapsed = ({open}: BundleContentProps): JSX.Element => (
  <div>
    <BigAssButton onClick={open}>Collapsed View</BigAssButton>
  </div>
);

export default Collapsed;
