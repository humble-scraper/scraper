import styled from "styled-components";

import { urlFor } from "../../util";
import BundleContentProps from "./BundleContentProps";

const CollapsedRoot = styled.div`
  height: 300px;
  width: 350px;
  background-color: #282c34;
  margin: 1%;
  display: block;
`;

const CollapsedFlex = styled.div`
  display: flex;
  flex-direction:row;
  width: inherit;
  height:29%
`;

const Title = styled.div.attrs({
  children: "Pink Butterfly",
})`
  background-color: #645b5b;
  width:50%;
  padding:0.5em;
`;

const ImgService = styled.img.attrs({
  src: urlFor("image_placeholder.jpg"),
  alt: "Some image",
})`
  height: 70%;
  width: inherit;
  background-color: #282c34;
  margin: none;
`;

const BigAssButton = styled.button`
  width: 50%;
`;

const Collapsed = ({ open }: BundleContentProps): JSX.Element => (
  <CollapsedRoot>
    <ImgService />
    <CollapsedFlex>
      <Title />
      <BigAssButton onClick={open}>Collapsed View</BigAssButton>
    </CollapsedFlex>
  </CollapsedRoot>
);

export default Collapsed;
