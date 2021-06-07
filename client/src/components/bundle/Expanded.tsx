import styled from "styled-components";
import { urlFor } from "../../util";
import BundleContentProps from "./BundleContentProps";

const ExpandedRoot = styled.div`
  height: 300px;
  width: 350px;
  background: linear-gradient(
    to right,
    #bf953f,
    #fcf6ba,
    #b38728,
    #fbf5b7,
    #aa771c
  );
  margin: 1%;
  display: block;
`;

const ExpandedFlex = styled.div`
  display: flex;
  flex-direction: row;
  width: inherit;
  height: 29%;
`;

const ImgService = styled.img.attrs({
  src: urlFor("image_placeholder2.jpg"),
  alt: "Some image but expanded",
})`
  height: 70%;
  width: inherit;
  background-color: #a59225;
`;
const Title = styled.div.attrs({
  children: "Gold Butterfly",
})`
  background-color: #645b5b;
  width:50%;
  padding:0.5em;
`;


const BigAssButton = styled.button`
width: 50%;
`;

const Expanded = ({ open }: BundleContentProps): JSX.Element => (
  <ExpandedRoot>
    <ImgService />
    <ExpandedFlex>
      <Title />
      <BigAssButton onClick={open}>Expanded View</BigAssButton>
    </ExpandedFlex>
  </ExpandedRoot>
);

export default Expanded;
