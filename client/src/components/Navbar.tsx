import styled from "styled-components";
import { urlFor } from "../util";

const ImgLogo = styled.img.attrs({
  src: urlFor("logo.png"),
})`
  height: 10%;
  padding: 1.25em;
  box-sizing: initial;
`;

const Search = styled.input.attrs({
})`
   width: 100%;
  height: 1%;
  padding: 1.25em;
  box-sizing: initial;
  margin: 1em;
`;
const SearchBar = styled.div`


`;

const Row = styled.div`
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  align-items: top;
`;

const Navbar = styled.div.attrs({
  children: (
    <Row>
      <ImgLogo />
      <SearchBar />
    </Row>
  ),
})`
  background-color: #494f5c;
  color: #d8d8da;
  border-bottom: 1px #373c46 solid;
  box-shadow: 1px 2px 3px #00000045;
  height: 65px;
  width: 100%;
  display: "flex";
  justify-content: center;
  align-items: center;
  position: sticky;
`;

export default Navbar;
