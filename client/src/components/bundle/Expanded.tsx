import styled from "styled-components";
import BundleContentProps from "./BundleContentProps";

const BigAssButton = styled.button``;

const Expanded = ({open}: BundleContentProps): JSX.Element => (
  <div>
    <BigAssButton onClick={open}>Expanded View</BigAssButton>
  </div>
);

export default Expanded;