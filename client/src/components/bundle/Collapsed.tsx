import { MouseEventHandler } from "react";
import styled from "styled-components";
import { urlFor } from "../../util";
import BundleContentProps from "./BundleContentProps";

const CollapsedRoot = styled.div`
  height: 300px;
  width: 350px;
  background-color: #282c34;
  margin: 1%;
  display: block;
  box-shadow: 0 4px 8px 0 rgba(255, 255, 255, 0.2),
    0 6px 20px 0 rgba(247, 244, 244, 0.19);
`;

const CollapsedFlex = styled.div`
  display: flex;
  flex-direction: row;
  width: inherit;
  height: 29%;
`;

const Title = styled.div.attrs({
  children: "Pink Butterfly",
})`
  width: 50%;
  padding: 0.5em;
  text-align: center;
  font-size: large;
  font-family: Arial, Helvetica, sans-serif;
  font-weight: bold;
  color: white;
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
  width: 30%;
  height: 50%;
  margin-left: 2.1em;
  align-self: center;
  border-radius: 4px;
  background-color: inherit;
  color: white;
`;

type CollapsedProps = { open?: MouseEventHandler<HTMLButtonElement> };

const Collapsed = (
  { open }: CollapsedProps = { open: () => undefined }
): JSX.Element => (
  <CollapsedRoot>
    <ImgService />
    <CollapsedFlex>
      <Title />
      <BigAssButton onClick={open}>Collapsed View</BigAssButton>
    </CollapsedFlex>
  </CollapsedRoot>
);

export default Collapsed;
